# Changelog

All notable changes to **The GEO Handbook** are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project aims to follow it. Because this is a documentation project rather than software, "versions" are content milestones, not code releases. Week-by-week detail lives in [`updates/`](updates/README.md); this file captures the notable milestones.

## [Unreleased]

### Added

- **[`CLAIMS.md`](CLAIMS.md)** — the maturity vocabulary (`established` / `mixed` / `experimental` / `folklore`, plus `reproducible`; `solid` == `established` as in the sibling ledger), the mapping from the markers the chapters already use, and a graded table of the twelve claims the handbook rests on.
- **GEO ID Card** in the README, mirrored field by field from `about.jsonld`, which now also carries `abstract`, `citation`, `version`, `datePublished` and `dateModified`.
- **[`ECOSYSTEM.md`](ECOSYSTEM.md)** — the canonical sibling list shared by the three GEO repositories; the README footer is a copy between `ecosystem:start` / `ecosystem:end` markers.
- `updates/2026-W35.md` — the missing first week (initial `v0.1.0` release), so the weekly record is continuous.

### Changed

- **Sourcing wording**: the README, `llms.txt` and `CITATION.cff` no longer say "primary-sourced" / "every claim carries a primary source"; they now state the handbook's actual rule — a source or an explicit needs-verification flag, primary preferred, secondary labelled.
- **Citation corrections**: removed a quotation attributed to Microsoft that appears in none of the cited sources (`02`); replaced the unsupported "3–6 million requests per day" with Cloudflare's own wording and post (`04`); fixed the Dodge et al. 2021 paper title (`05`, `07`, `09`); pointed the Bingbot "official doc" at Microsoft's own crawler page (`09`, `02`); corrected five citation dates (`06`, `09`); relabelled the Similarweb figure as secondary coverage (`07`).
- **Limitations next to figures**: "up to 40%" now carries its ceiling caveat in the same sentence (README, `03`, `09`); the `03` TL;DR recency range matches its own table; three vendor / agency figures in `updates/2026-W36.md` are flagged as such.
- `llms.txt`: absolute URLs, an Identity block (author, license, version, date, DOI, canonical URL) and links to `CLAIMS.md` and `CITATION.cff`.
- Author credited by full name (Fernando Aporta Franco) in the README author line and attribution string; six glossary cross-reference labels now match their targets.

- **DOI.** `v0.1.1` is archived on Zenodo, so the handbook is citable by a persistent
  identifier instead of a repository URL. The concept DOI
  [`10.5281/zenodo.22299644`](https://doi.org/10.5281/zenodo.22299644) always resolves to the latest release. Recorded in the
  README badge and citation, `CITATION.cff`, `about.jsonld` and `llms.txt`.

## [0.1.1] — 2026-09-04

### Added

- **First weekly landscape entry: [`updates/2026-W36.md`](updates/2026-W36.md)** — the busy late-August 2026 GEO week: Google's embeddable **Preferred Sources** button + **AI Mode link carousels**, **ChatGPT ads** live across the EU, the **IETF AIPREF** `Content-Usage`/`train-ai`-vs-`search` drafts, **Cloudflare's 15 Sep** ad-page crawler default, and fresh citation/traffic studies (DA&lt;40 sources, cited≠recommended, the SIGIR 252k-trial paper).
- **Cookbook cross-links in every chapter that has a recipe** — five *Reproducible example* callouts pointing to the runnable before/after in the [GEO Cookbook](https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook): `03 · Content` → chunk-friendly structure; `04 · Technical` → structured data (JSON-LD) and AI crawler access (`robots.txt` + `llms.txt`); `05 · Authority` → entity clarity with `sameAs`; `06 · Measurement` → citation anchoring. Each carries the recipe's own measured numbers and its offline-proxy caveat.
- `README.md`: **How to cite** section (plain-text citation built from `CITATION.cff`, plus the "Cite this repository" button).

### Changed

- **Citation precision fixes** in `02 · The Engines` and `04 · Technical GEO`: completed a truncated Google quote on `Google-Extended` (*"…nor is it used as a ranking signal in Google Search"*), moved the "does not affect Search ranking" attribution from the AI-features page to [`google-common-crawlers`](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers) where the sentence actually appears (in both the crawler table and the publisher-controls list), added Google's *written* "no AI text files needed" statement — flagged as the narrower non-necessity claim it is, scoped to Google's own AI features — alongside the existing oral Illyes/Mueller comments in the `llms.txt` verdict, and widened the `Google-Extended` grounding scope to the four destinations Google lists (Gemini Apps and Vertex AI, training and grounding).
- `04 · Technical GEO`: added the **IETF AIPREF** standardization (`train-ai` vs `search`; the `Content-Usage` HTTP header and `robots.txt` rule) and **Cloudflare's 15 Sep 2026** default block of training/agent crawlers on ad-bearing pages.
- `02 · The Engines`: added Google's embeddable **Preferred Sources** button and **AI Mode link carousels** to the Google publisher-controls profile.
- `07 · Research & Case Studies`: added the **SIGIR 2026 "What Gets Cited"** controlled-factorial study (252k trials; relevance + list position win, formatting barely helps) to Part 2.
- `LICENSE` now carries the **full CC BY-SA 4.0 legalcode** (previously a summary deed with a link) so GitHub's license detection identifies the repository as CC-BY-SA-4.0. Terms unchanged.

### Ongoing

- Expand the case studies and keep every engine's citation behavior current.

## [0.1.0] — 2026-08-25

### Added

- Initial public release: full META documentation and **nine fully written, cited chapters**.
- `README.md` hub with a citable one-line definition of GEO (sourced to [arXiv:2311.09735](https://arxiv.org/abs/2311.09735), KDD 2024), the "Why this exists" rationale, and a full table of contents.
- Nine cited chapters under `docs/`: Foundations, The Engines, Content Strategy, Technical GEO, Authority & Trust, Measurement, Research & Case Studies, Future & Ethics, and Glossary.
- `CONTRIBUTING.md` with the PR process, the "cite or flag `needs verification`" rule, style guide, and weekly review cadence.
- `updates/` weekly-log convention (one file per ISO week).
- GitHub templates: pull request template and a "new technique" issue template, both requiring cited/verifiable contributions.
- `LICENSE`: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).

[Unreleased]: https://github.com/ferinazumaDEV/generative-engine-optimization-handbook/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/ferinazumaDEV/generative-engine-optimization-handbook/releases/tag/v0.1.1
[0.1.0]: https://github.com/ferinazumaDEV/generative-engine-optimization-handbook/releases/tag/v0.1.0
