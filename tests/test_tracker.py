import copy
import json
import os
import tempfile
import unittest
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

from src.core import PaperStore, canonical_doi, classify, read_json, write_json, year_bounds
from src.output import render_library
from src.runner import load_config, run
from src.sources import SourceError, collect_arxiv, collect_dblp, collect_eprint, parse_arxiv, parse_dblp, parse_eprint, parse_dblp_sparql, sparql_query
from scripts.publish_digest import publish

ROOT = Path(__file__).resolve().parent.parent
NOW = datetime(2026, 10, 29, 1, 17, tzinfo=timezone.utc)


def paper(title="Secure multiparty computation with secret sharing", source="arxiv", identifier="2610.00001", doi="", abstract=""):
    return {"title": title, "abstract": abstract, "authors": ["Alice"], "topics": ["MPC"], "matched_terms": {"MPC": ["secret sharing"]},
            "records": [{"source": source, "id": identifier, "doi": doi, "url": "https://example.org/paper", "year": "2026",
                         "published": "2026-10-20T00:00:00Z", "updated": "2026-10-22T00:00:00Z", "venue": source}]}


class Response:
    def __init__(self, data=None, text=""):
        self.data = data
        self.text = text

    def json(self):
        return self.data

    def raise_for_status(self):
        pass


class Client:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.calls = []

    def get(self, url, params):
        self.calls.append((url, params.copy()))
        return next(self.responses)


def atom(entries, total=None):
    body = "".join(f'<entry><id>http://arxiv.org/abs/{ident}</id><title>{title}</title><updated>{updated}</updated>'
                   '<published>2026-10-01T00:00:00Z</published><summary>Secure computation.</summary><author><name>Alice</name></author></entry>'
                   for ident, title, updated in entries)
    return ('<feed xmlns="http://www.w3.org/2005/Atom" xmlns:o="http://a9.com/-/spec/opensearch/1.1/">'
            f'<o:totalResults>{len(entries) if total is None else total}</o:totalResults>{body}</feed>')


def oai(token="", error=""):
    if error:
        body = f'<error code="{error}">message</error>'
    else:
        body = ('<ListRecords><record><header><identifier>oai:eprint.iacr.org:2026/1234</identifier><datestamp>2026-10-25T00:00:00Z</datestamp></header>'
                '<metadata><oai_dc:dc><dc:title>Oblivious transfer</dc:title><dc:creator>Alice</dc:creator><dc:description>Protocol abstract.</dc:description>'
                '<dc:date>2026-10-24T00:00:00Z</dc:date><dc:date>2026-10-25T00:00:00Z</dc:date></oai_dc:dc></metadata></record>'
                f'<resumptionToken>{token}</resumptionToken></ListRecords>')
    return ('<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/" '
            f'xmlns:dc="http://purl.org/dc/elements/1.1/">{body}</OAI-PMH>')


class MatchingTests(unittest.TestCase):
    def setUp(self):
        self.cfg = load_config(ROOT / "config.yaml")

    def test_generic_fl_is_not_tracked(self):
        self.assertEqual(classify(paper("FedAvg: Efficient Federated Learning", abstract="Robust local SGD and non-IID data."), self.cfg), {})

    def test_relevant_fl_crossovers_and_optional_exclusion(self):
        p = paper("Federated Learning with Secure Multi-Party Computation")
        self.assertIn("MPC", classify(p, self.cfg))
        self.cfg["tracking"]["exclude_federated_learning"] = True
        self.assertEqual(classify(p, self.cfg), {})

    def test_tee_independent_of_mpc(self):
        self.assertEqual(set(classify(paper("Fast remote attestation in Intel SGX"), self.cfg)), {"TEE"})

    def test_acronym_disambiguation(self):
        for text in ["Secure model predictive control (MPC) of a vehicle", "TEE for transesophageal echocardiography", "The enclave economy in regional development"]:
            self.assertEqual(classify(paper(text), self.cfg), {}, text)
        self.assertIn("MPC", classify(paper("Efficient MPC against malicious adversaries"), self.cfg))

    def test_both_topics_and_hyphen_variants(self):
        self.assertEqual(set(classify(paper("Multi-party computation in trusted execution environments"), self.cfg)), {"MPC", "TEE"})


