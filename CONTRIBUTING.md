# Contributing to The GEO Handbook

Thank you for helping keep this the most accurate, useful, and current reference on **Generative Engine Optimization**. This is a living document; it is only as good as its contributors keep it.

This project is documentation-only and is licensed under **[CC BY‑SA 4.0](LICENSE)**. By contributing, you agree that your contribution is licensed under the same terms and that you have the right to submit it.

---

## The one rule that matters most

> **Every factual claim must be backed by a real, linkable source — or explicitly marked `> ⚠️ needs verification`.**

We would rather ship an honest gap than a confident fabrication. **Never invent facts, statistics, or citations.** If you *think* something is true but can't source it, write it and flag it; someone will verify it in review. A handbook about getting *cited* by AI has to hold itself to a citation standard.

---

## What good looks like

Content here should be:

1. **Accurate & current (2026).** GEO moves fast. Prefer primary sources (papers, official engine/vendor docs, changelogs) over blog summaries. Date-stamp claims that are time-sensitive.
2. **Cited.** Link the source inline or in a footnote. Peer-reviewed research and official documentation beat opinion posts. If you cite a vendor, say so (vendors have incentives).
3. **Neutral.** Describe techniques and evidence, not hype. Distinguish *demonstrated* (studied/measured) from *plausible* (reasoned) from *anecdotal* (one person's result). No growth-hacking snake oil.
4. **Extractable.** Write the way we tell readers to write for GEO: clear headings, one idea per section, short self-contained paragraphs, quotable stats, tables and lists where they help. A generative engine (and a hurried human) should be able to lift a correct answer from a single chunk.
5. **Beginner-safe and pro-useful.** Define jargon on first use (or link the [glossary](docs/09-glossary.md)). Then go deep enough that an expert learns something.

---

## How the handbook is organized

- **`README.md`** — the hub: definition, table of contents, meta.
- **`docs/01`–`docs/09`** — the numbered chapters. Keep content in the chapter it belongs to; link across chapters instead of duplicating. If a topic doesn't fit, open an issue to discuss a new chapter before adding one.
- **`docs/09-glossary.md`** — one home for every term. Define once here; link everywhere else.
- **`updates/`** — one dated file per ISO week (see [`updates/README.md`](updates/README.md)).
- **`CHANGELOG.md`** — human-readable summary of notable repo changes ([Keep a Changelog](https://keepachangelog.com/en/1.1.0/)).

**One fact, one home.** Don't restate the same claim in three chapters — put it in the most relevant one and cross-link. This keeps the handbook consistent as it grows.

---

## PR process

1. **Open an issue first for anything non-trivial.** Typos and dead links can go straight to a PR; new sections, restructures, or claims that reshape guidance should start as an issue so we can align. New techniques have a [dedicated template](.github/ISSUE_TEMPLATE/new-technique.md).
2. **Fork & branch.** Use a descriptive branch name (`add/perplexity-citation-study`, `fix/robots-ai-useragents`).
3. **Write the change.** Follow the style guide above. Add your sources as links.
4. **Self-check** against the [PR checklist](.github/PULL_REQUEST_TEMPLATE.md): sources present? claims dated? neutral tone? links valid? glossary updated if you introduced a term?
5. **Open the PR.** Fill in the template, including your sources. Explain *why* the change is correct, not just *what* it is.
6. **Review.** A maintainer checks sources and tone. Expect requests to add citations or soften unsupported claims — that's the process working, not criticism.
7. **Merge & log.** Merged changes are summarized in the current week's `updates/` file and, if notable, in `CHANGELOG.md`.

## Style guide (quick reference)

- **Headings:** sentence case, hierarchical (`##` → `###`), each section self-contained.
- **Links:** descriptive text, not "click here". Prefer stable/canonical URLs. Archive links for volatile pages are welcome.
- **Claims:** `Statement.[^source]` or inline `([Source](url))`. Time-sensitive facts: `As of 2026‑08, …`.
- **Uncertainty:** `> ⚠️ needs verification` blockquote. Better an honest flag than a wrong assertion.
- **Voice:** second person, active, plain English. Define acronyms on first use.
- **Tables/lists** for anything comparative or enumerable — they are more extractable than prose.

## Weekly review cadence

Once per ISO week a maintainer does a light pass:

- Skim recent engine/vendor changelogs and new research; capture material shifts in `updates/YYYY-Www.md`.
- Triage open issues/PRs; merge what's ready and cited.
- Re-check any claim marked `needs verification` that's aged more than a couple weeks.
- Note dead links and outdated numbers.

You don't have to wait for the weekly pass to contribute — open PRs any time. The cadence just guarantees the handbook never silently drifts out of date.

## Code of conduct

Be kind, be rigorous, assume good faith, argue about evidence not people. Harassment or bad-faith contribution isn't welcome. Disagreements are settled by *sources*, not volume.

---

*Questions about contributing? Open an issue with the `question` label.*
