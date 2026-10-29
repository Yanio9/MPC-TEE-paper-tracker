"""Independent, paginated collectors with conservative HTTP pacing."""
from __future__ import annotations

import logging
import json
import random
import re
import time
import xml.etree.ElementTree as ET
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime

import requests

from .core import canonical_arxiv, clean_text, year_bounds

LOG = logging.getLogger(__name__)
ATOM = {"a": "http://www.w3.org/2005/Atom", "open": "http://a9.com/-/spec/opensearch/1.1/", "arxiv": "http://arxiv.org/schemas/atom"}
OAI = {"o": "http://www.openarchives.org/OAI/2.0/", "dc": "http://purl.org/dc/elements/1.1/", "odc": "http://www.openarchives.org/OAI/2.0/oai_dc/"}


class SourceError(RuntimeError):
    pass


class HttpClient:
    def __init__(self, name: str, interval: float, contact: str = ""):
        self.name = name
        self.interval = max(interval, 6.0 if name == "dblp" else 3.1)
        self.session = requests.Session()
        user_agent = "MPC-TEE-paper-tracker/1.0 (+https://github.com/Yanio9/MPC-TEE-paper-tracker)"
        self.session.headers["User-Agent"] = user_agent + (f"; mailto:{contact}" if contact else "")
        if name == "dblp":
            self.session.headers["Accept"] = "application/sparql-results+json, application/json"
        self.last_call = 0.0

    def get(self, url: str, params: dict):
        for attempt in range(4):
            jitter = random.uniform(0.5, 2.5) if self.name == "dblp" else 0
            time.sleep(max(0, self.interval + jitter - (time.monotonic() - self.last_call)))
            self.last_call = time.monotonic()
            try:
                response = self.session.get(url, params=params, timeout=(10, 45))
                # A challenge page is a failure, never an empty collection. Do not solve/bypass it.
                if response.status_code == 202 or "text/html" in response.headers.get("Content-Type", "").lower():
                    raise SourceError(f"{self.name}: expected API data, received HTTP {response.status_code} HTML/challenge page")
                if response.status_code == 429 or response.status_code >= 500:
                    delay = min(120, 8 * 2 ** attempt) + random.uniform(0.5, 2.5)
                    retry_after = response.headers.get("Retry-After", "")
                    try:
                        delay = max(delay, float(retry_after))
                    except ValueError:
                        try:
                            delay = max(delay, (parsedate_to_datetime(retry_after) - datetime.now(timezone.utc)).total_seconds())
                        except (TypeError, ValueError, OverflowError):
                            pass
                    if delay > 300:
                        raise SourceError(f"{self.name}: Retry-After {delay:.0f}s; retry on the next run")
                    if attempt < 3:
                        LOG.warning("%s HTTP %s; retrying in %.1fs", self.name, response.status_code, delay)
                        time.sleep(delay)
                        continue
                response.raise_for_status()
                return response
            except requests.RequestException as error:
                if attempt == 3:
                    raise SourceError(f"{self.name}: {error}") from error
                time.sleep(min(120, 8 * 2 ** attempt) + random.random())
        raise SourceError(f"{self.name}: exhausted retries")


def _strings(value) -> list[str]:
    if not value:
        return []
    if not isinstance(value, list):
        value = [value]
    return [str(item.get("text", "") if isinstance(item, dict) else item) for item in value]


def parse_dblp(data: dict, venues: dict) -> tuple[list[dict], int, int]:
    hits = data["result"]["hits"]
    raw = hits.get("hit", [])
    if isinstance(raw, dict):
        raw = [raw]
    papers = []
    for item in raw:
        info = item["info"]
        key = info.get("key", "")
        stream = "/".join(key.split("/")[:2])
        if venues and stream not in venues:
            continue
        urls = _strings(info.get("ee"))
        record = {"source": "dblp", "id": key or info.get("url", ""), "doi": info.get("doi", ""),
                  "url": next((u for u in urls if u.startswith("https://doi.org/")), urls[0] if urls else info.get("url", "")),
                  "venue": venues.get(stream, clean_text(info.get("venue", "Unknown venue"))), "year": str(info.get("year", "")), "updated": ""}
        papers.append({"title": clean_text(info.get("title", "")), "authors": _strings(info.get("authors", {}).get("author")),
                       "abstract": "", "records": [record]})
    return papers, int(hits.get("@total", 0)), len(raw)


