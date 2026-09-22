# Changelog

All notable changes to **The GEO Handbook** are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project aims to follow it. Because this is a documentation project rather than software, "versions" are content milestones, not code releases. Week-by-week detail lives in [`updates/`](updates/README.md); this file captures the notable milestones.

## [Unreleased]

## [0.1.4] — 2026-09-22

### Added
- **`06 · Measurement` — the noise floor of the Brave observation, and the
  confound two controls found.** Six queries, twice, an hour apart. Read
  naively the binary citation variable changed in three of six; that reading is
  wrong. A position control and an address control show the two blanks were a
  datacenter address running out of quota, not the product deciding to stop
  citing. Among the four queries answered in both passes the variable flipped
  once. The finding that outlives the number: **a query an engine declines to
  answer looks exactly like a query it answered without citing**, so a study
  that scores a missing answer as "no citation" manufactures an effect out of
  its own rate limit.
- **`docs/protocols/minor-engines-citations.md`** — what do-it-yourself
  measurement can actually reach, measured rather than assumed.
- `RELEASING.md`: how a release of this work actually happens, including the
  rule that the GitHub Release is created by hand here and that doing so is what
  mints the DOI — the opposite of the rule in the package repositories.
- **Weekly landscape entry: [`updates/2026-W39.md`](updates/2026-W39.md)** — covering 14–20 Sep 2026: Cloudflare's 15 Sep defaults confirmed to hit Googlebot **and** the new `Disallow AI Training` setting that resolves the trade-off; Google's **AI contribution pilot** paying publishers whose content grounds AI answers; **OpenAI's Astra for Law**, the third vertical in seventeen days answered from a licensed corpus; **Apple's Siri AI** shipping as a Gemini-backed default answer surface on iOS 27; the first server-log measurement of `llms.txt` with a DOI, and John Mueller's public confound for it; Mueller on the record that Search Console cannot usefully report AI position; Google's scraper-blocking squeeze on third-party rank data; Ahrefs' France natural experiment. Includes **negative findings**, a **coverage-and-gaps** note that names what was *not* swept, and an unusually long **needs-verification** list.
- **`02 · The Engines` — new section: Siri AI (Apple).** A default answer surface on iOS/iPadOS/macOS/watchOS/visionOS 27 from 14 Sep 2026, Gemini-backed, with no vendor guidance and no measured citation study — stated as unmeasured rather than guessed at, with a pointer to the observation protocol as the way to fix that.
- **`07 · Research & Cases`** — HAE-GEO ([arXiv:2609.06027](https://arxiv.org/abs/2609.06027) v2) on what agents do *after* ingesting poisoned evidence; the now-settled *Caption Injection* paper (ECML PKDD 2026, logged not endorsed); and Ahrefs' France before/after study, labelled vendor data with its 9-day post-window stated.
- **`06 · Measurement` — "Two vendor-side confounds landed in one week."** Google's scraper blocking (~80% collection drop reported by Nozzle) and OpenAI retiring automatic Instant→Thinking switching, plus the general rule they make concrete: every citation measurement must log engine, model, mode, account tier and achieved sample rate, or the series is not evidence.
- **`08 · Future & Ethics`** — Google's AI contribution pilot as the first time the broken bargain has been answered with money instead of links, with the generation-vs-link distinction quoted; and HAE-GEO's *corroboration trap* under the manipulation risk.
- **`05 · Authority`** — Google Search profiles at the new 10,000-follower threshold as an owned entity surface, with an explicit warning that Google ties it to neither AI Mode nor AI Overviews.

- **Weekly landscape entry: [`updates/2026-W38.md`](updates/2026-W38.md)** — covering 7–13 Sep 2026: Cloudflare's 15 Sep crawler default reaching untouched Free-plan zones (a correction to what the handbook said), "People also ask" answers now ≈ AI Overviews, the AI Mode citation regression on Gemini 3.8 Flash, Merchant Center AI performance insights, ChatGPT for Financial Services, the Amazon DSP ad pilot in ChatGPT, Perplexity's Sonar deadline reconfirmed and its Q2D-Web benchmark, three GEO preprints, Semrush's manufacturing study, Le Monde's audience figures, the DOJ statement of interest. Includes **negative findings** and a **coverage-and-gaps** note.
- **`07 · Research & Cases`** — three September 2026 preprints logged under the honesty note, each with its caveat (vendor-affiliated / vendor-released / simulation-only).
- **`06 · Measurement`** — Merchant Center *AI performance insights* (top search intents, top terms, popular attributes for AI Mode and AI Overviews — the first first-party Google surface with AI query terms) and the 27 Sep Perplexity Sonar deadline as a pipeline-breaking date.

### Changed
- **A sentence published in this handbook an hour earlier was disproved and is
  withdrawn in place.** The noise-floor section predicted a third pass and said
  the quota *"recovers on its own with time"*. Pass C ran an hour later and
  returned 0 of 6, every page titled `Brave Search`. The claim rested on pass B
  answering four queries an hour after pass A, which is equally explained by the
  budget not being spent yet. What is measured, and all that is measured: about
  ten answered queries exhaust it, and recovery is longer than an hour. The
  design consequence is harsher than the first version implied — **a panel of 12
  queries by 5 engines by 4 dates does not fit on one datacenter address**, and
  spacing requests within a day does not fix it.
- **`04 · Technical GEO`** — **resolution** of the Cloudflare `needs-verification` flag: the 15 Sep defaults do apply to mixed-use crawlers (*"either setting impacts search as well as training"*), and the new **Disallow AI Training** setting publishes a `Disallow:` directive for `Google-Extended` / `Applebot-Extended` instead — with Bing unsupported until early 2027. Also: the `llms.txt` verdict now rests on a measurement rather than an absence (Hall, [10.5281/zenodo.22814844](https://doi.org/10.5281/zenodo.22814844), competing interest declared) plus Mueller's directory-site confound; Apple's blunt `nosnippet` opt-out compared against Google's and Cloudflare's surgical ones; `ChatGPT-User` re-dated to 219 prefixes (18 Sep 2026) against Perplexity's nineteen-month-old IP file; `Mediapartners-Google` generalised.
- **`02 · The Engines`** — ChatGPT: **Astra for Law** completing the health → finance → law run, with the consequence stated plainly (in a licensed vertical the ceiling on open-web citation is set by the deal, not by your content); Sponsored Agents quoted from OpenAI's own post; the Instant→Thinking retirement as a measurement confound. Google: local knowledge panels rendering as AI Overviews, AI Mode text-link ads that **must be excluded from citation counts**, and Search Live on Gemini 3.8 Live as a third surface with unmeasured citation behaviour.

- **`02 · The Engines`, `03 · Content`, `07 · Research & Cases`, `08 · Future & Ethics`** — five `needs verification` markers replaced by primary sources fetched 2026-09-14 (crawler table re-verified and dated, Meta's three AI-relevant tokens added; Similarweb's own 60-vs-3.4-words statement; AI Act Art. 50 application date 2 August 2026 via Art. 113); the DeepSeek marker now records what was searched. (#30)
- **`04 · Technical GEO`** — **dated correction** under the Cloudflare 15 Sep 2026 note: the chapter said existing domains keep their settings; Cloudflare's press release says *"all existing free customers that have not changed their settings"* are moved to the new defaults too. Both Cloudflare texts quoted verbatim, including the Googlebot / Applebot / BingBot sentence; original paragraph retained.
- **`02 · The Engines`** — Google: PAA ≈ AI Overviews (vendor data, labelled) and citation display as a per-model property that can regress; ChatGPT: the vertical-connector pattern (health → finance) and the Amazon DSP ad pilot with OpenAI's stated control over placement; Perplexity: the Sonar retirement date and Q2D-Web.

### Fixed

- **`pr-review.yml`** — the AI citation review no longer returns "200 with no text" on large docs PRs. The diagnostics added in #29 showed the cause on the first failing run they saw: `stop_reason: max_tokens` with a single `thinking` block — the model thinks by default and a 1024-token budget was spent before any text. Thinking is now disabled for the review and the budget is 4096.

## [0.1.3] — 2026-09-13

### Added

- **[`docs/protocols/minor-engines-citations.md`](docs/protocols/minor-engines-citations.md)** — a
  one-pass observation protocol for inline citations in the smaller answer engines, and its first
  run (2026-09-13): Brave Search's AI answer showed inline citation markers on 6 of 6 fixed queries;
  You.com (sign-in wall in a clean session), Arc (no Linux client) and Claude (account required)
  were not observed and are said to be not observed. One screenshot, timestamps, limits.
- **Weekly landscape entry: [`updates/2026-W37.md`](updates/2026-W37.md)** — covering 31 Aug – 6 Sep 2026. Google's AI-features opt-out control going worldwide, the Perplexity Sonar deadline holding at 27 Sep, GPT-6 Astra, ChatGPT Ads at a $1B run rate, Perplexity's Hybrid Compute moving agent steps off the network, and Ahrefs' 3M-query citation-share snapshot. Includes a **negative-findings** section (Reddit's `robots.txt` never changed; no new evidence on the ChatGPT `site:` fan-out story) and an explicit **coverage-and-gaps** note naming what was not swept.

### Changed

- **`02 · The Engines`** — the *You.com / Brave / Arc* line no longer rests on a comparison blog: it
  states what the protocol above observed, with date and scope, and names what could not be observed.
  Claude's *structured citations with clickable source URLs* are now sourced to Anthropic's own web
  search tool documentation (primary) instead of an industry blog. Both blogs leave the sources list.
- **`04 · Technical GEO`** — the **Search generative AI control** reached **all websites worldwide on 31 August 2026**, so the section no longer carries the "geo-limited at launch, verify before relying on it" warning. Google's own wording is quoted on both halves of the trade-off: the control *"isn't used as a ranking or inclusion signal affecting other parts of Search"*, but opting out means *"You won't receive any traffic or impressions from these features."* The June UK-first history is retained.
- **`02 · The Engines`** — added the worldwide **Search generative AI control** and the Search Console **AI performance report** (no click data) to Google's publisher-controls list.

## [0.1.2] — 2026-09-06

The archived copy had fallen behind. `v0.1.1` was tagged on 4 September and eight
commits landed after it — including every correction below. So the Zenodo deposit
people were citing still contained the quotation attributed to Microsoft that
appears in none of the cited sources, the unsupported request-volume figure, and
the wording that promised a primary source for every claim. Those were fixed in
the repository on the 4th and remained in the archive until now.

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