class IdentityTests(unittest.TestCase):
    def test_sources_merge_by_normalized_title_and_keep_links(self):
        store = PaperStore()
        identifier, _ = store.add(paper(), NOW.isoformat())
        incoming = paper(title="Secure Multiparty Computation with Secret Sharing.", source="eprint", identifier="2026/1234")
        same, is_new = store.add(incoming, NOW.isoformat())
        self.assertEqual(same, identifier)
        self.assertFalse(is_new)
        self.assertEqual(len(store.papers[identifier]["records"]), 2)

    def test_version_title_changes_do_not_create_a_new_paper(self):
        store = PaperStore()
        identifier, _ = store.add(paper(identifier="2610.00001v1"), NOW.isoformat())
        same, fresh = store.add(paper(title="An improved secure computation protocol", identifier="2610.00001v2"), NOW.isoformat())
        self.assertEqual(same, identifier)
        self.assertFalse(fresh)
        self.assertEqual(len(store.papers[identifier]["records"]), 1)

    def test_doi_bridge_merges_existing_records(self):
        store = PaperStore()
        first, _ = store.add(paper(title="First title", doi="https://doi.org/10.1234/ABC"), NOW.isoformat())
        second, _ = store.add(paper(title="Different title", source="eprint", identifier="2026/99"), NOW.isoformat())
        merged, fresh = store.add(paper(title="Different title", source="dblp", identifier="conf/crypto/X26", doi="10.1234/abc"), NOW.isoformat())
        self.assertFalse(fresh)
        self.assertEqual(len(store.papers), 1)
        self.assertEqual(store.resolve(first), merged)
        self.assertEqual(store.resolve(second), merged)

    def test_missing_urls_do_not_collapse_distinct_papers(self):
        store = PaperStore()
        store.add(paper(title="Protocol alpha", identifier="a"), NOW.isoformat())
        store.add(paper(title="Protocol beta", identifier="b"), NOW.isoformat())
        self.assertEqual(len(store.papers), 2)