def collect_dblp(config: dict, client, today, since=None):
    cfg = config["sources"]["dblp"]
    if cfg.get("backend", "search") == "sparql":
        yield from collect_dblp_sparql(config, client, today)
        return
    if cfg.get("backend", "search") != "search":
        raise SourceError("Unknown DBLP backend")
    min_year, max_year = year_bounds(config, today)
    years = range(min_year, max_year + 1)
    terms = list(dict.fromkeys(term for topic in config["topics"].values() for term in topic["dblp_terms"]))
    size = min(1000, cfg["page_size"])
    for year in years:
        for term in terms:
            offset = 0
            query = f"{term} year:{year}:"
            LOG.info("DBLP query: %s", query)
            for _ in range(cfg["max_pages_per_query"]):
                response = client.get(cfg["url"], {"q": query, "format": "json", "h": size, "f": offset})
                papers, total, count = parse_dblp(response.json(), cfg.get("venues", {}))
                yield from papers
                offset += count
                if offset >= total:
                    break
                if not count:
                    raise SourceError(f"DBLP pagination stopped at {offset}/{total}: {query}")
            else:
                raise SourceError(f"DBLP page limit reached: {query}; increase max_pages_per_query")


def sparql_query(config: dict, today, offset: int) -> str:
    """Translate the configured AND/OR/prefix terms to a broad title candidate query."""
    cfg = config["sources"]["dblp"]
    streams = cfg.get("venues", {})
    if any(not re.fullmatch(r"(?:conf|journals)/[\w-]+", stream) for stream in streams):
        raise ValueError("Invalid DBLP stream key")
    values = "VALUES ?venue { " + " ".join(f"<https://dblp.org/streams/{stream}>" for stream in streams) + " }" if streams else ""
    terms = list(dict.fromkeys(term for topic in config["topics"].values() for term in topic["dblp_terms"]))
    expressions = []
    for term in terms:
        and_parts = []
        for part in term.split():
            alternatives = []
            for token in part.split("|"):
                exact = token.endswith("$")
                token = token.removesuffix("$")
                token = re.escape(token).replace(r"\-", "[^a-z0-9]?")
                alternatives.append("(^|[^a-z0-9])" + token + ("([^a-z0-9]|$)" if exact else ""))
            pattern = "|".join(alternatives)
            and_parts.append(f"REGEX(STR(?candidateTitle), {json.dumps(pattern)}, \"i\")")
        expressions.append("(" + " && ".join(and_parts) + ")")
    if not expressions:
        raise ValueError("DBLP requires at least one search term")
    min_year, max_year = year_bounds(config, today)
    size = int(cfg.get("sparql_page_size", 500))
    return f'''
PREFIX dblp: <https://dblp.org/rdf/schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
SELECT ?paper ?title ?year ?stream ?doi ?ee ?author WHERE {{
  {{ SELECT DISTINCT ?paper WHERE {{
      {values}
      ?paper dblp:publishedInStream ?venue ; dblp:title ?candidateTitle ; dblp:yearOfPublication ?candidateYear .
      FILTER (?candidateYear >= "{min_year}"^^xsd:gYear && ?candidateYear <= "{max_year}"^^xsd:gYear)
      FILTER ({" || ".join(expressions)})
    }} ORDER BY ?paper LIMIT {size} OFFSET {int(offset)}
  }}
  ?paper dblp:title ?title ; dblp:yearOfPublication ?year ; dblp:publishedInStream ?stream .
  OPTIONAL {{ ?paper dblp:doi ?doi }}
  OPTIONAL {{ ?paper dblp:primaryDocumentPage ?ee }}
  OPTIONAL {{ ?paper dblp:authoredBy ?person . ?person dblp:primaryCreatorName ?author }}
}} ORDER BY ?paper
'''


