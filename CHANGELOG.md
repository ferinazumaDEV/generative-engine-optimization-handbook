# Changelog

All notable changes to **The GEO Handbook** are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project aims to follow it. Because this is a documentation project rather than software, "versions" are content milestones, not code releases. Week-by-week detail lives in [`updates/`](updates/README.md); this file captures the notable milestones.

## [Unreleased]

### Added

- **First weekly landscape entry: [`updates/2026-W36.md`](updates/2026-W36.md)** — the busy late-August 2026 GEO week: Google's embeddable **Preferred Sources** button + **AI Mode link carousels**, **ChatGPT ads** live across the EU, the **IETF AIPREF** `Content-Usage`/`train-ai`-vs-`search` drafts, **Cloudflare's 15 Sep** ad-page crawler default, and fresh citation/traffic studies (DA&lt;40 sources, cited≠recommended, the SIGIR 252k-trial paper).

### Changed

- `04 · Technical GEO`: added the **IETF AIPREF** standardization (`train-ai` vs `search`; the `Content-Usage` HTTP header and `robots.txt` rule) and **Cloudflare's 15 Sep 2026** default block of training/agent crawlers on ad-bearing pages.
- `02 · The Engines`: added Google's embeddable **Preferred Sources** button and **AI Mode link carousels** to the Google publisher-controls profile.
- `07 · Research & Case Studies`: added the **SIGIR 2026 "What Gets Cited"** controlled-factorial study (252k trials; relevance + list position win, formatting barely helps) to Part 2.

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

[Unreleased]: https://github.com/ferinazumaDEV/generative-engine-optimization-handbook/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ferinazumaDEV/generative-engine-optimization-handbook/releases/tag/v0.1.0
