#!/usr/bin/env python3
"""Chain-of-Title Compass quickstart: read a track's Rights Passport.

Free lane, no credentials. Stdlib only.
Usage: python3 passport_check.py ["Track Title"]   (default: "Zooted Zone")
Prints DOCUMENTED fields verbatim with sources; names PENDING fields with
what's missing and who provides them. Never invents a value.
Exit 0 on success; 1 if the passport file can't be read or the track is absent.
"""
import json
import sys
import urllib.request

PASSPORTS_URL = "https://cumulativewebinc.github.io/cwi-learn/compass/passports.json"


def fetch(url, retries=2):
    """Fetch JSON. curl-first: this VM's Fastly path truncates Python-urllib
    bodies (IncompleteRead) while curl receives full bodies with
    Accept-Encoding: identity. urllib is the fallback."""
    import subprocess, shutil
    if shutil.which("curl"):
        last = None
        for _ in range(retries + 1):
            try:
                p = subprocess.run(
                    ["curl", "-sS", "--fail", "--max-time", "30",
                     "-H", "Accept-Encoding: identity",
                     "-A", "clawhub-skill/1.0.0", url],
                    capture_output=True, text=True, timeout=40)
                if p.returncode == 0:
                    return json.loads(p.stdout)
                last = RuntimeError(p.stderr.strip() or f"curl rc={p.returncode}")
            except Exception as e:
                last = e
        raise last
    last = None
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={"Accept-Encoding": "identity",
                         "User-Agent": "clawhub-skill/1.0.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:
            last = e
    raise last

def main():
    title = sys.argv[1] if len(sys.argv) > 1 else "Zooted Zone"
    try:
        doc = fetch(PASSPORTS_URL)
    except Exception as e:
        print(f"PASSPORT FAIL: could not fetch passports.json ({e})", file=sys.stderr)
        print("Do not answer rights questions from memory.", file=sys.stderr)
        return 1
    if doc.get("format") != "cwi-compass/v1":
        print("PASSPORT FAIL: unexpected format — stop.", file=sys.stderr)
        return 1
    pp = next(
        (p for p in doc.get("passports", []) if p.get("title", "").lower() == title.lower()),
        None,
    )
    if pp is None:
        print(f"PASSPORT FAIL: no passport for '{title}' in this file.", file=sys.stderr)
        return 1
    fields = pp.get("fields", {})
    print(f"PASSPORT OK: {pp['title']} ({doc.get('compass')})")
    print("DOCUMENTED:")
    for k, f in fields.items():
        if f.get("status") == "DOCUMENTED":
            print(f"  {k}: {f.get('value')}  [source: {f.get('source')}]")
    print("PENDING (refuse to assert; say what's missing):")
    for k, f in fields.items():
        if f.get("status") == "PENDING":
            print(f"  {k}: {f.get('whats_missing')} — provided by {f.get('provided_by')}")
    print("ADVISORY TOOLING ONLY: not legal advice; no field substitutes for clearance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
