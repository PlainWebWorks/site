from __future__ import annotations

import argparse
import json
import socket
import ssl
import sys
import time
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

import requests
import yaml
from bs4 import BeautifulSoup


DEFAULT_TIMEOUT_SECONDS = 12
CERT_EXPIRY_WARNING_DAYS = 30


@dataclass
class CheckResult:
  ok: bool
  value: Any = None
  note: str | None = None

  def to_json(self) -> dict[str, Any]:
    result: dict[str, Any] = {"ok": self.ok}
    if self.value is not None:
      result["value"] = self.value
    if self.note:
      result["note"] = self.note
    return result


def load_clients(path: Path) -> list[dict[str, Any]]:
  with path.open("r", encoding="utf-8") as handle:
    data = yaml.safe_load(handle) or {}

  clients = data.get("clients")
  if not isinstance(clients, list):
    raise ValueError(f"{path} must contain a top-level 'clients' list")

  return clients


def fetch_url(session: requests.Session, url: str, timeout: int) -> tuple[requests.Response | None, float | None, str | None]:
  started = time.perf_counter()
  try:
    response = session.get(url, timeout=timeout, allow_redirects=True)
  except requests.RequestException as exc:
    return None, None, str(exc)

  elapsed_ms = round((time.perf_counter() - started) * 1000, 2)
  return response, elapsed_ms, None


def check_dns(domain: str) -> CheckResult:
  try:
    addresses = sorted({info[4][0] for info in socket.getaddrinfo(domain, 443, type=socket.SOCK_STREAM)})
  except socket.gaierror as exc:
    return CheckResult(False, note=f"DNS lookup failed: {exc}")

  return CheckResult(bool(addresses), addresses)


def check_https_certificate(domain: str) -> CheckResult:
  context = ssl.create_default_context()
  try:
    with socket.create_connection((domain, 443), timeout=DEFAULT_TIMEOUT_SECONDS) as sock:
      with context.wrap_socket(sock, server_hostname=domain) as tls:
        cert = tls.getpeercert()
  except (OSError, ssl.SSLError) as exc:
    return CheckResult(False, note=f"TLS certificate check failed: {exc}")

  not_after = cert.get("notAfter")
  if not not_after:
    return CheckResult(False, note="TLS certificate did not include an expiration date")

  expires_at = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
  days_remaining = (expires_at - datetime.now(timezone.utc)).days
  ok = days_remaining >= CERT_EXPIRY_WARNING_DAYS
  return CheckResult(ok, {"expires_at": expires_at.isoformat(), "days_remaining": days_remaining})


def check_http_to_https(session: requests.Session, domain: str, canonical_url: str, timeout: int) -> CheckResult:
  http_url = f"http://{domain}"
  response, _, error = fetch_url(session, http_url, timeout)
  if error or response is None:
    return CheckResult(False, note=f"HTTP redirect check failed: {error}")

  final_url = response.url.rstrip("/")
  expected = canonical_url.rstrip("/")
  ok = final_url == expected or final_url.startswith("https://")
  return CheckResult(ok, {"from": http_url, "to": response.url, "status": response.status_code})


def check_page_metadata(soup: BeautifulSoup) -> dict[str, CheckResult]:
  title = soup.find("title")
  description = soup.find("meta", attrs={"name": "description"})
  og_title = soup.find("meta", attrs={"property": "og:title"})
  og_description = soup.find("meta", attrs={"property": "og:description"})
  json_ld = soup.find("script", attrs={"type": "application/ld+json"})

  return {
    "title": CheckResult(bool(title and title.get_text(strip=True)), title.get_text(strip=True) if title else None),
    "meta_description": CheckResult(bool(description and description.get("content")), description.get("content") if description else None),
    "og_title": CheckResult(bool(og_title and og_title.get("content")), og_title.get("content") if og_title else None),
    "og_description": CheckResult(bool(og_description and og_description.get("content")), og_description.get("content") if og_description else None),
    "json_ld": CheckResult(bool(json_ld)),
  }


