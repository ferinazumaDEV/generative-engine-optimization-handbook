# Claims — what this handbook asserts, and how strongly

This file is the handbook's maturity declaration: the vocabulary the cluster uses (handbook, cookbook, evidence ledger), the mapping from the markers the chapters already carry, and a graded table of the claims the handbook itself rests on. `about.jsonld` (`additionalProperty` → `maturity`, `reproducible`) is the source of truth once those values are set; when this file and `about.jsonld` disagree, `about.jsonld` wins.

## Vocabulary

| Grade | Meaning | Test |
|---|---|---|
| `established` | Reproducible effect, primary source, stated scope. | Someone else gets the same result from the primary source or from a script in this cluster. |
| `mixed` | Evidence points both ways; the scope decides. | At least one primary source for and one against, or a clear effect in one setting and none in another. |
| `experimental` | Plausible from mechanism, one study, or an uncontrolled observation; not measured under control. | No controlled measurement of the effect exists. **Default grade for any technique whose effect on citation has not been measured.** |
| `folklore` | Widely repeated; no reproducible evidence, or debunked. | The search for a primary source ends at other people repeating it. |
| `reproducible` (`yes` / `no`) | Orthogonal flag: a script in this cluster re-derives the number offline. | `yes` only where a Cookbook recipe exists (the *Reproducible example* callouts). |

