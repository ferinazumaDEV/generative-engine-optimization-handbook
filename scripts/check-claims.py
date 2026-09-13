#!/usr/bin/env python3
"""Check that the handbook's graded claims table, about.jsonld and the chapters agree.

    python3 scripts/check-claims.py

What is checked, and why it is exactly this and not more:

1. Every row of the graded table in CLAIMS.md carries a grade from the vocabulary
   (`established` / `mixed` / `experimental` / `folklore`), at least one primary source
   that is a URL, a DOI, or a cross-reference to other rows, and a non-empty limitation.
   A row with a grade and no source is an opinion in a table.
2. Every "Reproducible: yes — Cookbook `<recipe>`" names a recipe that exists in the
   Cookbook (the six recipe directories, listed below).
3. The work-level maturity CLAIMS.md states (`maturity`, `reproducible`) is what
   about.jsonld declares in `additionalProperty`. CLAIMS.md says about.jsonld wins when
   they disagree; this makes a disagreement fail instead of silently resolving.
4. The `needs verification` markers are counted per chapter and listed, so the number the
   README implies is visible on every run. This is a report, not an assertion.

This is what CI can check about "every claim carries a source". It does not read every
sentence of every chapter; the README says so.

No network, no dependencies.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))

GRADES = ("established", "mixed", "experimental", "folklore")

# The Cookbook's recipe directories (generative-engine-optimization-cookbook, one per chapter
# callout). Kept here because CI has no network; update when a recipe is added there.
COOKBOOK_RECIPES = {
    "chunk-friendly-structure",
    "ai-crawler-access",
    "ssr-vs-csr-rendering",
    "structured-data-jsonld",
    "entity-clarity-sameas",
    "citation-anchoring",
}

SOURCE_OK = re.compile(r"https?://\S+|doi:10\.\d{4,9}/|\bRows?\s+\d+", re.I)
RECIPE = re.compile(r"Cookbook\s+`([a-z0-9-]+)`")
GRADE = re.compile(r"`(" + "|".join(GRADES) + r")`")
MATURITY_LINE = re.compile(r"`maturity:\s*([a-z]+)`,\s*`reproducible:\s*([a-z]+)`")


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def table_rows(md):
    """Rows of the graded table: the first table after the 'Claims the handbook rests on' heading."""
    section = md.split("## Claims the handbook rests on", 1)
    if len(section) < 2:
        return None
    rows = []
    for line in section[1].split("\n## ", 1)[0].splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or not cells[0].isdigit():
            continue  # header, separator
        rows.append(cells)
    return rows


def main():
    problems = []
    claims = read("CLAIMS.md")

    rows = table_rows(claims)
    if rows is None:
        problems.append("CLAIMS.md: the 'Claims the handbook rests on' section is missing")
        rows = []
    if not rows:
        problems.append("CLAIMS.md: the graded table has no rows")

    reproducible_rows = 0
    for cells in rows:
        n = cells[0]
        if len(cells) < 6:
            problems.append(f"row {n}: expected 6 cells (#, claim, grade, reproducible, primary source, limitation), got {len(cells)}")
            continue
        _, claim, grade, repro, source, limitation = cells[:6]
        if not GRADE.search(grade):
            problems.append(f"row {n}: grade {grade!r} carries none of {GRADES}")
        if not SOURCE_OK.search(source):
            problems.append(f"row {n}: primary source has no URL, DOI or row cross-reference: {source[:80]!r}")
        if not limitation.strip():
            problems.append(f"row {n}: the limitation cell is empty")
        if repro.lower().startswith("yes"):
            reproducible_rows += 1
            m = RECIPE.search(repro)
            if not m:
                problems.append(f"row {n}: 'reproducible: yes' names no Cookbook recipe")
            elif m.group(1) not in COOKBOOK_RECIPES:
                problems.append(f"row {n}: Cookbook recipe {m.group(1)!r} does not exist (known: {sorted(COOKBOOK_RECIPES)})")
        elif not repro.lower().startswith("no"):
            problems.append(f"row {n}: reproducible must start with 'yes' or 'no', got {repro!r}")

    m = MATURITY_LINE.search(claims)
    if not m:
        problems.append("CLAIMS.md: no '`maturity: …`, `reproducible: …`' line in the work-level section")
    else:
        stated = {"maturity": m.group(1), "reproducible": m.group(2)}
        about = json.loads(read("about.jsonld"))
        declared = {}
        def walk(node):
            if isinstance(node, dict):
                if node.get("@type") == "PropertyValue" and node.get("name") in stated:
                    declared[node["name"]] = str(node.get("value"))
                for v in node.values():
                    walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)
        walk(about)
        for key, want in stated.items():
            got = declared.get(key)
            if got != want:
                problems.append(f"about.jsonld says {key}={got!r}, CLAIMS.md says {want!r}")

    counts = {}
    docs = os.path.join(ROOT, "docs")
    for name in sorted(os.listdir(docs)):
        if name.endswith(".md"):
            text = open(os.path.join(docs, name), encoding="utf-8").read()
            counts[name] = len(re.findall(r"needs verification", text, re.I))
    total = sum(counts.values())

    if problems:
        sys.stderr.write(f"\nClaims check FAILED -- {len(problems)} problem(s):\n")
        for p in problems:
            sys.stderr.write(f"  - {p}\n")
        return 1
    print(f"claims OK: {len(rows)} graded rows, {reproducible_rows} reproducible via the Cookbook, "
          f"about.jsonld agrees with CLAIMS.md")
    print(f"needs-verification markers: {total} — " + ", ".join(f"{k[:-3]}={v}" for k, v in counts.items() if v))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
