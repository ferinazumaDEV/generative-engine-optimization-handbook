# The GEO Handbook

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22299644.svg)](https://doi.org/10.5281/zenodo.22299644)

**Everything about Generative Engine Optimization, in one place.** From *"what is GEO and where do I start?"* all the way to the technical checklist, the measurement method, and the primary research — whatever you need to get your content understood and **cited by AI answer engines** (ChatGPT, Perplexity, Google AI Overviews, Gemini, Copilot), you'll find it here. Beginner to practitioner, and **every single claim carries a real, verifiable source**.

> **Generative Engine Optimization (GEO)** is the practice of structuring, writing, and publishing content so that it is understood, trusted, and **cited by generative AI engines** — such as ChatGPT, Perplexity, Google AI Overviews / AI Mode, Gemini, and Copilot — when they answer a user's question.

The term was coined in the peer-reviewed paper *"GEO: Generative Engine Optimization"* (Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, & Deshpande), presented at **KDD 2024** — [arXiv:2311.09735](https://arxiv.org/abs/2311.09735) · [DOI:10.1145/3637528.3671900](https://doi.org/10.1145/3637528.3671900). That study was the first to show, in a controlled experiment, that content can be deliberately optimized for higher visibility in AI‑generated answers, reporting visibility gains of **up to 40%** from content‑level signals such as citing sources, adding statistics, and quoting credible authorities.

## GEO ID Card

The machine-readable version of this table is [`about.jsonld`](about.jsonld) (schema.org JSON-LD). That file is the source of truth; this table mirrors it field by field.

| Field | Value |
|---|---|
| Type | `CreativeWork` — *The GEO Handbook* |
| Creator | Fernando Aporta Franco (ferinazumaDEV) · sameAs: [github.com/ferinazumaDEV](https://github.com/ferinazumaDEV), [zentimes.es](https://zentimes.es) |
| Abstract | A comprehensive, sourced reference on Generative Engine Optimization (GEO): structuring, writing, and publishing content so it is understood, trusted, and cited by generative AI answer engines. |
| Based on | [arXiv:2311.09735](https://arxiv.org/abs/2311.09735) — Aggarwal et al., *GEO: Generative Engine Optimization*, KDD 2024 |
| Sources | Work-level citation: [arXiv:2311.09735](https://arxiv.org/abs/2311.09735). Every chapter lists its own sources, primary ones first; secondary (industry) sources are labelled as such |
| Cite as | DOI [10.5281/zenodo.22299644](https://doi.org/10.5281/zenodo.22299644) (concept DOI, always the latest release) — [`CITATION.cff`](CITATION.cff) |
| Canonical URL | <https://github.com/ferinazumaDEV/generative-engine-optimization-handbook> |
| License | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| Version | 0.1.1 |
| Published | 2026-08-25 |
| Last modified | 2026-09-04 |
| Maturity | see [CLAIMS.md](CLAIMS.md) |

---

## Why this exists

Search is shifting from a list of blue links to a **single synthesized answer**. When a person asks ChatGPT or Perplexity a question, the model composes a response and — increasingly — cites a handful of sources. If your content is not in that handful, you are invisible, no matter how well it ranked on classic Google.

Traditional SEO optimizes for *ranking a page*. **GEO optimizes for *being quoted inside the answer*.** The two overlap but are not the same, and the tactics that move the needle are different (and still being discovered).

This handbook is a **free, public, community-maintained reference** on how generative engines select, cite, and synthesize sources — and what creators can do about it. It is written to be useful to a **newcomer** ("what is this and where do I start?") and to a **practitioner** ("give me the technical checklist and the measurement method"). It aims to be *accurate and current*, to **cite real, verifiable sources**, and to grow every week through community contributions.

**Keywords:** generative engine optimization, GEO, AI search optimization, LLM SEO, answer engine optimization (AEO), how to get cited by ChatGPT / Perplexity / Google AI Overviews, RAG visibility, LLM citations.

---

## Table of Contents

| # | Section | What it covers |
|---|---------|----------------|
| 01 | [Foundations](docs/01-foundations.md) | What GEO is, GEO vs SEO vs AEO, how generative engines retrieve and cite, core vocabulary |
| 02 | [The Engines](docs/02-engines.md) | ChatGPT Search, Perplexity, Google AI Overviews / AI Mode, Gemini, Copilot — how each retrieves & cites, and how they differ |
| 03 | [Content Strategy](docs/03-content.md) | Writing extractable, citable content: structure, quotable stats, "chunk‑friendly" formatting, entity clarity |
| 04 | [Technical GEO](docs/04-technical.md) | Crawlability for AI bots, `robots.txt` & AI user‑agents, structured data, `llms.txt`, feeds, rendering |
| 05 | [Authority & Trust](docs/05-authority.md) | E‑E‑A‑T for machines, entities & knowledge graphs, citations, brand mentions, off‑site presence |
| 06 | [Measurement](docs/06-measurement.md) | How to measure AI visibility & citation share, tooling, referral traffic from AI, KPIs |
| 07 | [Research & Case Studies](docs/07-research-cases.md) | The primary literature, reproducible experiments, and documented case studies (cited) |
| 08 | [Future & Ethics](docs/08-future-ethics.md) | Where GEO is heading, prompt/answer manipulation risks, disclosure, and doing this responsibly |
| 09 | [Glossary](docs/09-glossary.md) | Plain-language definitions of every term used across the handbook |

> All nine chapters are written and cited (100+ primary sources, cited throughout). They are living documents kept current every week — [contributions and corrections welcome](CONTRIBUTING.md).

---

## How to contribute

This handbook only stays accurate if people keep it accurate. See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the PR process and the style guide. The one non‑negotiable rule: **every claim carries a real, linkable source, or it is explicitly marked `needs verification`.** No invented facts, no fabricated citations.

- Found something outdated or wrong? Open an issue.
- Have a new, *cited* technique? Use the [New Technique issue template](.github/ISSUE_TEMPLATE/new-technique.md) or open a PR.
- Small fixes (typos, dead links) are always welcome.

## Weekly-update cadence

GEO changes fast — engines ship, cite differently, and expose new controls almost weekly. To stay current:

- Every week we publish a dated log in **[`updates/`](updates/README.md)** (e.g. `updates/2026-W35.md`) summarizing *what changed in the GEO landscape* and *what changed in this repo*.
- A running summary of notable changes lives in **[CHANGELOG.md](CHANGELOG.md)** (Keep a Changelog format).
- Target cadence: **one update entry per ISO week.** Weeks with nothing material still get a short "no material change" note so the record is continuous.

## How to cite

Every tagged release is archived on Zenodo with a DOI. Cite the **concept DOI** — it always resolves to the latest release. Each release also carries its own version DOI, on its own record page, if you need to pin one exact state of the text.

> Aporta Franco, Fernando. *The GEO Handbook*. Zenodo, 2026. <https://doi.org/10.5281/zenodo.22299644>.

The same metadata lives in [`CITATION.cff`](CITATION.cff) — GitHub's **"Cite this repository"** button on the repo page renders it as APA or BibTeX.

## License

Content is licensed under **[Creative Commons Attribution‑ShareAlike 4.0 International (CC BY‑SA 4.0)](LICENSE)**. You may share and adapt the material, even commercially, as long as you give appropriate credit and license your derivatives under the same terms. Full text: <https://creativecommons.org/licenses/by-sa/4.0/legalcode>.

## Author & maintainer

Created and maintained by Fernando Aporta Franco (ferinazumaDEV). Contributions are credited to their authors; see the changelog and PR history. If you build on this, attribution to *"The GEO Handbook — Fernando Aporta Franco, CC BY‑SA 4.0"* is appreciated.

## Part of a cluster of open work

<!-- ecosystem:start -->
Part of a cluster of open work on making content legible to machines, by **Fernando Aporta Franco** ([ferinazumaDEV](https://github.com/ferinazumaDEV)):

**Three layers on GEO (Generative Engine Optimization)**
- **[The GEO Handbook](https://github.com/ferinazumaDEV/generative-engine-optimization-handbook)** — the reference: what to do and why, with sources (theory).
- **[The GEO Cookbook](https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook)** — six reproducible before/after recipes with offline measurements (practice).
- **[Evidence-Based Prompt Engineering](https://github.com/ferinazumaDEV/prompt-engineering-evidence)** — a graded, sourced ledger of prompting techniques (the input side).

**Small open tools**
- [typedout](https://github.com/ferinazumaDEV/typedout) — reliable structured output from OpenAI and Anthropic, with a provider interface for others.
- [politeclient](https://github.com/ferinazumaDEV/politeclient) — a polite HTTP client for Python: retries with backoff, per-host rate limiting, caching, pagination.
- [webhook-replay](https://github.com/ferinazumaDEV/webhook-replay) — capture a webhook once, then replay it at your local app as many times as you need.
- [scaffld](https://github.com/ferinazumaDEV/scaffld) — scaffold fully-wired Python projects from templates, with a TUI.
- [framesig](https://github.com/ferinazumaDEV/framesig) — find on-screen events in video by pixel signature; no ML.
- [notebooklm-kb-system](https://github.com/ferinazumaDEV/notebooklm-kb-system) — a token-efficient second brain for AI agents on top of NotebookLM.

Hub and writing: **[zentimes.es](https://zentimes.es)**.
<!-- ecosystem:end -->

More at **[github.com/ferinazumaDEV](https://github.com/ferinazumaDEV)**.

---

*This is a documentation-only project. It contains no code, no tracking, and no private data. Everything here is public and meant to be reused.*