**Alias: `solid` == `established`.** The ledger in [prompt-engineering-evidence](https://github.com/ferinazumaDEV/prompt-engineering-evidence) grades with `solid`, and its CI accepts only `solid | mixed | folklore`. Same meaning, two spellings; nothing is renamed.

## The markers the chapters already use, and what they mean here

| Marker | Where | Reads as |
|---|---|---|
| `> ⚠️ needs verification` | any chapter (rule in [CONTRIBUTING.md](CONTRIBUTING.md)) | `experimental` — `folklore` once a source shows it debunked |
| **Documented** | `05 · Authority` evidence table; `07 · Research` Tier 4 | `established` for the documented *fact* (model paper, filing); says nothing about an effect on citation |
| **Demonstrated** (controlled / peer-reviewed / adversarial) | `07 · Research` Tier 1 | `established` within the study's scope |
| **Observed at scale** (large-N, correlational, industry) | `05 · Authority`; `07 · Research` Tier 2 | `mixed` — correlation, usually single-vendor, not causal |
| **Behavioral** (measured human behaviour) | `07 · Research` Tier 3 | `established` for the behaviour; `experimental` for any tactic inferred from it |
| **Mechanism + consensus**, **Plausible** | `05 · Authority` | `experimental` |
| **Needs verification** (table row) | `05 · Authority` | `experimental`; never repeated as fact |
| *Reproducible example* callout | `03`, `04` (×2), `05`, `06` | `reproducible: yes` for the measured proxy; the engine effect keeps its own grade |
| *demonstrated / plausible / anecdotal* | [CONTRIBUTING.md](CONTRIBUTING.md), "What good looks like" | `established`-or-`mixed` / `experimental` / `folklore` candidate |

## Source versus primary source

- **Primary source:** a peer-reviewed paper, a model paper, an official document in which a vendor states a fact about *its own* product, a public dataset, or a script in this cluster that re-derives the number.
- **Source:** anything reporting a primary source second-hand — news, analyst posts, a vendor's claims about *other* systems, a study whose method is not disclosed.
- A number that has a source but no primary source carries its limitation in the same sentence and cannot lift a claim above `experimental`.
- The README's "100+ sources" is a count of links; the tables in `05 · Authority` and `07 · Research` say which ones are primary.

## Per-technique format

Every technique entry added or revised follows **Definition → Answer → Evidence → Implementation → Limitations → Sources**. *Evidence* names the grade and what the primary source actually shows, with its scope. *Sources* lists primary sources first, marked as such, then secondary ones.

## Claims the handbook rests on (graded)

Each row was checked against the primary source named. A claim not in this table keeps the marker its chapter gives it (mapping above) until it is added here.

| # | Claim | Grade | Reproducible | Primary source | Limitation, in the same sentence |
|---|---|---|---|---|---|
| 1 | "GEO" as a term; content-level edits raised visibility by up to 40 % | `established` | no | Aggarwal et al., KDD 2024 — [arXiv:2311.09735](https://arxiv.org/abs/2311.09735), [doi:10.1145/3637528.3671900](https://doi.org/10.1145/3637528.3671900) | 40 % is the paper's best case on its own benchmark and engine set-up, not a lift to expect on a live engine. |
| 2 | Topical relevance and list position, not formatting, decide the first citation | `established` within a two-document RAG testbed | no | Vishwakarma, Kumar, Jamidar, SIGIR 2026 — [arXiv:2605.25517](https://arxiv.org/abs/2605.25517) | ~252k trials across six LLMs and 18 factors in a controlled testbed; not a production-engine measurement. |
| 3 | "Optimising content raises citation on live engines" | `mixed` | no | Rows 1 and 2 | Row 1 measured content-level signals, row 2 formatting-only edits: different interventions, different answers, and no live-engine measurement in this cluster. |
| 4 | Major answer engines read `llms.txt` for retrieval or citation | `experimental` — no engine confirms it | no | Spec [llmstxt.org](https://llmstxt.org/); fetch data [Ahrefs, 137k sites](https://ahrefs.com/blog/llmstxt-study/) (logged in `updates/2026-W36.md`) | The 97 %-never-read figure is one vendor's sample (137k sites). |
| 5 | `Google-Extended` does not affect inclusion in Google Search and is not a ranking signal | `established` (Google documenting its own product) | no | [google-common-crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers) | Scoped to Google's own products; says nothing about other engines. |
| 6 | Client-side-only rendering is invisible to a fetch-only crawler (6 → 152 words) | `established` for the property · engine effect `experimental` | yes — Cookbook `ssr-vs-csr-rendering` | One controlled page pair; no engine's citation behaviour was measured. |
| 7 | JSON-LD makes typed facts extractable (0 → 37 facts, 0 → 17 entities) | `established` for the property · engine effect `experimental` | yes — Cookbook `structured-data-jsonld` | Same as 6. |
| 8 | Allowing AI user-agents and publishing `llms.txt` makes content reachable (0 → 8 of 8 UAs; 0 → 2,868 bytes) | `established` for the precondition · engine effect `experimental` | yes — Cookbook `ai-crawler-access` | Reachability is a precondition of citation, not a citation. |
| 9 | Self-contained sections survive a fixed-size splitter (0 of 5 → 5 of 5) | `established` for the property · engine effect `experimental` | yes — Cookbook `chunk-friendly-structure` | One article, one splitter setting (`chunk_size = 800`). |
| 10 | `sameAs` / `@id` resolve named entities to one Wikidata ID (0 → 5 of 5) | `established` for the property · engine effect `experimental` | yes — Cookbook `entity-clarity-sameas` | Five entities on one page. |
| 11 | Inline sources yield parser-liftable claim→source pairs (0 → 8 of 8) | `established` for the property · engine effect `experimental` | yes — Cookbook `citation-anchoring` | Eight claims in one document; the recipe rates its own confidence low–moderate. |
| 12 | Answers from live AI search vary across runs, prompts and time, so a one-off observation is not a representative measurement | `established` (as stated in the paper's abstract, which draws on its empirical studies) | no | Schulte, Bleeker & Kaufmann, 2026 — [arXiv:2604.07585](https://arxiv.org/abs/2604.07585) | The Jaccard range quoted in the Cookbook changelog (≈ 0.32–0.43) is repeated from that paper and carries `⚠️ needs verification` here until re-read against its tables; the direction is why a small live test cannot show a lift. |

## Work-level maturity

**Proposed, pending the owner's confirmation; not yet set in `about.jsonld`.** The proposal is `maturity: mixed`, `reproducible: no`. The handbook's central claim — that GEO techniques change what gets cited — has controlled evidence for content-level signals (row 1) and against formatting-only edits (row 2), and no live-engine measurement in this cluster. What is reproducible lives in the Cookbook (rows 6–11). Until `additionalProperty` is set in `about.jsonld`, the README ID card reads "see CLAIMS.md".

## Changing a grade

A grade changes only with a primary source, in a PR that names it (see [CONTRIBUTING.md](CONTRIBUTING.md)). The same PR bumps `dateModified` in `about.jsonld`; the README ID card and `llms.txt` follow it.