def check_indexing(soup: BeautifulSoup, robots_text: str | None, launched: bool) -> dict[str, CheckResult]:
  robots_meta = soup.find("meta", attrs={"name": "robots"})
  robots_content = (robots_meta.get("content", "") if robots_meta else "").lower()
  found_noindex = "noindex" in robots_content
  found_nofollow = "nofollow" in robots_content
  robots_blocks_all = False

  if robots_text:
    normalized = [line.strip().lower().replace(" ", "") for line in robots_text.splitlines()]
    robots_blocks_all = "user-agent:*" in normalized and "disallow:/" in normalized

  return {
    "noindex": CheckResult(not (launched and found_noindex), found_noindex, "noindex is acceptable before launch" if found_noindex and not launched else None),
    "nofollow": CheckResult(not (launched and found_nofollow), found_nofollow, "nofollow is acceptable before launch" if found_nofollow and not launched else None),
    "robots_blocks_all": CheckResult(not (launched and robots_blocks_all), robots_blocks_all, "robots.txt blocks all crawling before launch" if robots_blocks_all and not launched else None),
  }


def normalize_phone(text: str) -> str:
  return "".join(char for char in text if char.isdigit())


def check_contact_path(client: dict[str, Any], soup: BeautifulSoup, page_text: str) -> CheckResult:
  hrefs = [tag.get("href", "") for tag in soup.find_all("a")]
  expected_emails = client.get("expected_email") or []
  expected_phones = client.get("expected_phone") or []

  email_ok = not expected_emails or any(
    email.lower() in page_text.lower() or f"mailto:{email.lower()}" in [href.lower() for href in hrefs]
    for email in expected_emails
  )
  phone_digits = normalize_phone(page_text + " " + " ".join(hrefs))
  phone_ok = not expected_phones or any(normalize_phone(phone) in phone_digits for phone in expected_phones)

  return CheckResult(email_ok and phone_ok, {"email": email_ok, "phone": phone_ok})


def check_required_text(required_text: list[str], page_text: str) -> CheckResult:
  missing = [text for text in required_text if text.lower() not in page_text.lower()]
  return CheckResult(not missing, {"missing": missing, "checked": len(required_text)})


def check_required_links(required_links: list[str], soup: BeautifulSoup) -> CheckResult:
  hrefs = [tag.get("href", "") for tag in soup.find_all("a")]
  missing = [link for link in required_links if not any(link in href for href in hrefs)]
  return CheckResult(not missing, {"missing": missing, "checked": len(required_links)})


def check_paths(session: requests.Session, canonical_url: str, paths: list[str], timeout: int) -> CheckResult:
  results = []
  ok = True
  for path in paths:
    url = urljoin(canonical_url.rstrip("/") + "/", path.lstrip("/"))
    response, elapsed_ms, error = fetch_url(session, url, timeout)
    if error or response is None:
      ok = False
      results.append({"path": path, "ok": False, "error": error})
      continue

    path_ok = 200 <= response.status_code < 400
    ok = ok and path_ok
    results.append({"path": path, "ok": path_ok, "status": response.status_code, "response_time_ms": elapsed_ms})

  return CheckResult(ok, results)


def check_internal_links(session: requests.Session, canonical_url: str, soup: BeautifulSoup, timeout: int) -> CheckResult:
  canonical = urlparse(canonical_url)
  seen: set[str] = set()
  results = []
  ok = True

  for tag in soup.find_all("a"):
    href = tag.get("href")
    if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
      continue

    url = urljoin(canonical_url, href)
    parsed = urlparse(url)
    if parsed.netloc and parsed.netloc != canonical.netloc:
      continue
    if url in seen:
      continue
    seen.add(url)

    response, _, error = fetch_url(session, url, timeout)
    if error or response is None:
      ok = False
      results.append({"url": url, "ok": False, "error": error})
      continue

    link_ok = 200 <= response.status_code < 400
    ok = ok and link_ok
    if not link_ok:
      results.append({"url": url, "ok": False, "status": response.status_code})

  return CheckResult(ok, {"checked": len(seen), "problems": results})


def fetch_robots(session: requests.Session, canonical_url: str, timeout: int) -> str | None:
  robots_url = urljoin(canonical_url.rstrip("/") + "/", "robots.txt")
  response, _, error = fetch_url(session, robots_url, timeout)
  if error or response is None or response.status_code >= 400:
    return None
  return response.text


