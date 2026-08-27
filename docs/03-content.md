# 03 · Content Optimization

> Part of **[The GEO Handbook](../README.md)** — a free, community-maintained reference on Generative Engine Optimization. New here? Start at the [README](../README.md). Terms are defined once in the [Glossary](09-glossary.md); this chapter assumes the mental model built in **[01 · Foundations](01-foundations.md)**.
>
> *Last substantive review: 2026-08. Time-sensitive figures are dated inline; verify anything marked `⚠️`.*

This is the chapter most creators come for. Foundations explained *what* GEO is and *how* an engine turns a page into a cited sentence. This chapter is the **on-page playbook**: the writing and formatting choices that make a passage of yours the one the model lifts, quotes, and attributes — and, just as important, the ones that demonstrably *don't* work so you can stop wasting effort on them.

The organizing idea, carried over from Foundations, is this:

> **You are not optimizing a page to rank. You are optimizing a *passage* to be extracted.** The unit of competition in a generative answer is the **chunk**, not the URL.

---

## TL;DR

- **The single most evidence-backed content move is to add verifiable material.** The founding, peer-reviewed GEO study found that adding **statistics, citing sources, and inserting quotations** produced the largest, most reliable visibility gains — clustering above the paper's headline **~40%** — while **keyword stuffing was among the *worst* methods** ([Aggarwal et al., KDD 2024](https://arxiv.org/abs/2311.09735)). Everything else in this chapter is downstream of that finding.
- **Write self-contained chunks.** One idea per section, a descriptive heading, and a passage that makes sense *lifted out of the page*. Retrieval systems index and quote at passage level, so a correct, standalone paragraph is your product.
- **Answer first, then elaborate.** Lead each section with the direct answer (inverted pyramid); put the payoff in the first sentence, not the fifth paragraph.
- **Formats that get extracted:** short **TL;DRs**, **Q&A / FAQ** blocks, **comparison tables**, **bulleted definitions**, and **ranked "best-of" lists** — the last of which made up **43.8% of all page types ChatGPT cited** in a 26,283-URL Ahrefs analysis ([Allsopp / Ahrefs, Dec 2025](https://ahrefs.com/blog/best-lists-research/)). *Caveat below:* being #1 in your *own* list does **not** reliably get your brand named.
- **Write for conversational, long-tail queries.** People type to assistants in full sentences — SimilarWeb measured ChatGPT prompts at roughly **17× the length of Google searches** ([SimilarWeb 2025 GenAI Landscape](https://officechai.com/ai/chatgpt-queries-17x-longer-than-google-searches-6x-longer-than-googles-ai-mode-similarweb-data/)). Match that phrasing in your headings and answers.
- **Freshness is a real signal.** In a 5,000+ URL study, **~44–50% of AI citations went to content published in 2025**, and ~85–89% to the last ~3 years ([Seer Interactive, Jun 2025](https://www.seerinteractive.com/insights/study-ai-brand-visibility-and-content-recency)). Date your content and update it.
- **E-E-A-T still matters, but its heaviest signals are *off-page*** (brand mentions, third-party citations) — covered in depth in **[05 · Authority & Trust](05-authority.md)**. On-page, the credibility cues an LLM can extract are exactly the paper's winners: named authors, real sources, first-hand evidence.

---

## First, calibrate: what's *proven* vs. *plausible* vs. *consensus*

GEO advice online is a firehose of confident claims, most of them uncited. This handbook's rule is to tell you **how much weight each tactic actually carries**. The table below rates the on-page techniques in this chapter by the strength of evidence behind them, so you can prioritize honestly.

| Technique | Evidence level | Basis |
|---|---|---|
| Add **statistics**, **cite sources**, add **quotations** | **Demonstrated** (controlled experiment) | [Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735) — top-performing methods, ~40%+ gains |
| **Keyword stuffing** (as a positive tactic) | **Demonstrated *not* to work** | Same study — among the weakest, sometimes net-negative |
| **"Best-of" / ranked list** format gets cited | **Observed at scale** (large-sample observational) | [Ahrefs, Dec 2025](https://ahrefs.com/blog/best-lists-research/) — 43.8% of ChatGPT-cited page types |
| **Freshness / recency** raises citation odds | **Observed at scale** (observational) | [Seer Interactive, Jun 2025](https://www.seerinteractive.com/insights/study-ai-brand-visibility-and-content-recency) |
| **Conversational / long-tail** phrasing matches real queries | **Behavioral data + mechanism** | [SimilarWeb, 2025](https://officechai.com/ai/chatgpt-queries-17x-longer-than-google-searches-6x-longer-than-googles-ai-mode-similarweb-data/) — prompts ~17× longer |
| Self-contained **chunks**, **TL;DR**, **Q&A**, **tables**, **definitions** | **Consensus + mechanism** (how RAG chunking works) | Practitioner consensus + retrieval mechanics; not isolated in a public controlled test `⚠️` |
| **Answer-first** (inverted pyramid), question-shaped headings | **Consensus + mechanism** | Practitioner consensus; aligns with how retrieval selects passages `⚠️` |
| On-page **E-E-A-T** (author bylines, credentials, experience) | **Consensus + indirect** | Aligns with the paper's credibility signals; strongest proof is *off-page* → see [Ch. 05](05-authority.md) |
| **Schema markup** as a *direct* citation lever | **Tested — no direct effect found** | [Ahrefs via SEJ, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/); helps *indirectly* → see [Ch. 04](04-technical.md) |

> **How to read this table.** "Demonstrated" means someone ran a controlled test and measured it. "Observed at scale" means a large observational study found a strong pattern (correlation, not proof of cause). "Consensus + mechanism" means it's not been isolated in a public experiment, but it follows directly from how retrieval/chunking works and virtually every practitioner recommends it — reasonable to do, but hold it more loosely. When in doubt, **prefer the demonstrated tactics and measure the rest yourself** (see [06 · Measurement](06-measurement.md)).

---

## Technique 1 — Write extractable chunks (the whole game)

A generative engine retrieves and reasons over **passages**, not entire documents. Its retriever splits pages into chunks, embeds them, and pulls the few that best match the query; the LLM then synthesizes an answer from those chunks and attributes some of them ([mechanism recap in Foundations](01-foundations.md#how-a-generative-engine-turns-your-page-into-a-cited-answer)). The practical consequence:

> **Every section should survive being copied out of the page and still make sense on its own.**

If a paragraph only makes sense after three paragraphs of setup, it is a bad chunk — the retriever may grab it *without* that setup, and either the model won't use it or it'll misuse it. Concretely:

- **One idea per section.** Don't braid three topics into one heading. Split them so each maps to one question a person might ask.
- **Front-load the entity and the claim.** Start with the *thing* ("**The Nintendo Switch 2** launched in June 2025…"), not a pronoun ("It launched…"). A chunk lifted out of context has no antecedent for "it."
- **Descriptive, question-shaped headings.** `## How much does a UK visa cost in 2026?` beats `## Costs`. The heading is part of what gets embedded and matched.
- **Keep chunks self-contained but short.** Aim for passages that state a complete thought in a few sentences. Walls of text bury the extractable claim; one-line fragments starve it of context.
- **Repeat key context, sparingly.** Because chunks travel alone, it's fine — even helpful — to re-state the subject or the year in a section rather than relying on it being established elsewhere on the page.

This is *mechanism-based consensus*, not a lab result (`⚠️` — no public controlled study isolates "self-contained chunks" as a variable), but it falls straight out of how RAG works and is the least controversial recommendation in the field.

### Anatomy of a citable passage

```
## <Question a real person would ask, verbatim-ish>

<Direct one-sentence answer — the quotable core.>
<One or two sentences of specific support: a stat, a date, a named source.>
<Optional: a short list or a row of a comparison table.>

Source: <link to the primary source for the claim>
```

A passage in that shape gives the model everything it needs to quote you *and* to trust the quote: a clear claim, evidence, and provenance — all in one liftable block.

---

## Technique 2 — Answer first (inverted pyramid)

Lead with the answer, then explain. This is old journalism wisdom, and it maps perfectly onto passage retrieval: the sentence most likely to be extracted is the one that *directly answers the query*, so put it first and make it complete.

- **First sentence of a section = the answer.** Background, caveats, and nuance come after.
- **The first ~100–200 words of the page should already answer the primary question.** Real-time retrieval engines weight opening content heavily; a page that buries the answer under a personal preamble gives the retriever nothing to grab early. *(Widely recommended by practitioners; treat the exact "200 words" as a rule of thumb, not a measured threshold `⚠️`.)*
- **Don't make the model infer.** If the answer is "no, but with two exceptions," say exactly that in the lead, then list the exceptions.

A TL;DR block at the top of the page (like the one in this chapter) is the purest form of this: a pre-chunked, self-contained summary of your best claims, handed to the retriever on a plate.

---

## Technique 3 — Add the "citable trio": statistics, sources, quotations

This is the **most evidence-backed section of the chapter**, because it comes straight from the controlled experiment that named the field.

The founding GEO paper tested nine content-rewrite methods across a 10,000-query benchmark and measured the change in each source's visibility inside generated answers. The three that consistently won — the cluster the authors credit with the headline **"over 40%"** visibility increase — were:

| Method | What it means in practice |
|---|---|
| **Cite Sources** | Attribute claims to named, linkable sources (studies, official docs, primary data). |
| **Quotation Addition** | Include short, relevant quotations from credible authorities. |
| **Statistics Addition** | Replace vague claims with concrete, sourced numbers. |

Meanwhile **Keyword Stuffing** — the caricature of legacy SEO — was one of the *weakest* methods and, in places, counter-productive ([Aggarwal et al., 2024, §1](https://arxiv.org/abs/2311.09735); see the [Foundations breakdown](01-foundations.md#the-nine-methods--and-the-headline-result)). The authors also reported visibility gains of **up to 37% on Perplexity**, a live engine.

> **Why this works (the intuition):** the same signals that make a human editor trust a passage — it's specific, it's sourced, it quotes an authority — are the signals an LLM uses to decide a passage is safe to repeat. Evidence *is* the ranking factor.

**Before → after, made concrete:**

> ❌ *"Zero-click search has been rising for years and most people don't click anymore."*
>
> ✅ *"Zero-click search is now the majority outcome: in early 2026, **68.01% of U.S. Google searches ended without a click** to an outside site, up from ~45% a decade earlier ([SparkToro, 2026](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/))."*

The second version is what gets quoted. It hands the model a number, a date, and a source — a complete, attributable unit.

> **A discipline, not a trick:** every stat and quote must be *real and correctly sourced*. Fabricated or misattributed numbers are the fast path to being wrong in an AI answer — and to the exact credibility problems the [Ethics chapter](08-future-ethics.md) covers. Precision without accuracy is worse than vagueness. When you can't verify a figure, say so, or leave it out.

> ⚠️ **On the exact percentages:** the paper's headline "~40%" and "up to 37% on Perplexity" are averages measured under 2023–24 conditions and are **domain-specific** (the authors stress this). Later work broadly replicates the *direction* — evidence beats keyword tricks — while refining the magnitudes for production retrieval pipelines. Read individual per-method percentages as "as measured then." Deep treatment of the literature and replications lives in **[07 · Research & Case Studies](07-research-cases.md)**.

---

## Technique 4 — Structure the page for extraction

Beyond the citable trio, *format* itself changes how liftable your content is. The formats below are the ones retrieval systems and practitioners consistently find extractable. Treat the strongly-cited ones (lists) as observed-at-scale, and the rest as mechanism-based consensus.

### TL;DR summaries
A short, self-contained summary near the top is a pre-made chunk of your best claims. It's the single easiest extractable unit to add to any page.

### Q&A / FAQ blocks
Format sections as an explicit question and a direct answer. This does two things at once: the question mirrors how people actually query assistants (Technique 5), and the answer is already a clean, self-contained chunk. A genuine FAQ that answers real user questions is one of the highest-leverage structures you can add.

### Comparison tables
Tables encode structured, row-by-row facts that models parse and reproduce cleanly — "Product A vs B vs C" across consistent attributes. A well-built comparison table is disproportionately quotable because each row is a compact, self-contained fact.

### Bulleted definitions
Define terms in `**Term** — one-sentence definition` form (as this handbook's glossary does). Definitions are catnip for "what is X?" queries and lift cleanly into answers.

### Ranked "best-of" lists — the format with the hard data (and a big caveat)

Ranked lists are, empirically, the most-cited page *type* in AI answers. In an Ahrefs analysis of **26,283 source URLs across 750 top-of-funnel prompts**, "best X" blog listicles made up **43.8% of all page types ChatGPT cited** — the single most prominent format ([Allsopp / Ahrefs, Dec 2025](https://ahrefs.com/blog/best-lists-research/)). Comparison-style content shows up across query types and platforms.

**But read the caveat carefully, because it's where most advice goes wrong:**

> Publishing a "best tools" list that ranks *your own product* #1 does **not** reliably get your brand *named* in the AI's answer. In a controlled test of 34 self-promotional lists, one researcher found the AI would "use your article as the source of its information, but won't actually mention your brand," and in **43% of cases a competitor was named instead** — even when the competitor was ranked *second* in the original list ([Makosiewicz, via SEJ, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/)).

The honest takeaway: **the list format is genuinely extractable, but self-serving ranking is not a shortcut to being recommended.** Lists win when they deliver real comparative value — transparent criteria, honest inclusion of alternatives, up-to-date data. Build them to *inform*, and disclose when you're in your own list. (More on the line between optimization and manipulation in [08 · Future & Ethics](08-future-ethics.md).)

> **Note on schema markup.** Adding JSON-LD structured data is often sold as a direct GEO lever. A controlled Ahrefs test (1,885 pages that added schema vs. ~4,000 controls) found **no meaningful direct uplift** in AI citations over 30 days ([SEJ, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/)). Schema still helps *indirectly* (it feeds Google's Knowledge Graph and general machine-readability) — but it's a **technical** measure, so it lives in **[04 · Technical GEO](04-technical.md)**, not here. Don't expect it to substitute for extractable writing.

---

## Technique 5 — Write for conversational, long-tail queries

People don't talk to assistants the way they type into Google. Where a Google query is a terse keyword fragment ("pizza near me"), a prompt to ChatGPT is usually a full, contextual sentence. SimilarWeb's 2025 GenAI Landscape report measured ChatGPT prompts at roughly **17× the length of Google searches** (and ~6× longer than Google's AI Mode) ([SimilarWeb 2025, via OfficeChai](https://officechai.com/ai/chatgpt-queries-17x-longer-than-google-searches-6x-longer-than-googles-ai-mode-similarweb-data/)).

> ⚠️ The *exact* unit is reported inconsistently across write-ups (characters vs. words, and figures like "60 characters" vs. "5.48 words" appear in secondary coverage). The robust, directional fact — **AI prompts are far longer and more conversational than keyword searches** — is not in dispute; treat any single precise word/character count as `needs verification`.

What to do with that:

- **Phrase headings as the question a person would actually ask.** `## What's the cheapest way to get from Lisbon to Porto?` matches a real prompt better than `## Transport options`.
- **Cover the long tail of specifics.** Conversational queries carry constraints ("…for a family of four, in winter, on a budget"). Content that addresses those specific combinations answers questions your keyword-optimized competitors never phrased.
- **Answer follow-ups on the page.** Assistants and users think in follow-up chains. Anticipate the next two questions and answer them in adjacent sections.
- **Use natural language, not keyword-ese.** Write the way a knowledgeable person would explain it aloud. This is the opposite of stuffing — and it aligns with the paper's finding that fluent, understandable phrasing helps while keyword density doesn't.

---

## Technique 6 — Keep it fresh

Recency is a measurable citation signal, especially on the fastest-moving engines. In Seer Interactive's study of **5,000+ URLs with extractable publish dates** cited across ChatGPT, Perplexity, and Google AI Overviews ([Seer, Jun 2025](https://www.seerinteractive.com/insights/study-ai-brand-visibility-and-content-recency)):

| Engine | Citations from 2025 | From last ~3 years (2023–25) |
|---|---|---|
| **Google AI Overviews** | 44% | 85% (strongest recency bias) |
| **Perplexity** | 50% | 80% |
| **ChatGPT** | 31% | 71% (longest tail — still surfaces old pages) |

The same study found AI crawler activity skewed hard to recent content: **~65% of bot log hits targeted pages from the past year**, ~89% within three years, and only ~6% on content older than six years.

Practical freshness moves:

- **Show a real, visible publish/update date** — and actually update the content when you touch it (don't just bump the date; that's the manipulation version, and it's brittle).
- **Refresh cornerstone pages on a cadence.** Re-verify stats, swap in current figures, add newly relevant sections. A page that says "as of 2026" with 2026 data reads as current to both humans and models.
- **Note that recency needs vary by topic.** Evergreen definitions age slowly; pricing, rankings, "best X," and news age fast. Seer's own conclusion was to *tailor recency to your industry*, not chase freshness for its own sake. ChatGPT's longer tail also means authoritative older content still gets cited — freshness is a strong signal, not the only one.

---

## Technique 7 — E-E-A-T signals a model can actually read

**E-E-A-T** — Experience, Expertise, Authoritativeness, Trustworthiness — comes from [Google's Search Quality Rater Guidelines](https://developers.google.com/search/blog/2022/12/google-raters-guidelines-e-e-a-t) and predates GEO, but the underlying idea (is this a trustworthy source?) is exactly what a generative engine is judging when it decides whether to repeat you.

Two honest framings up front:

1. **The *heaviest* trust signals are off-page, not on-page.** The strongest observed correlate of AI brand visibility isn't anything on your own site — it's how much the *rest of the web* talks about you. Ahrefs' 75,000-brand study (Dec 2025) found **YouTube mentions (~0.74)** and **branded web mentions (~0.66–0.71)** far out-correlated with AI visibility than backlinks (~0.19–0.24) or Domain Rating (~0.27–0.33) ([Ahrefs, 2025](https://ahrefs.com/blog/ai-brand-visibility-correlations/)). Those are *correlations, not proof of cause*, and they're the subject of **[05 · Authority & Trust](05-authority.md)** — but they mean on-page E-E-A-T is necessary, not sufficient.

2. **On the page, give the model the credibility cues it can extract.** These align directly with the paper's winning methods:
   - **A named author with a real byline and a bio** stating relevant credentials — not "Admin" or "Staff."
   - **First-hand experience** made explicit: "we tested," "in our 6 months running this," original screenshots, original data. Experience is the hardest E-E-A-T signal to fake and the most distinctive.
   - **Real sourcing**: link claims to primary sources (this *is* the "Cite Sources" method).
   - **Clear, consistent entity information** — full names for people, products, and your organization, so the engine can disambiguate and corroborate you (ties into [entity clarity in Ch. 05](05-authority.md)).
   - **Transparency**: dates, methodology, disclosures, and correction history signal a source that's accountable.

> ⚠️ **Watch the vendor stats here.** A lot of marketing posts cite dramatic figures like "pages with strong E-E-A-T get 96% of AI citations" or "author credentials increase citation probability by 60%." These come from single-vendor analyses with undisclosed or non-reproducible methodology and should be treated as **`needs verification`** — do not repeat them as fact. The *defensible* claim is narrower: credibility signals help, the strongest measured ones are off-page brand mentions, and on-page E-E-A-T aligns with what the controlled GEO study rewarded. Everything quantitative about E-E-A-T beyond that belongs in [Ch. 05](05-authority.md) with its caveats attached.

---

## Anti-patterns: what to stop doing

The flip side of the evidence is just as useful. Avoid:

- **Keyword stuffing.** Demonstrated to be among the *weakest* methods and sometimes net-negative ([Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735)). Keyword *coverage* (naturally addressing the topic) is fine; keyword *density* is a dead ritual.
- **Walls of undifferentiated text.** They bury the extractable claim. If a section has no liftable sentence, the model has nothing to quote.
- **Burying the answer.** Personal-blog preambles ("Before we get into it, let me tell you about my weekend…") push the answer past where retrieval looks. Lead with it.
- **Self-serving lists with no real value.** Ranking yourself #1 doesn't get you named ([Makosiewicz, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/)) and erodes the trust that *does*. Build lists that genuinely compare.
- **Unverifiable or fabricated stats.** The fastest way to be confidently wrong inside an AI answer — and a direct route to the harms in [Ch. 08](08-future-ethics.md).
- **Treating schema / `llms.txt` as a content shortcut.** They're technical measures with limited or indirect effect on citations ([SEJ, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/)); Ahrefs found **97% of published `llms.txt` files are never fetched**. See [Ch. 04](04-technical.md) for what technical work actually earns its keep.
- **Over-optimizing to the point of manipulation.** Adversarial text designed to hijack citations is a *different, riskier* activity than legitimate GEO, invites detection, and is covered — as a risk, not a recommendation — in [Ch. 08](08-future-ethics.md).

---

## The content optimization checklist

A page-level pass you can run before publishing. None of these is a magic bullet; together they cover the demonstrated and consensus tactics above.

- [ ] **TL;DR / summary** near the top — a self-contained chunk of the best claims.
- [ ] **Direct answer in the first ~100–200 words**; each section leads with its answer.
- [ ] **Descriptive, question-shaped headings** that mirror real conversational queries.
- [ ] **One idea per section**, each passage self-contained (survives being lifted out).
- [ ] **The citable trio present:** concrete **statistics**, **cited sources**, and relevant **quotations** — all real and correctly attributed.
- [ ] **Extractable formats** where they fit: **Q&A/FAQ**, **comparison tables**, **bulleted definitions**, honest **ranked lists**.
- [ ] **Named entities up front** (no orphan pronouns in lead sentences).
- [ ] **Visible publish/update date**, and content actually refreshed — current figures, current year.
- [ ] **E-E-A-T cues:** real author byline + credentials, first-hand evidence, transparent sourcing.
- [ ] **No keyword stuffing, no buried answers, no unverifiable claims.**
- [ ] **Every stat traceable to a real source** (the handbook's own rule — apply it to your own pages).

---

## Where to go next

- **[04 · Technical GEO](04-technical.md)** — making sure AI crawlers can *fetch and render* the content you just optimized (the price of entry). Schema, `robots.txt`, AI user-agents, `llms.txt`.
- **[05 · Authority & Trust](05-authority.md)** — the *off-page* half of credibility: brand mentions, entities, third-party citations — which the correlational data suggests carries even more weight than anything on your own page.
- **[06 · Measurement](06-measurement.md)** — how to test the "consensus" tactics on *your* content instead of taking them on faith.
- **[07 · Research & Case Studies](07-research-cases.md)** — the founding paper in depth, replications, and the per-method numbers with their caveats.
- **[02 · The Engines](02-engines.md)** — how ChatGPT, Perplexity, AI Overviews / AI Mode, Gemini, and Copilot differ in what they retrieve and cite.

---

## Sources

Primary/controlled evidence first, then large-sample observational studies, then behavioral data. All links verified as of 2026-08. Where a study is single-vendor or its methodology isn't fully reproducible, that's noted in-text — prefer the primary source and check dates.

- **Aggarwal, P., Murahari, V., Rajpurohit, T., Kalyan, A., Narasimhan, K., & Deshpande, A. (2024). *GEO: Generative Engine Optimization.* KDD 2024.** — the founding controlled study; source of the "citable trio" and the keyword-stuffing finding. [arXiv:2311.09735](https://arxiv.org/abs/2311.09735) · [PDF](https://arxiv.org/pdf/2311.09735) · [DOI:10.1145/3637528.3671900](https://doi.org/10.1145/3637528.3671900) · [project page & data](https://generative-engines.com/GEO/)
- **Allsopp, G. / Ahrefs (Dec 2025). *Do Self-Promotional "Best" Lists Boost ChatGPT Visibility? Study of 26,283 Source URLs.*** — "best X" lists = 43.8% of ChatGPT-cited page types. [ahrefs.com/blog/best-lists-research](https://ahrefs.com/blog/best-lists-research/)
- **Search Engine Journal (2026). *9 AI Search Myths, Debunked by 15 Million Data Points* (Ahrefs SPA studies).** — self-promotional-list caveat (Makosiewicz), schema-markup null result, `llms.txt` 97%-unread, backlink/DR correlations. [searchenginejournal.com](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/)
- **Ahrefs (Dec 12, 2025). *Top Brand Visibility Factors in ChatGPT, AI Mode, and AI Overviews (75k Brands Studied).*** — YouTube/web-mention correlations vs. backlinks/DR. [ahrefs.com/blog/ai-brand-visibility-correlations](https://ahrefs.com/blog/ai-brand-visibility-correlations/)
- **Seer Interactive (Jun 25, 2025). *Study: AI Brand Visibility and Content Recency* (5,000+ URLs).** — recency of cited content across ChatGPT, Perplexity, AI Overviews; AI-bot crawl recency. [seerinteractive.com](https://www.seerinteractive.com/insights/study-ai-brand-visibility-and-content-recency)
- **SimilarWeb (2025). *2025 Generative AI Landscape: From Platforms to Pathways.*** — ChatGPT prompts ~17× longer than Google searches; conversational query behavior. [SimilarWeb 2025, via OfficeChai](https://officechai.com/ai/chatgpt-queries-17x-longer-than-google-searches-6x-longer-than-googles-ai-mode-similarweb-data/)
- **SparkToro / Fishkin (2026). *In 2026, Less than One Third of Google Searches Still Send a Click* (Similarweb clickstream).** — the zero-click figure used in the before/after example. [sparktoro.com](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/)
- **Google. *Search Quality Rater Guidelines — E-E-A-T* (context for Technique 7).** [developers.google.com](https://developers.google.com/search/blog/2022/12/google-raters-guidelines-e-e-a-t)
- **Search Engine Land (2026). *Mastering Generative Engine Optimization in 2026: Full Guide* (practitioner-consensus reference).** [searchengineland.com](https://searchengineland.com/mastering-generative-engine-optimization-in-2026-full-guide-469142)

> **Found an error, a dead link, or a newer study?** This chapter is meant to be corrected. See [CONTRIBUTING.md](../CONTRIBUTING.md) — the one non-negotiable rule is that every claim carries a real source or an honest `⚠️ needs verification` flag. Special caution on this topic: the web is full of confident, uncited GEO stats. If you add one, bring its primary source.