def parse_dblp_sparql(data: dict, venues: dict) -> list[dict]:
    rows = data["results"]["bindings"]
    grouped = {}
    for row in rows:
        value = lambda key: row.get(key, {}).get("value", "")
        url = value("paper")
        if not url.startswith("https://dblp.org/rec/") or not value("title"):
            raise SourceError("Incomplete DBLP SPARQL binding")
        key = url.removeprefix("https://dblp.org/rec/")
        stream = value("stream").removeprefix("https://dblp.org/streams/")
        if key not in grouped:
            grouped[key] = {"title": clean_text(value("title")), "abstract": "", "authors": [], "records": [{
                "source": "dblp", "id": key, "year": value("year"), "updated": "", "doi": value("doi"),
                "url": value("doi") or value("ee") or url, "venue": venues.get(stream, stream)}]}
        if value("author") and value("author") not in grouped[key]["authors"]:
            grouped[key]["authors"].append(clean_text(value("author")))
    return list(grouped.values())


def collect_dblp_sparql(config: dict, client, today):
    cfg = config["sources"]["dblp"]
    offset = 0
    size = cfg.get("sparql_page_size", 500)
    for _ in range(cfg["max_pages_per_query"]):
        LOG.info("DBLP official SPARQL page at offset %s", offset)
        data = client.get(cfg["sparql_url"], {"query": sparql_query(config, today, offset)}).json()
        papers = parse_dblp_sparql(data, cfg.get("venues", {}))
        yield from papers
        if len(papers) < size:
            return
        offset += len(papers)
    raise SourceError("DBLP SPARQL page limit reached; increase max_pages_per_query")


def parse_arxiv(xml: str) -> tuple[list[dict], int]:
    root = ET.fromstring(xml)
    if root.tag != "{" + ATOM["a"] + "}feed":
        raise SourceError("arXiv did not return an Atom feed")
    papers = []
    for entry in root.findall("a:entry", ATOM):
        url = entry.findtext("a:id", "", ATOM)
        if "/api/errors" in url:
            raise SourceError("arXiv API: " + entry.findtext("a:summary", "unknown error", ATOM))
        identifier = canonical_arxiv(url)
        updated = entry.findtext("a:updated", "", ATOM)
        published = entry.findtext("a:published", "", ATOM)
        record = {"source": "arxiv", "id": identifier, "url": "https://arxiv.org/abs/" + identifier,
                  "pdf_url": "https://arxiv.org/pdf/" + identifier, "published": published, "updated": updated,
                  "year": published[:4], "venue": "arXiv", "doi": entry.findtext("arxiv:doi", "", ATOM)}
        papers.append({"title": clean_text(entry.findtext("a:title", "", ATOM)),
                       "abstract": clean_text(entry.findtext("a:summary", "", ATOM)), "abstract_updated": updated,
                       "authors": [clean_text(a.findtext("a:name", "", ATOM)) for a in entry.findall("a:author", ATOM)],
                       "records": [record]})
    total_text = root.findtext("open:totalResults", None, ATOM)
    if total_text is None:
        raise SourceError("arXiv feed is missing totalResults")
    return papers, int(total_text)


def arxiv_queries(config: dict):
    batch_size = config["sources"]["arxiv"].get("query_batch_size", 6)
    for topic in config["topics"].values():
        terms = topic["arxiv_terms"]
        for index in range(0, len(terms), batch_size):
            # Title and abstract only; no author/category match masquerading as relevance.
            yield " OR ".join(f"(ti:{term} OR abs:{term})" for term in terms[index:index + batch_size])