def check_client(client: dict[str, Any], timeout: int) -> dict[str, Any]:
  name = client["name"]
  domain = client["domain"]
  canonical_url = client["canonical_url"]
  launched = bool(client.get("launched", True))
  session = requests.Session()
  session.headers.update({"User-Agent": "PlainWebWorksHealthcheck/0.1"})

  checks: dict[str, CheckResult] = {
    "dns": check_dns(domain),
    "https_certificate": check_https_certificate(domain),
    "http_to_https": check_http_to_https(session, domain, canonical_url, timeout),
  }

  response, elapsed_ms, error = fetch_url(session, canonical_url, timeout)
  if error or response is None:
    checks["http_status"] = CheckResult(False, note=error)
    checks["response_time_ms"] = CheckResult(False)
    return build_client_result(client, checks)

  checks["http_status"] = CheckResult(response.status_code == 200, response.status_code)
  checks["response_time_ms"] = CheckResult(elapsed_ms is not None and elapsed_ms < 3000, elapsed_ms)

  soup = BeautifulSoup(response.text, "html.parser")
  page_text = soup.get_text(" ", strip=True)
  robots_text = fetch_robots(session, canonical_url, timeout)

  checks.update(check_page_metadata(soup))
  checks.update(check_indexing(soup, robots_text, launched))
  checks["contact_path"] = check_contact_path(client, soup, page_text)
  checks["required_text"] = check_required_text(client.get("required_text") or [], page_text)
  checks["required_links"] = check_required_links(client.get("required_links") or [], soup)
  checks["configured_paths"] = check_paths(session, canonical_url, client.get("check_paths") or ["/"], timeout)
  checks["internal_links"] = check_internal_links(session, canonical_url, soup, timeout)

  return build_client_result(client, checks)


def build_client_result(client: dict[str, Any], checks: dict[str, CheckResult]) -> dict[str, Any]:
  failed = [name for name, result in checks.items() if not result.ok]
  notes = [f"{name}: {result.note}" for name, result in checks.items() if result.note]

  return {
    "date": date.today().isoformat(),
    "checked_at": datetime.now(timezone.utc).isoformat(),
    "client": client["name"],
    "domain": client["domain"],
    "canonical_url": client["canonical_url"],
    "launched": bool(client.get("launched", True)),
    "status": "healthy" if not failed else "warning",
    "checks": {name: result.to_json() for name, result in checks.items()},
    "failed_checks": failed,
    "notes": notes,
  }


def write_results(results: list[dict[str, Any]], output_dir: Path) -> Path:
  output_dir.mkdir(parents=True, exist_ok=True)
  path = output_dir / f"{date.today().isoformat()}.json"
  payload = {
    "date": date.today().isoformat(),
    "status": "healthy" if all(result["status"] == "healthy" for result in results) else "warning",
    "results": results,
  }
  path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
  return path


def print_summary(results: list[dict[str, Any]]) -> None:
  for result in results:
    failed = ", ".join(result["failed_checks"]) if result["failed_checks"] else "none"
    print(f"{result['client']}: {result['status']} (failed: {failed})")
    for note in result["notes"]:
      print(f"  note: {note}")


def parse_args(argv: list[str]) -> argparse.Namespace:
  parser = argparse.ArgumentParser(description="Run Plain Web Works public-surface health checks.")
  parser.add_argument("--clients", type=Path, default=Path("clients.yml"), help="Path to clients.yml")
  parser.add_argument("--output-dir", type=Path, default=Path("reports/daily"), help="Directory for daily JSON results")
  parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS, help="HTTP timeout in seconds")
  parser.add_argument("--no-write", action="store_true", help="Print summary without writing a report file")
  return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
  args = parse_args(argv or sys.argv[1:])
  clients = load_clients(args.clients)
  results = [check_client(client, args.timeout) for client in clients]
  print_summary(results)

  if not args.no_write:
    path = write_results(results, args.output_dir)
    print(f"Wrote {path}")

  return 0 if all(result["status"] == "healthy" for result in results) else 1


if __name__ == "__main__":
  raise SystemExit(main())