class SourceTests(unittest.TestCase):
    def test_arxiv_versions_and_abstracts(self):
        entries, total = parse_arxiv(atom([("2610.00001v3", "Secure MPC", "2026-10-23T00:00:00Z")]))
        self.assertEqual(entries[0]["records"][0]["id"], "2610.00001")
        self.assertEqual(entries[0]["abstract"], "Secure computation.")
        self.assertEqual(total, 1)

    def test_arxiv_api_errors_are_not_zero_results(self):
        with self.assertRaises(SourceError):
            parse_arxiv(atom([("../api/errors#incorrect_id_format", "Error", "2026-10-23")]))

    def test_arxiv_paginates_until_cutoff(self):
        cfg = load_config(ROOT / "config.yaml")
        cfg["topics"] = {"MPC": {"arxiv_terms": ['"secure computation"']}}
        cfg["sources"]["arxiv"]["page_size"] = 1
        client = Client([Response(text=atom([("2610.1", "Secure MPC", "2026-10-25T00:00:00Z")], 5)),
                         Response(text=atom([("2610.2", "Secure MPC", "2026-09-01T00:00:00Z")], 5))])
        result = list(collect_arxiv(cfg, client, NOW.date(), date(2026, 10, 1)))
        self.assertEqual(len(result), 1)
        self.assertEqual([call[1]["start"] for call in client.calls], [0, 1])

    def test_eprint_empty_error_and_resumption_token(self):
        self.assertEqual(parse_eprint(oai(error="noRecordsMatch")), ([], ""))
        with self.assertRaises(SourceError):
            parse_eprint(oai(error="badArgument"))
        cfg = load_config(ROOT / "config.yaml")
        client = Client([Response(text=oai("opaque-token")), Response(text=oai())])
        results = list(collect_eprint(cfg, client, NOW.date(), date(2026, 10, 1)))
        self.assertEqual(len(results), 2)
        self.assertEqual(client.calls[1][1], {"verb": "ListRecords", "resumptionToken": "opaque-token"})
        self.assertEqual(results[0]["records"][0]["published"], "2026-10-24T00:00:00Z")

    def test_dblp_pagination_and_venue_filter(self):
        cfg = load_config(ROOT / "config.yaml")
        cfg["sources"]["dblp"]["backend"] = "search"
        cfg["tracking"].update(start_year=2026, years_ahead=0)
        cfg["topics"] = {"MPC": {"dblp_terms": ["secure comput"]}}
        def data(key):
            return {"result": {"hits": {"@total": "2", "hit": [{"info": {"key": key, "title": "Secure computation", "year": "2026",
                       "authors": {"author": [{"text": "Alice"}]}, "ee": ["https://example.org/x"]}}]}}}
        client = Client([Response(data("conf/crypto/A26")), Response(data("conf/unrelated/B26"))])
        result = list(collect_dblp(cfg, client, NOW.date()))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["records"][0]["venue"], "CRYPTO")
        self.assertEqual([call[1]["f"] for call in client.calls], [0, 1])

    def test_html_challenge_is_not_a_feed(self):
        with self.assertRaises(SourceError):
            parse_eprint("<html><body>Not a bot?</body></html>")

    def test_sparql_authors_do_not_change_pagination_unit(self):
        cfg = load_config(ROOT / "config.yaml")
        cfg["sources"]["dblp"]["sparql_page_size"] = 1
        base = {key: {"value": value} for key, value in {"paper": "https://dblp.org/rec/conf/crypto/A26", "title": "Secure computation",
                  "year": "2026", "stream": "https://dblp.org/streams/conf/crypto", "doi": "https://doi.org/10.1234/test"}.items()}
        rows = [{**base, "author": {"value": name}} for name in ("Alice", "Bob")]
        client = Client([Response({"results": {"bindings": rows}}), Response({"results": {"bindings": []}})])
        papers = list(collect_dblp(cfg, client, NOW.date()))
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0]["authors"], ["Alice", "Bob"])
        self.assertIn("OFFSET 1", client.calls[1][1]["query"])
        self.assertIn('"2020"^^xsd:gYear', client.calls[0][1]["query"])

    def test_sparql_query_contains_both_independent_topics(self):
        cfg = load_config(ROOT / "config.yaml")
        query = sparql_query(cfg, NOW.date(), 0)
        self.assertIn("multiparty", query)
        self.assertIn("SGX", query)
        self.assertIn("streams/conf/crypto", query)
        self.assertNotIn("federate", query)

    def test_start_year_remains_2020_in_future_runs(self):
        cfg = load_config(ROOT / "config.yaml")
        self.assertEqual(year_bounds(cfg, date(2030, 1, 1)), (2020, 2031))
        self.assertIn('"2020"^^xsd:gYear', sparql_query(cfg, date(2030, 1, 1), 0))

    def test_arxiv_history_partitions_submission_years(self):
        cfg = load_config(ROOT / "config.yaml")
        cfg["topics"] = {"MPC": {"arxiv_terms": ['"secure computation"']}}
        client = Client([Response(text=atom([])) for _ in range(7)])
        self.assertEqual(list(collect_arxiv(cfg, client, NOW.date(), date(2020, 1, 1))), [])
        self.assertEqual(len(client.calls), 7)
        self.assertIn("submittedDate:[202001010000 TO 202012312359]", client.calls[0][1]["search_query"])
        self.assertIn("submittedDate:[202601010000 TO 202610292359]", client.calls[-1][1]["search_query"])


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix=".local-test-", dir=ROOT)
        self.root = Path(self.temp.name)
        self.cfg = load_config(ROOT / "config.yaml")
        self.cfg["enrichment"] = {}

    def tearDown(self):
        if not Path(self.temp.name).resolve().is_relative_to(ROOT.resolve()):
            raise RuntimeError("Test cleanup escaped the repository")
        self.temp.cleanup()

    def call(self, collectors, now=NOW, **kwargs):
        return run(self.root, self.cfg, now=now, collectors=collectors,
                   client_factory=lambda *args: None, no_enrich=True, **kwargs)

    def test_baseline_then_new_tee_without_new_mpc(self):
        collectors = {"dblp": lambda *args: [], "eprint": lambda *args: [], "arxiv": lambda *args: [paper()]}
        self.call(collectors)
        self.assertEqual(read_json(self.root / "data/state.json", {})["pending"], [])
        collectors["arxiv"] = lambda *args: [paper(), paper("TEE security with Intel SGX", identifier="2610.2")]
        result = self.call(collectors, now=NOW + timedelta(days=1))
        self.assertEqual(result["pending"], 1)
        self.assertEqual(result["total_papers"], 2)

    def test_failed_source_rolls_back_but_other_sources_finish(self):
        def broken(*args):
            yield paper(source="dblp", identifier="conf/crypto/A26")
            raise SourceError("second page failed")
        result = self.call({"dblp": broken, "arxiv": lambda *args: [paper("Intel SGX security", identifier="2610.2")], "eprint": lambda *args: []})
        self.assertEqual(result["failed_sources"], ["dblp"])
        self.assertEqual(result["total_papers"], 1)
        state = read_json(self.root / "data/state.json", {})
        self.assertNotIn("last_success", state["sources"]["dblp"])
        self.assertIn("last_success", state["sources"]["arxiv"])

    def test_dry_run_does_not_change_files(self):
        self.call({name: lambda *args: [paper()] for name in ("dblp", "arxiv", "eprint")}, dry_run=True)
        self.assertFalse((self.root / "data").exists())

    def test_repeated_same_day_uses_cache(self):
        self.call({name: lambda *args: [] for name in ("dblp", "arxiv", "eprint")})
        def never(*args):
            raise AssertionError("Collector must not run twice today")
        result = self.call({name: never for name in ("dblp", "arxiv", "eprint")})
        self.assertTrue(all(status["status"] == "cached" for status in result["sources"].values()))

    def test_initial_scan_starts_at_2020_for_all_sources(self):
        windows = []
        def collector(config, client, upper, lower):
            windows.append((lower, upper))
            return []
        self.call({name: collector for name in ("dblp", "arxiv", "eprint")})
        self.assertEqual(windows, [(date(2020, 1, 1), NOW.date())] * 3)

    def test_explicit_backfill_is_quiet_and_does_not_refresh_eprint_daily_window(self):
        self.call({name: lambda *args: [] for name in ("dblp", "arxiv", "eprint")})
        state_path = self.root / "data/state.json"
        state = read_json(state_path, {})
        state["sources"]["eprint"]["coverage_start"] = "2026-09-28"
        write_json(state_path, state)
        windows = []
        def historical(config, client, upper, lower):
            windows.append((lower, upper))
            return [paper("A 2020 secure computation protocol", source="eprint", identifier="2020/1234")]
        result = self.call({"eprint": historical}, selected=["eprint"], since=date(2020, 1, 1))
        self.assertEqual(result["pending"], 0)
        self.assertEqual(result["total_papers"], 1)
        self.assertEqual(windows, [(date(2020, 1, 1), date(2026, 10, 25))])
        again = self.call({"eprint": historical}, selected=["eprint"], since=date(2020, 1, 1))
        self.assertEqual(again["sources"]["eprint"]["status"], "cached")
        self.assertEqual(len(windows), 1)

    def test_pre_2020_preprints_are_filtered_even_when_recently_revised(self):
        old = paper("Secret sharing before 2020", identifier="1901.1")
        old["records"][0]["year"] = "2019"
        boundary = paper("Secure computation from 2020", identifier="2001.1")
        boundary["records"][0]["year"] = "2020"
        result = self.call({"arxiv": lambda *args: [old, boundary]}, selected=["arxiv"])
        self.assertEqual(result["total_papers"], 1)

    def test_unknown_venue_still_renders(self):
        p = paper(source="dblp")
        p["records"][0]["venue"] = "New conference"
        self.assertIn("New conference", render_library({"p": p}, {}))

    def test_notification_retry_recovers_sent_ids(self):
        p = paper()
        write_json(self.root / "data/papers.json", {"papers": {"abc123": p}})
        write_json(self.root / "data/state.json", {"pending": ["abc123"]})
        class Session:
            def get(self, *args, **kwargs):
                return Response([{"body": "<!-- mpc-tee-papers:abc123 -->"}])
            def post(self, *args, **kwargs):
                raise AssertionError("Must not publish twice")
        with patch.dict(os.environ, {"GITHUB_REPOSITORY": self.cfg["project"]["repository"]}):
            self.assertEqual(publish(self.root, self.cfg, Session()), 0)
        self.assertEqual(read_json(self.root / "data/state.json", {})["pending"], [])

    def test_notification_cannot_target_another_repository(self):
        with patch.dict(os.environ, {"GITHUB_REPOSITORY": "youngfish42/FL-paper-update-tracker"}):
            with self.assertRaises(RuntimeError):
                publish(self.root, self.cfg, None)


if __name__ == "__main__":
    unittest.main()