def collect_arxiv(config: dict, client, today, since):
    cfg = config["sources"]["arxiv"]
    first_year, _ = year_bounds(config, today)
    historical = since.year < today.year
    # Annual submission windows keep historical queries below arXiv's result limits.
    windows = [(date(year, 1, 1), min(date(year, 12, 31), today)) for year in range(first_year, today.year + 1)] if historical else [(date(first_year, 1, 1), today)]
    page_size = cfg.get("backfill_page_size", cfg["page_size"]) if historical else cfg["page_size"]
    queries = [(f"({query}) AND submittedDate:[{start:%Y%m%d}0000 TO {end:%Y%m%d}2359]", start, end)
               for query in arxiv_queries(config) for start, end in windows]
    for query, start_date, end_date in queries:
        offset = 0
        for _ in range(cfg["max_pages_per_query"]):
            LOG.info("arXiv submissions %s to %s, offset %s", start_date, end_date, offset)
            response = client.get(cfg["url"], {"search_query": query, "start": offset, "max_results": page_size,
                                              "sortBy": "lastUpdatedDate", "sortOrder": "descending"})
            papers, total = parse_arxiv(response.text)
            # Sorting by update date also catches revisions and late discoverability.
            for paper in papers:
                updated = paper["records"][0]["updated"]
                if not updated:
                    raise SourceError("arXiv entry has no update timestamp")
                if updated[:10] >= since.isoformat():
                    yield paper
            offset += len(papers)
            if offset >= total or (papers and papers[-1]["records"][0]["updated"][:10] < since.isoformat()):
                break
            if not papers:
                raise SourceError(f"arXiv returned an empty page at {offset}/{total}")
        else:
            raise SourceError("arXiv page limit reached before the date boundary; increase max_pages_per_query")


def parse_eprint(xml: str) -> tuple[list[dict], str]:
    root = ET.fromstring(xml)
    if root.tag != "{" + OAI["o"] + "}OAI-PMH":
        raise SourceError("ePrint did not return OAI-PMH XML")
    error = root.find("o:error", OAI)
    if error is not None:
        if error.get("code") == "noRecordsMatch":
            return [], ""
        raise SourceError(f"ePrint OAI {error.get('code')}: {error.text}")
    records = root.find("o:ListRecords", OAI)
    if records is None:
        raise SourceError("ePrint response has no ListRecords")
    papers = []
    for entry in records.findall("o:record", OAI):
        header = entry.find("o:header", OAI)
        if header is None or header.get("status") == "deleted":
            continue
        identifier = header.findtext("o:identifier", "", OAI).rsplit(":", 1)[-1]
        if not re.fullmatch(r"\d{4}/\d+", identifier):
            raise SourceError("Unexpected ePrint identifier: " + identifier)
        metadata = entry.find("o:metadata/odc:dc", OAI)
        if metadata is None:
            raise SourceError("ePrint record missing Dublin Core metadata")
        updated = header.findtext("o:datestamp", "", OAI)
        dates = [item.text for item in metadata.findall("dc:date", OAI) if item.text]
        published = min(dates) if dates else ""
        record = {"source": "eprint", "id": identifier, "url": "https://eprint.iacr.org/" + identifier,
                  "pdf_url": "https://eprint.iacr.org/" + identifier + ".pdf", "published": published, "updated": updated,
                  "year": published[:4] or identifier[:4], "venue": "IACR ePrint"}
        papers.append({"title": clean_text(metadata.findtext("dc:title", "", OAI)),
                       "abstract": clean_text(metadata.findtext("dc:description", "", OAI)), "abstract_updated": updated,
                       "authors": [clean_text(item.text) for item in metadata.findall("dc:creator", OAI)], "records": [record]})
    return papers, (records.findtext("o:resumptionToken", "", OAI) or "").strip()


def collect_eprint(config: dict, client, today, since):
    cfg = config["sources"]["eprint"]
    params = {"verb": "ListRecords", "metadataPrefix": "oai_dc", "from": since.isoformat(), "until": today.isoformat()}
    seen_tokens = set()
    for page in range(cfg["max_pages"]):
        LOG.info("ePrint OAI interval %s to %s, page %s", since, today, page + 1)
        papers, token = parse_eprint(client.get(cfg["url"], params).text)
        yield from papers
        if not token:
            return
        if token in seen_tokens:
            raise SourceError("ePrint repeated its resumption token")
        seen_tokens.add(token)
        params = {"verb": "ListRecords", "resumptionToken": token}
    raise SourceError("ePrint page limit reached; increase max_pages")


COLLECTORS = {"dblp": collect_dblp, "arxiv": collect_arxiv, "eprint": collect_eprint}
