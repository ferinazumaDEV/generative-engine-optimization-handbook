# 09 · Glossary

> Part of **[The GEO Handbook](../README.md)** — a free, community-maintained reference on Generative Engine Optimization. New to the project? Start at the [README](../README.md). This chapter is the **canonical home for definitions**: a term is defined **once here** and linked from everywhere else ([CONTRIBUTING](../CONTRIBUTING.md)).
>
> *Last substantive review: 2026-08. Engine-specific facts are dated inline; anything unsettled is flagged `⚠️ needs verification`. Definitions are neutral, and where a term has a documented origin (a paper, RFC, standard, or vendor announcement) it is cited.*

---

## TL;DR — how to use this glossary

- **Alphabetical.** Jump to a letter (`## A` … `## Z`); each entry is a self-contained, one- to three-sentence definition designed to be lifted on its own.
- **Cross-linked.** Entries point to the chapter where the concept is worked in depth (e.g. → [04 · Technical](04-technical.md)). The *definition* lives here; the *practice* lives there.
- **Cited at the origin.** Terms that come from a specific source (the founding paper, an RFC, a vendor doc) carry that link. Conceptual/consensus terms are marked as such.
- **Honest about churn.** GEO vocabulary is young and unsettled. Where two communities use a word differently, or where a claim is time-sensitive, the entry says so rather than pretending there's a single authority.

> **Two quick disambiguations up front**, because they trip up every newcomer:
> - **GEO vs. AEO vs. SEO** — see the [acronym-soup table](#quick-reference-the-acronym-soup) below. Short version: SEO ranks a *page*, AEO wins a *direct answer*, GEO gets you *cited inside a synthesized answer*. This handbook uses **GEO** as the umbrella term.
> - **Training-time vs. retrieval-time** — an engine can "know" your brand two different ways: because your content was in its *training data*, or because it *retrieved your live page* to answer this specific question. GEO mostly targets the second; they are not the same lever. See [Training-time vs. retrieval-time](#training-time-vs-retrieval-time-attribution).

---

## Quick reference: the acronym soup

The field hasn't agreed on one name. These labels overlap heavily and are often used interchangeably; only **GEO** has a specific academic origin. Treat the "optimizes for" column as the *useful distinction*, not a policed boundary.

| Acronym | Stands for | Optimizes for | Origin / status |
|---|---|---|---|
| **SEO** | Search Engine Optimization | Ranking a page in a list of results | 1990s–2000s search industry |
| **AEO** | Answer Engine Optimization | Being the source of a **direct answer** (featured snippets, AI Overviews, voice) | Industry term; **no single canonical definition** `⚠️` |
| **GEO** | Generative Engine Optimization | Being **cited/quoted/recommended inside a generative answer** | Coined in [Aggarwal et al., KDD 2024](https://arxiv.org/abs/2311.09735) |
| **LLMO** | LLM Optimization | Same space as GEO; emphasis on the model | Informal synonym `⚠️` |
| **AIO** | AI Optimization | Umbrella for "optimizing for AI surfaces" | Informal synonym `⚠️` |
| **GAIO** | Generative AI Optimization | Same space as GEO | Informal synonym `⚠️` |
| **"AI SEO"** | — | Loose umbrella; usually means GEO + technical AI crawlability | Informal `⚠️` |

The full comparison (win conditions, signature tactics, how they layer rather than compete) is in **[01 · Foundations → GEO vs. SEO vs. AEO](01-foundations.md#geo-vs-seo-vs-aeo--and-the-rest-of-the-acronym-soup)**.

---

## A

### AEO (Answer Engine Optimization)

Optimizing content to be the source of a **direct answer** on an "answer surface" — featured snippets, knowledge panels, voice assistants, and AI Overviews — rather than one link among many. Often used interchangeably with GEO; some practitioners reserve AEO for *answer surfaces inside traditional search* and GEO for *standalone LLM assistants*, but there is **no single authoritative definition** and no coining paper. `⚠️ needs verification on any claim about who coined "AEO" or a canonical GEO/AEO boundary.` → [01 · Foundations](01-foundations.md#geo-vs-seo-vs-aeo--and-the-rest-of-the-acronym-soup)

### AI bot / AI crawler

An automated agent operated by an AI vendor to fetch web content. They do different jobs — **training** (collect data to train models), **search/indexing** (build the retrieval index an engine cites from), and **user-triggered fetch** (grab a page in real time to answer a live prompt) — and each job often has its own user-agent token. Which one to allow is a per-purpose decision, not all-or-nothing. See the [AI crawler quick-reference table](#ai-crawler-user-agents-quick-reference) and → [04 · Technical GEO](04-technical.md#ai-crawlers-the-bots-you-need-to-know).

### AI impression

In Google Search Console's **AI Performance** report, a recorded appearance of your page inside an AI surface (AI Overviews / AI Mode). An AI impression is **not** the same as a classic search impression and does **not** imply a click — treat it as a visibility signal, not traffic. As of 2026 the exact counting rules are vendor-defined and evolving. ([Bing Webmaster Tools AI Performance](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview) · [Search Engine Journal on Google's report](https://www.searchenginejournal.com/google-reports-ai-search-impressions-how-to-read-them/582824/)) → [06 · Measurement](06-measurement.md#google-search-console-the-ai-performance-report)

### AI Mode (Google)

Google's conversational, generative search experience (a full chat-style mode, distinct from the AI Overview shown atop normal results). It leans heavily on the [query fan-out](#query-fan-out-google) technique. Google reported AI Mode passing large user milestones in 2026, but `⚠️ current user counts change monthly — verify against Google's own announcement before quoting a number.` → [02 · The Engines](02-engines.md#google--ai-overviews-ai-mode--gemini)

### AI Overview / AI Overviews (AIO) (Google)

Google's AI-generated summary shown **above or among** classic search results, with supporting links. Formerly launched as **SGE (Search Generative Experience)** in 2023. When an AI Overview appears, click-through to results drops sharply (Pew and SparkToro both measured large declines in 2025–2026). Prevalence has been volatile — appearing on a single-digit-to-mid-teens percentage of queries depending on the study and month. ([Pew Research, 2025](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) · [Search Engine Land on Semrush data, 2025](https://searchengineland.com/google-ai-overviews-surge-pullback-data-466314)) → [02 · The Engines](02-engines.md#google--ai-overviews-ai-mode--gemini)

### AI referral traffic

Visits that arrive at your site from a click *inside* an AI engine's answer (e.g. a Perplexity citation, a ChatGPT source link). It is chronically under-counted because many engines pass no or inconsistent HTTP referrer (see [referrer leakage](#referrer-leakage)), and it is a **lagging** indicator — most AI answers are [zero-click](#zero-click-search). Several 2025–2026 industry analyses report AI referrals convert at higher rates than classic organic, though the numbers are noisy and vendor-flavored. `⚠️ treat conversion-multiple claims as directional.` → [06 · Measurement](06-measurement.md#layer-2--the-traffic-layer-ai-referrals-in-analytics)

### AI SEO

Informal umbrella term for "optimizing for AI search," usually meaning GEO plus the technical work of being crawlable by AI bots. No canonical definition. `⚠️` → see [GEO](#geo-generative-engine-optimization).

### AI Share of Voice

See [Share of Voice](#share-of-voice-sov--citation-share).

### Answer engine

A search experience that returns a **synthesized answer** (often with citations) instead of, or above, a list of links. Includes both AI-answer surfaces inside traditional search (AI Overviews) and standalone assistants (ChatGPT, Perplexity). The generative subset of answer engines is what GEO targets. → [01 · Foundations](01-foundations.md)

### Answer-first (inverted pyramid)

A writing pattern where the direct answer comes in the **first sentence of a section** (or first ~100–200 words of a page), with elaboration after. It maximizes [extractability](#extractability-liftability): an engine can lift a correct, self-contained answer from the top of the [chunk](#chunk) without parsing the whole page. Borrowed from journalism's "inverted pyramid." → [03 · Content Strategy](03-content.md#technique-2--answer-first-inverted-pyramid)

### Attribution

Which source(s) an engine credits for a statement. In GEO it has two distinct senses: **citation attribution** (the visible linked/named source) and **content attribution** (whether your *facts* made it into the answer even if you weren't linked — see [citation absorption](#citation-absorption)). Distinguish both from [training-time vs. retrieval-time](#training-time-vs-retrieval-time-attribution) attribution. → [06 · Measurement](06-measurement.md)

### Authoritative (GEO method)

One of the [nine content-rewrite methods](#geo-content-methods-the-nine) tested in the founding paper: rephrasing content to sound more authoritative/confident. A middling performer on its own — far behind adding real citations, quotations, and statistics. ([Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735)) → [07 · Research & Cases](07-research-cases.md#the-nine-methods-they-tested)

---

## B

### Backlink

An inbound hyperlink from another site — the classic SEO authority signal. In GEO its role is **diminished but not gone**: LLMs are trained on text, not a link graph, so an **unlinked** [brand mention](#brand-mention-unlinked-mention) can teach a model much of what a linked one would. Backlinks still matter for the *classic index* that AI engines retrieve from. → [05 · Authority & Trust](05-authority.md#backlinks-vs-brand-mentions-in-the-geo-era)

### Bingbot

Microsoft's search crawler. It matters disproportionately for GEO because the **Bing index powers ChatGPT Search and Microsoft Copilot's** retrieval, so being indexed in Bing is a prerequisite for citation on those surfaces. ([Bing Webmaster Tools — which crawlers does Bing use](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0) · [llmpulse crawler index](https://llmpulse.ai/ai-crawler-index/bingbot), industry source) → [04 · Technical GEO](04-technical.md#ai-crawlers-the-bots-you-need-to-know)

### Brand mention (unlinked mention)

Any reference to your brand/entity in text, **whether or not it links to you**. Because LLMs learn from [co-occurrence](#co-occurrence-branded-co-occurrence) in text rather than from links, an unlinked mention on a trusted page carries real GEO weight — a conceptual break from link-centric SEO. Count unlinked mentions as wins. ([GrowthX, 2026](https://growthx.ai/learn/branded-co-occurrence-ai-search) · [Ahrefs, Dec 2025](https://ahrefs.com/blog/ai-brand-visibility-correlations/)) → [05 · Authority & Trust](05-authority.md#backlinks-vs-brand-mentions-in-the-geo-era)

---

## C

### C4 (Colossal Clean Crawled Corpus)

A large, cleaned snapshot of [Common Crawl](#common-crawl--ccbot) used to train many language models. Notable for GEO because analyses of what's *in* it show a handful of domains dominate — a reason certain sources (Wikipedia, major publishers) are structurally over-represented in model "priors." ([Documenting the C4 corpus, EMNLP 2021](https://arxiv.org/abs/2104.08758)) → [07 · Research & Cases](07-research-cases.md#why-some-sources-dominate-the-training-corpus-papers)

### ChatGPT / ChatGPT Search (OpenAI)

OpenAI's assistant; **ChatGPT Search** is its web-connected mode that retrieves live sources and cites them. Its retrieval draws on the **Bing index** plus OpenAI's own crawling, so classic Bing indexation is part of the eligibility path. ([Yoast on ChatGPT Search](https://yoast.com/chatgpt-search/) · [OpenAI bots doc](https://developers.openai.com/api/docs/bots)) → [02 · The Engines](02-engines.md#chatgpt--chatgpt-search-openai)

### Chunk

A passage-sized unit of content that a retrieval system indexes and an engine may lift into an answer (the act of splitting a page into these units is **chunking**). GEO's core reframing: the unit of competition is the **chunk**, not the whole page — a single self-contained, quotable passage can be cited even from a page that wouldn't "rank." Keep chunks short and self-contained. → [01 · Foundations](01-foundations.md#how-a-generative-engine-turns-your-page-into-a-cited-answer) · [03 · Content](03-content.md#technique-1--write-extractable-chunks-the-whole-game)

### Citable trio

This handbook's shorthand for the three content additions the founding paper found most effective: **statistics, cited sources, and quotations**. Adding concrete, verifiable material of these three kinds drove the paper's largest visibility gains. → [03 · Content Strategy](03-content.md#technique-3--add-the-citable-trio-statistics-sources-quotations)

### Citation

A source an engine **links or names** in its answer. Being cited is GEO's **primary target outcome** — the visible payoff at the end of the retrieve→select→synthesize→cite pipeline. → [01 · Foundations](01-foundations.md)

### Citation absorption

Whether your **facts or claims are carried into an answer even when you are not the linked source** — content-level attribution, as opposed to citation selection (who gets the link). A 2026 research thread measures this directly; it means you can "win" on substance while another site gets the visible credit. `⚠️ based on recent preprints — check version and peer-review status.` → [07 · Research & Cases](07-research-cases.md#part-2--research-building-on-geo-the-wider-literature)

### Citation share

See [Share of Voice](#share-of-voice-sov--citation-share).

### ClaudeBot / Claude-SearchBot / Claude-User

Anthropic's crawler tokens, split by purpose: **ClaudeBot** (general crawl, incl. training-related), **Claude-SearchBot** (builds Claude's search index), and **Claude-User** (fetches a page to answer a user's live request). The split lets a site allow the search/user bots while controlling the training crawl. ([Anthropic support](https://support.claude.com/en/articles/8896518) · [Search Engine Land](https://searchengineland.com/anthropic-claude-bots-470171)) → [04 · Technical GEO](04-technical.md#ai-crawlers-the-bots-you-need-to-know)

### Click-through rate (CTR)

The share of impressions that result in a click. Central to SEO, **degraded as a metric in the AI era**: [zero-click](#zero-click-search) answers and AI Overviews depress CTR, and an [AI impression](#ai-impression) may never generate a click at all. → [06 · Measurement](06-measurement.md#why-measurement-is-different-here)

### Co-occurrence (branded co-occurrence)

How often your brand/entity appears **alongside** a topic across documents. Because LLMs learn associations from text statistics, co-occurring with your target topic on trusted pages teaches the model "brand X ≈ topic Y" — even without a link. Feeding real co-occurrence (digital PR, mentions in relevant contexts) is a core GEO lever. ([GrowthX, 2026](https://growthx.ai/learn/branded-co-occurrence-ai-search)) → [05 · Authority & Trust](05-authority.md#backlinks-vs-brand-mentions-in-the-geo-era)

### Comet Plus (Perplexity)

Perplexity's **publisher revenue-share program**, part of a broader move by engines to compensate sources they cite. Part of the emerging "citation economics" of AI search. ([Search Engine Journal, 2025](https://www.searchenginejournal.com/perplexity-launches-comet-plus-shares-revenue-with-publishers/554596/)) → [02 · The Engines](02-engines.md#perplexity)

### Common Crawl / CCBot

A large, freely available web crawl (**CCBot** is its crawler) that underpins many training datasets, including [C4](#c4-colossal-clean-crawled-corpus). Blocking CCBot influences whether your content enters that common training supply. ([commoncrawl.org](https://commoncrawl.org/ccbot)) → [04 · Technical GEO](04-technical.md)

### Consensus (corroboration)

When multiple independent sources state the same fact, engines are more likely to treat it as reliable and repeat it. A practical implication: being **one of several** corroborating sources on a claim can matter more than being the single best page. → [05 · Authority & Trust](05-authority.md#mechanism-3--corroboration-and-consensus)

### Copilot (Microsoft)

Microsoft's assistant, integrated across Bing and Microsoft products; **Copilot Search in Bing** is its cited-answer surface. Retrieval is Bing-index-based, so Bing indexation and Microsoft-adjacent authority help. ([Bing blog, 2025](https://blogs.bing.com/search/April-2025/Introducing-Copilot-Search-in-Bing)) → [02 · The Engines](02-engines.md#microsoft-copilot--bing)

### Core Web Vitals

Google's page-experience metrics (loading, interactivity, layout stability). Relevant to GEO mainly as a **crawl-efficiency and classic-ranking** input; most AI crawlers care more about fast, reliable **HTML delivery** ([TTFB](#ttfb-time-to-first-byte)) than about cosmetic front-end performance. → [04 · Technical GEO](04-technical.md#page-speed-and-crawl-efficiency)

### Crawlability

Whether an engine's bot can **fetch and parse** your content at all. It's the price of entry: a page an AI crawler can't reach (blocked, JS-only, slow, error-prone) can't be selected or cited, no matter how good it is. → [04 · Technical GEO](04-technical.md)

### Crawl-to-refer ratio

How many times a vendor's bot **crawls** you per visitor it **sends back**. A high ratio (lots of crawling, few referrals) is normal for AI engines — because most answers are [zero-click](#zero-click-search) — and it reframes "crawl ≠ citation ≠ traffic." Useful for spotting bots that take a lot and give little. ([Cloudflare, 2025](https://blog.cloudflare.com/ai-crawler-traffic-by-purpose-and-industry/) · [Seomator](https://seomator.com/blog/crawl-to-refer-ratio-ai-crawlers-llm-bots)) → [06 · Measurement](06-measurement.md#crawl--citation-the-crawl-to-refer-reality)

---

## D

### Digital PR

Earning coverage, mentions, and co-occurrence on **trusted third-party sites** — the most actionable off-page GEO lever. It works by feeding the model real associations between your entity and your topic across credible documents, rather than by chasing links for their own sake. Earn the mention; don't fake it. → [05 · Authority & Trust](05-authority.md#digital-pr-the-most-actionable-off-page-lever)

### Disambiguation (entity)

Making it unambiguous **which** thing your content refers to (which "Apple," which "Jordan"), so engines and knowledge graphs resolve you to the right [entity](#entity). Achieved through consistent naming, `sameAs` links, and presence in public knowledge graphs. → [05 · Authority & Trust](05-authority.md#entities--knowledge-graphs-becoming-a-thing-the-engine-recognizes)

### Domain Rating (DR)

Ahrefs' 0–100 score of a domain's backlink authority (other tools have equivalents). A useful *correlate* in AI-visibility studies but **not a direct GEO metric** — it measures link authority, and GEO also rewards mentions and corroboration that DR doesn't capture. → [05 · Authority & Trust](05-authority.md#backlinks-vs-brand-mentions-in-the-geo-era)

### Dynamic rendering / prerendering

Serving a bot a fully-rendered HTML version of a page that would otherwise require JavaScript. A workaround for the [JavaScript rendering problem](#javascript-rendering-problem); generally inferior to true [server-side rendering (SSR)](#ssr-server-side-rendering--ssg-static-site-generation) as a durable fix. → [04 · Technical GEO](04-technical.md#rendering-and-crawlability-the-javascript-problem)

---

## E

### E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)

Google's framework (from its Search Quality Rater Guidelines) for content quality signals. In GEO it's reframed as **"E-E-A-T a model can actually read"**: named authors with real bios, visible dates, cited sources, and consistent entity signals — the machine-legible proxies for credibility. ([Google Search Central](https://developers.google.com/search/blog/2022/12/google-raters-guidelines-e-e-a-t)) → [05 · Authority & Trust](05-authority.md)

### ELI5 ("Explain Like I'm 5")

A public Q&A dataset (from Reddit's r/explainlikeimfive) used, among others, to build [GEO-bench](#geo-bench). Named here because it's one of the query sources in the founding paper's benchmark. → [07 · Research & Cases](07-research-cases.md)

### Entity

A distinct, identifiable **thing** — person, product, organization, place, concept — that engines and knowledge graphs recognize and [disambiguate](#disambiguation-entity). GEO wants your brand to be a recognized entity with clear, consistent, corroborated attributes, not just a string of keywords. → [05 · Authority & Trust](05-authority.md#entities--knowledge-graphs-becoming-a-thing-the-engine-recognizes)

### Extractability (liftability)

How easily a **correct, self-contained answer can be lifted** from your content *without* its surrounding context. The central content property GEO optimizes for: clear headings, one idea per section, [answer-first](#answer-first-inverted-pyramid) sentences, and quotable stats all raise it. → [03 · Content Strategy](03-content.md#technique-1--write-extractable-chunks-the-whole-game)

---

## F

### FAQ / FAQPage schema

A Q&A content block, optionally marked up with schema.org `FAQPage`. Useful as an **extractable format** (question-shaped headings map well to real queries), but a cautionary tale on markup: Google **narrowed FAQ rich results** in 2023 and removed them entirely on 7 May 2026, so the *rich-result* payoff is gone even though the *format* still helps extraction. Date any schema claim. ([Search Engine Journal, May 2026](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/)) → [03 · Content](03-content.md) · [04 · Technical](04-technical.md#structured-data-schemaorg-and-json-ld)

### Featured snippet

The boxed direct answer Google lifts atop classic results. The archetypal **AEO** target and a conceptual ancestor of AI-answer extraction: winning it rewards the same [answer-first](#answer-first-inverted-pyramid), self-contained passage writing GEO favors. → [01 · Foundations](01-foundations.md)

### Fluency optimization (GEO method)

One of the [nine methods](#geo-content-methods-the-nine): improving the readability/flow of text. A modest performer; helpful in combination but far behind the [citable trio](#citable-trio). ([Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735)) → [07 · Research & Cases](07-research-cases.md#the-nine-methods-they-tested)

---

## G

### GAIO (Generative AI Optimization)

Informal synonym for GEO. No canonical origin. `⚠️` → see [GEO](#geo-generative-engine-optimization).

### Gemini (Google)

Google's flagship model and assistant app; also the model family behind Google's AI surfaces. Uses **grounding** to attach live retrieved sources to answers. → [02 · The Engines](02-engines.md#google--ai-overviews-ai-mode--gemini)

### Generative engine (GE)

The term from the founding paper: a system that uses generative models (LLMs) to **gather information from multiple sources and synthesize a response** to a query, typically **grounded in retrieved documents with inline attribution**. In 2026 this includes ChatGPT (with search), Perplexity, Google AI Overviews / AI Mode, Gemini, and Copilot. ([Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735)) → [01 · Foundations](01-foundations.md#what-counts-as-a-generative-engine)

### GEO (Generative Engine Optimization)

The practice of structuring, writing, and publishing content so that **generative engines understand it, trust it, and cite or recommend it** when answering a user's question. Coined in the peer-reviewed paper *GEO: Generative Engine Optimization* (Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande), presented at **KDD 2024**, the first controlled study to show content can be deliberately optimized for AI-answer visibility (gains of up to ~40% — the best method on the best metric, on a GPT-3.5-era engine; a ceiling, not an average). ([arXiv:2311.09735](https://arxiv.org/abs/2311.09735) · [DOI:10.1145/3637528.3671900](https://doi.org/10.1145/3637528.3671900)) → [01 · Foundations](01-foundations.md#what-is-geo)

### GEO-bench

The benchmark introduced in the founding paper for evaluating GEO methods: **10,000 queries** (8K train / 1K validation / 1K test) drawn from diverse public datasets (MS MARCO, ORCAS-1, Natural Questions, ELI5, and others), paired with web sources and adapted for generative engines. It let the authors measure visibility changes at scale rather than anecdotally. ([Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735) · [project page & data](https://generative-engines.com/GEO/) · [code](https://github.com/GEO-optim/GEO)) → [07 · Research & Cases](07-research-cases.md#what-they-built-geo-bench-and-two-ways-to-measure-visibility)

### GEO content methods (the nine)

The nine content-rewrite methods the founding paper tested on source pages: **Authoritative, Statistics Addition, Keyword Stuffing, Cite Sources, Quotation Addition, Easy-to-Understand, Fluency Optimization, Unique Words, Technical Terms**. The reliable winners were **Cite Sources, Quotation Addition, and Statistics Addition** (the [citable trio](#citable-trio)); **Keyword Stuffing** was among the *weakest*. Effects are domain-specific — read the percentages as directional. ([Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735)) → [07 · Research & Cases](07-research-cases.md#the-nine-methods-they-tested)

### G-Eval

An LLM-as-judge evaluation method (a model scores outputs against defined criteria). The founding paper uses it to compute the [Subjective Impression](#subjective-impression) metric across ~7 sub-dimensions of prominence. `⚠️ LLM-judge scores are useful but not ground truth — they inherit the judge model's biases.` → [06 · Measurement](06-measurement.md#the-academic-metrics-worth-knowing)

### Google-Extended

Google's **standalone control token** for opting content out of use in **Gemini/Vertex AI model training and grounding**, *without* affecting classic Search ranking. Crucially, **Google-Extended ≠ AI Overviews**: as of 2026, opting out via Google-Extended does not remove you from AI Overviews, which are tied to normal Search indexing (a separate opt-out mechanism applies). Date and verify this control — Google has changed it. ([Google common crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers) · [Search Engine Journal](https://www.searchenginejournal.com/what-opting-out-of-googles-ai-search-features-means-now/584321/)) → [04 · Technical GEO](04-technical.md#google-specific-controls-and-the-ai-overviews-trap)

### Googlebot

Google's primary search crawler. Because AI Overviews and AI Mode are gated on **normal Google indexing**, ordinary Googlebot crawlability is a prerequisite for appearing in Google's AI surfaces — there are "no additional requirements" beyond being indexed and snippet-eligible. ([Google AI features doc](https://developers.google.com/search/docs/appearance/ai-features)) → [04 · Technical GEO](04-technical.md)

### GPTBot

OpenAI's crawler for **collecting training data**. Distinct from **[OAI-SearchBot](#oai-searchbot)** (builds the search index used to cite) and **ChatGPT-User** (live user-triggered fetch); blocking GPTBot affects *training inclusion*, not necessarily *citation*. ([OpenAI bots doc](https://developers.openai.com/api/docs/bots)) → [04 · Technical GEO](04-technical.md#ai-crawlers-the-bots-you-need-to-know)

### Grounding

Tying a model's output to **retrieved source material**, so claims are backed by (and can cite) real documents rather than the model's parametric memory. Grounding is what makes a citation possible; the retrieval that supplies it is [RAG](#rag-retrieval-augmented-generation). → [01 · Foundations](01-foundations.md#key-terminology)

---

## H

### Hallucination

A model output that is **fluent but factually wrong or unsupported** by any source. [Grounding](#grounding) reduces (but does not eliminate) hallucination; for GEO it's a reason clear, verifiable, well-sourced content is safer to cite. → [01 · Foundations](01-foundations.md)

---

## I

### IndexNow

An open protocol (backed by Microsoft/Bing and others) that lets a site **push** notifications of new or updated URLs to participating search engines instead of waiting to be crawled. Useful for GEO because faster Bing indexing feeds ChatGPT/Copilot retrieval. ([indexnow.org](https://www.indexnow.org/)) → [04 · Technical GEO](04-technical.md#sitemaps-feeds-and-freshness)

### Impression

See [AI impression](#ai-impression) for the AI-surface sense; contrast with a classic search impression. The key caution: **an AI impression ≠ a classic impression ≠ a click**. → [06 · Measurement](06-measurement.md)

### Inverted pyramid

See [Answer-first](#answer-first-inverted-pyramid).

---

## J

### JavaScript rendering problem

The finding that **most AI crawlers do not execute JavaScript** — they read the raw HTML your server returns. Content injected client-side (by React/Vue/etc. without SSR) is often invisible to them, so it can't be cited. The fix is [server-side rendering or static generation](#ssr-server-side-rendering--ssg-static-site-generation). ([Vercel, Dec 2024](https://vercel.com/blog/the-rise-of-the-ai-crawler)) → [04 · Technical GEO](04-technical.md#rendering-and-crawlability-the-javascript-problem)

### JSON-LD

A syntax (JavaScript Object Notation for Linked Data) for embedding [structured data](#structured-data-schemaorg--json-ld) in a page, Google's recommended schema format. Note the evidence: at least one large 2026 study found **JSON-LD schema markup had no measurable direct effect on AI citation** — it aids machine understanding and classic rich results, but don't promise a citation lift from it. `⚠️ effect on AI citation is contested.` ([Ahrefs / Search Engine Journal, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/)) → [04 · Technical GEO](04-technical.md#structured-data-schemaorg-and-json-ld)

---

## K

### Keyword stuffing

Cramming a page with target keywords. The caricature of old-school SEO — and, per the founding paper, one of the **least effective** (sometimes counter-productive) [GEO methods](#geo-content-methods-the-nine). The clearest evidence that GEO is not "SEO tricks for robots." ([Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735)) → [01 · Foundations](01-foundations.md#the-nine-methods--and-the-headline-result)

### Knowledge Graph / Knowledge Panel

A structured database of [entities](#entity) and their relationships (Google's Knowledge Graph is the best-known; [Wikidata](#wikidata) is the open one). Becoming a resolved node in these graphs helps engines recognize and correctly attribute your brand; a **Knowledge Panel** is the surfaced card for such an entity. → [05 · Authority & Trust](05-authority.md#entities--knowledge-graphs-becoming-a-thing-the-engine-recognizes)

---

## L

### `lastmod`

The "last modified" timestamp in an XML [sitemap](#sitemap). Keep it **honest** — accurate `lastmod` values help crawlers prioritize genuinely updated pages; inflating them across a whole site erodes trust in the signal. → [04 · Technical GEO](04-technical.md#sitemaps-feeds-and-freshness)

### Liftability

See [Extractability](#extractability-liftability).

### `llms.txt`

A **proposed convention** for a plain-text/Markdown file at your site root that points LLMs to clean, LLM-friendly content — analogous in spirit to `robots.txt` but for *curation*, not blocking. Proposed by **Jeremy Howard (Answer.AI) in September 2024**. `⚠️ Adoption and real-world effect are unproven — as of 2026 no major engine has publicly confirmed using it for retrieval or citation. Treat it as low-cost, low-evidence.` ([llmstxt.org](https://llmstxt.org/)) → [04 · Technical GEO](04-technical.md#llmstxt-the-emerging-and-unproven-convention)

### LLMO (LLM Optimization)

Informal synonym for GEO, emphasizing the model side. No canonical origin. `⚠️` → see [GEO](#geo-generative-engine-optimization).

### Long-tail query

A specific, low-volume, often conversational query. AI engines shift demand toward the long tail (people ask fuller, natural-language questions), so GEO rewards covering the **long tail of specifics** and answering conversational follow-ups on the page. Related: [query fan-out](#query-fan-out-google). → [03 · Content](03-content.md#technique-5--write-for-conversational-long-tail-queries)

---

## M

### Mention

See [Brand mention](#brand-mention-unlinked-mention) and [unlinked mention](#unlinked-mention).

### Model/version drift

When an engine swaps or updates its underlying model/mode, breaking your measured trends because the *system under test changed*, not your content. A reason to **record the model/version** with every measurement and distrust trend lines that span a model change. → [06 · Measurement](06-measurement.md#honest-caveats-on-attribution-read-this-before-quoting-any-number)

### MS MARCO

A large public dataset of real Bing queries and passages, used (among others) as a query source for [GEO-bench](#geo-bench). → [07 · Research & Cases](07-research-cases.md)

---

## N

### Natural Questions

A Google dataset of real search questions with Wikipedia-based answers, another query source for [GEO-bench](#geo-bench). → [07 · Research & Cases](07-research-cases.md)

### Non-determinism (volatility)

The property that the **same prompt can yield different answers and different citations** across runs, users, sessions, and time — because of sampling randomness, personalization, and constant engine changes. It is *the* core measurement challenge in GEO: never measure once; query repeatedly and report distributions, not single results. → [06 · Measurement](06-measurement.md#step-3-dont-measure-once--the-variance-problem)

---

## O

### OAI-SearchBot

OpenAI's crawler that **builds the search index ChatGPT Search cites from**. Distinct from [GPTBot](#gptbot) (training) and **ChatGPT-User** (live fetch): if you want to be *citable* in ChatGPT, this is the token to allow. ([OpenAI bots doc](https://developers.openai.com/api/docs/bots)) → [04 · Technical GEO](04-technical.md#ai-crawlers-the-bots-you-need-to-know)

### Off-page / off-site signals

Everything about your credibility that lives **on other sites**: mentions, co-occurrence, reviews, third-party inclusion, presence in knowledge graphs. In GEO these matter more than in classic SEO because they shape what the model *learned* about you, not just where it can navigate. → [05 · Authority & Trust](05-authority.md#the-off-page-authority-checklist)

### ORCAS

A large click-log query dataset from Bing, used as a query source for [GEO-bench](#geo-bench). → [07 · Research & Cases](07-research-cases.md)

---

## P

### Passage

A short, self-contained span of text — effectively a [chunk](#chunk) as seen from the content side. "Passages beat pages" is the GEO through-line: engines cite passages, so write in liftable passages. → [03 · Content](03-content.md)

### Pay-per-crawl

An emerging model, pioneered by **Cloudflare on 1 July 2025**, where publishers can **charge AI companies per fetch** (and block AI crawlers by default), flipping AI crawling from opt-out to opt-in. Part of the new "citation/crawl economics" reshaping who gets access to content. ([Cloudflare, 2025](https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/) · [Search Engine Land](https://searchengineland.com/cloudflare-to-block-ai-crawlers-by-default-with-new-pay-per-crawl-initiative-457708)) → [04 · Technical GEO](04-technical.md#the-infrastructure-layer-block-by-default-and-pay-per-crawl)

### Perplexity

A standalone AI answer engine built around cited web answers; the founding paper validated GEO methods on it (reporting up to ~37% visibility gains). It operates crawlers ([PerplexityBot](#perplexitybot--perplexity-user), Perplexity-User) and a publisher revenue-share ([Comet Plus](#comet-plus-perplexity)). ([Perplexity bots doc](https://docs.perplexity.ai/guides/bots)) → [02 · The Engines](02-engines.md#perplexity)

### PerplexityBot / Perplexity-User

Perplexity's tokens: **PerplexityBot** indexes the web for Perplexity's answers, while **Perplexity-User** fetches a page in response to a live user request. (Note: Perplexity's crawling has been contested — Cloudflare publicly disputed its bot behavior in 2025.) ([Perplexity bots doc](https://docs.perplexity.ai/guides/bots) · [Search Engine Journal](https://www.searchenginejournal.com/cloudflare-delists-and-blocks-perplexity-from-crawling-websites/552899/)) → [04 · Technical GEO](04-technical.md#ai-crawlers-the-bots-you-need-to-know)

### Position-Adjusted Word Count

One of the two academic visibility metrics in the founding paper: how many words of the answer are **attributed to your source, discounted the later they appear** (exponential decay by citation position). It captures that a source quoted early and at length is "more visible" than one mentioned briefly at the end. ([Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735)) → [06 · Measurement](06-measurement.md#the-academic-metrics-worth-knowing)

### Presence rate (mention rate)

The share of prompts (in your test set) where your brand appears **at all** in the answer. The most basic AI-visibility KPI — the "do you show up?" number, upstream of [citation share](#share-of-voice-sov--citation-share) and [prominence](#prominence). → [06 · Measurement](06-measurement.md#step-4-score-presence-share-prominence-and-sentiment)

### Prominence

**How prominently** you appear when you do — position in the answer, how much of it is attributed to you, whether your facts are [absorbed](#citation-absorption). Distinguishes "mentioned in passing at the end" from "the answer is basically built on you." → [06 · Measurement](06-measurement.md#step-4-score-presence-share-prominence-and-sentiment)

### Prompt set / prompt coverage

The set of test prompts you evaluate AI visibility against, and how **broad and representative** it is. Good [measurement](06-measurement.md) starts here: a set grounded in real user intents (head + long tail + fan-out variants) rather than a handful of flattering queries. → [06 · Measurement](06-measurement.md#step-1-build-a-prompt-set-prompt-coverage)

### Prompt volume

Loosely, how often people ask a given kind of question of an engine — the AI-era analog of search volume. Hard to measure directly (engines don't publish it); estimated from tools and proxies. `⚠️ no authoritative public source — treat vendor "prompt volume" figures as estimates.` → [06 · Measurement](06-measurement.md)

---

## Q

### Q&A / FAQ block

A content pattern of explicit question-and-answer pairs. Highly [extractable](#extractability-liftability) because question-shaped headings map to real user queries; distinct from the *schema markup* of the same name (see [FAQPage schema](#faq--faqpage-schema)). → [03 · Content](03-content.md)

### Query fan-out (Google)

Google's own term for how **AI Mode and AI Overviews** answer a question: they "may use a 'query fan-out' technique — **issuing multiple related searches across subtopics and data sources**," then synthesize across the results. Practical implication: optimize for the *cluster* of sub-questions a topic fans out into, not just your head term. ([Google AI features doc](https://developers.google.com/search/docs/appearance/ai-features)) → [02 · The Engines](02-engines.md#google--ai-overviews-ai-mode--gemini) · [03 · Content](03-content.md#technique-5--write-for-conversational-long-tail-queries)

### Quotation Addition (GEO method)

One of the top-performing [nine methods](#geo-content-methods-the-nine): adding **relevant quotations from credible sources**. Part of the [citable trio](#citable-trio); a leading driver of visibility gains in the founding paper. ([Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735)) → [07 · Research & Cases](07-research-cases.md#the-nine-methods-they-tested)

---

## R

### RAG (Retrieval-Augmented Generation)

The architecture where an engine **retrieves relevant documents and conditions its generated answer on them**, rather than answering from the model's memory alone. It's the mechanism most consumer AI search relies on, and the reason being *retrievable* (and *extractable*) is the whole GEO game. → [01 · Foundations](01-foundations.md#how-a-generative-engine-turns-your-page-into-a-cited-answer)

### Referrer leakage

The HTTP `Referer` header tells your analytics where a visit came from. **Referrer leakage** is the core AI-attribution problem: many AI engines pass **no or inconsistent referrer**, so [AI referral traffic](#ai-referral-traffic) is under- or mis-counted in standard analytics — requiring custom channel groups and other workarounds. → [06 · Measurement](06-measurement.md#the-core-problem-referrer-leakage)

### Retrieval / retrieval-time

The step where an engine fetches candidate sources for *this specific query* (the "R" in [RAG](#rag-retrieval-augmented-generation)). **Retrieval-time** attribution — being pulled in and cited live — is the main lever GEO targets, as opposed to [training-time](#training-time-vs-retrieval-time-attribution) presence. → [05 · Authority & Trust](05-authority.md#being-present-in-the-corpora-training-vs-retrieval)

### `robots.txt`

The long-standing site file (standardized as **RFC 9309**) that tells crawlers which paths they may fetch, **per user-agent**. In the AI era it's how you allow/deny specific AI bots — but it is a **request, not a lock**: compliance is voluntary and some crawlers ignore or misreport it. ([RFC 9309](https://www.rfc-editor.org/info/rfc9309/)) → [04 · Technical GEO](04-technical.md#robotstxt-and-ai-crawler-control)

### RSL (Really Simple Licensing)

An emerging standard for publishers to declare **licensing/compensation terms** for AI use of their content (part of the same wave as [pay-per-crawl](#pay-per-crawl)). `⚠️ early-stage — verify current adopters and mechanics before relying on it.` ([CJR on AI licensing, 2025](https://www.cjr.org/analysis/reddit-winning-ai-licensing-deals-openai-google-gemini-answers-rsl.php)) → [04 · Technical GEO](04-technical.md)

### RSS / Atom feed

A structured, machine-readable feed of a site's latest content. Alongside sitemaps, feeds help engines discover fresh content quickly — a freshness signal for retrieval. → [04 · Technical GEO](04-technical.md#sitemaps-feeds-and-freshness)

---

## S

### Schema.org / structured data

See [Structured data](#structured-data-schemaorg--json-ld).

### SEO (Search Engine Optimization)

Optimizing to **rank a page** in a list of search results. GEO's older sibling: overlapping foundations (crawlability, authority, relevance) but a different win condition. Good SEO is largely a **prerequisite** for good GEO, not a rival to it. → [01 · Foundations](01-foundations.md#geo-vs-seo-vs-aeo--and-the-rest-of-the-acronym-soup)

### SGE (Search Generative Experience)

Google's **2023 experimental name** for what launched broadly as [AI Overviews](#ai-overview--ai-overviews-aio-google). Mostly of historical interest now; you'll still see it in older sources. → [02 · The Engines](02-engines.md)

### Share of Voice (SoV) / citation share

How often your content is cited across a set of prompts **relative to competitors** — your slice of the total citations in a category. A core GEO KPI: presence answers "do you show up?", share answers "what fraction of the answers are you?". Sometimes surfaced by tools as "AI Share of Voice." → [06 · Measurement](06-measurement.md#step-4-score-presence-share-prominence-and-sentiment)

### Sitemap

An XML file listing your URLs (with metadata like [`lastmod`](#lastmod)) to help crawlers discover and prioritize content. A complete, honest sitemap is basic [crawlability](#crawlability) hygiene for AI bots as much as for search. → [04 · Technical GEO](04-technical.md#sitemaps-feeds-and-freshness)

### Snippet directives

`robots` meta/HTTP directives that control how much of your text an engine may show — `nosnippet`, `max-snippet`, `noindex`, and Google's newer AI-specific opt-out toggle. They're a double-edged tool: restricting snippets can also **restrict your eligibility to be quoted** in AI answers, so use deliberately and date the behavior. ([Search Engine Land, 2026](https://searchengineland.com/google-ai-opt-out-feature-competitors-480375)) → [04 · Technical GEO](04-technical.md#snippet-directives--and-the-new-opt-out-toggle)

### SSR (server-side rendering) / SSG (static site generation)

Serving fully-formed **HTML from the server** (SSR) or pre-building static HTML pages (SSG), so content is present in the raw response. The recommended fix for the [JavaScript rendering problem](#javascript-rendering-problem): most AI crawlers read HTML and don't run JS, so client-rendered content is invisible to them. → [04 · Technical GEO](04-technical.md#the-fix-server-side-rendering-or-static-generation)

### Statistics Addition (GEO method)

One of the top-performing [nine methods](#geo-content-methods-the-nine): adding **relevant, concrete statistics**. Part of the [citable trio](#citable-trio); a leading driver of visibility gains — quantified claims are more quotable and read as more credible. ([Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735)) → [07 · Research & Cases](07-research-cases.md#the-nine-methods-they-tested)

### Structured data (schema.org / JSON-LD)

Machine-readable markup describing what a page is *about* (an article, product, person, FAQ), typically written in [JSON-LD](#json-ld) using the **schema.org** vocabulary. It aids entity understanding and classic rich results; its **direct** effect on AI *citation* is contested (at least one large 2026 study found none). Add correct schema for understanding — don't promise a citation lift from it. `⚠️` ([schema.org](https://schema.org/) · [Google intro to structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)) → [04 · Technical GEO](04-technical.md#structured-data-schemaorg-and-json-ld)

### Subjective Impression

The second academic visibility metric in the founding paper: an **LLM-judged composite** (via [G-Eval](#g-eval)) across ~7 sub-dimensions — relevance, influence, uniqueness, position, count, click-likelihood, diversity — capturing *qualitative* prominence a raw word count misses. ([Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735)) → [06 · Measurement](06-measurement.md#the-academic-metrics-worth-knowing)

---

## T

### Technical Terms (GEO method)

One of the [nine methods](#geo-content-methods-the-nine): adding domain-specific terminology. A modest, domain-dependent performer. ([Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735)) → [07 · Research & Cases](07-research-cases.md#the-nine-methods-they-tested)

### TTFB (Time to First Byte)

How quickly your server starts responding. For AI crawlers, **fast, reliable HTML delivery** (low TTFB, few errors) matters more than cosmetic front-end speed — a bot that times out or gets a 5xx simply doesn't ingest the page. → [04 · Technical GEO](04-technical.md#page-speed-and-crawl-efficiency)

### Training corpus / training data

The body of text a model was trained on. Some sources are structurally **over-represented** — e.g. GPT-3 sampled **Wikipedia ~3.4×** its token share ([Brown et al., 2020](https://arxiv.org/abs/2005.14165)) — which shapes a model's default "priors" about who is authoritative. Distinct from what an engine *retrieves* at answer time. → [07 · Research & Cases](07-research-cases.md#why-some-sources-dominate-the-training-corpus-papers)

### Training-time vs. retrieval-time attribution

The two distinct ways an engine can surface your brand: because your content was in its **training data** (baked into the model's parameters, hard to influence quickly) or because it **retrieved your live page** to answer *this* query (influenceable now — the main GEO lever). Conflating them leads to bad strategy; most actionable GEO is retrieval-time. → [05 · Authority & Trust](05-authority.md#being-present-in-the-corpora-training-vs-retrieval)

---

## U

### Unlinked mention

A [brand mention](#brand-mention-unlinked-mention) with **no hyperlink** back to you. Because LLMs learn from text [co-occurrence](#co-occurrence-branded-co-occurrence) rather than a link graph, unlinked mentions on trusted pages carry real GEO weight — so count them as wins, unlike in classic link-based SEO. → [05 · Authority & Trust](05-authority.md#backlinks-vs-brand-mentions-in-the-geo-era)

### User-agent

The identifier a crawler sends in its HTTP request (e.g. `GPTBot`, `PerplexityBot`, `Google-Extended`, `ClaudeBot`). It's how you grant or deny access **per bot and per purpose** in [`robots.txt`](#robotstxt). Tokens, purposes, and controls change — always confirm against the vendor's official docs and **date** the claim. See the quick-reference table below. → [04 · Technical GEO](04-technical.md#ai-crawlers-the-bots-you-need-to-know)

### AI crawler user-agents (quick reference)

Definitions only — the canonical **per-purpose control matrix** (what to allow vs. block, and why) lives in **[04 · Technical GEO](04-technical.md#reference-table--major-ai-crawlers-as-of-2026-08)**. Purposes change; verify against each vendor's doc and date your `robots.txt`. *As of 2026-08.*

| Token | Operator | Primary purpose | Official doc |
|---|---|---|---|
| `GPTBot` | OpenAI | Training-data collection | [OpenAI](https://developers.openai.com/api/docs/bots) |
| `OAI-SearchBot` | OpenAI | Builds the search index ChatGPT cites from | [OpenAI](https://developers.openai.com/api/docs/bots) |
| `ChatGPT-User` | OpenAI | Live, user-triggered page fetch | [OpenAI](https://developers.openai.com/api/docs/bots) |
| `PerplexityBot` | Perplexity | Indexing for Perplexity answers | [Perplexity](https://docs.perplexity.ai/guides/bots) |
| `Perplexity-User` | Perplexity | Live, user-triggered fetch | [Perplexity](https://docs.perplexity.ai/guides/bots) |
| `ClaudeBot` | Anthropic | General crawl (incl. training-related) | [Anthropic](https://support.claude.com/en/articles/8896518) |
| `Claude-SearchBot` | Anthropic | Builds Claude's search index | [Anthropic](https://support.claude.com/en/articles/8896518) |
| `Claude-User` | Anthropic | Live, user-triggered fetch | [Anthropic](https://support.claude.com/en/articles/8896518) |
| `Googlebot` | Google | Search index (gates AI Overviews/AI Mode eligibility) | [Google](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers) |
| `Google-Extended` | Google | **Opt-out control** for Gemini training/grounding (≠ AI Overviews) | [Google](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers) |
| `Bingbot` | Microsoft | Search index (powers ChatGPT Search & Copilot) | [Microsoft](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0) |
| `CCBot` | Common Crawl | Open web crawl feeding many training sets | [Common Crawl](https://commoncrawl.org/ccbot) |
| `Amazonbot` | Amazon | Crawl for Amazon/Alexa AI | [Amazon](https://developer.amazon.com/amazonbot) |

---

## V

### Volatility

See [Non-determinism](#non-determinism-volatility).

---

## W

### Wikidata

The **open, structured knowledge base** (sister project to Wikipedia) that many engines and knowledge graphs draw on to recognize and disambiguate [entities](#entity). Being a well-formed, correct Wikidata item is a consensus GEO practice for entity clarity — but **don't fabricate notability** to get one. → [05 · Authority & Trust](05-authority.md#how-to-build-entity-clarity-consensus-practices)

### Wikipedia (up-weighting)

Wikipedia is structurally privileged in AI systems: heavily **over-sampled in training** (GPT-3 sampled it ~3.4× its token share — [Brown et al., 2020](https://arxiv.org/abs/2005.14165)) and dominant in the indexes engines retrieve from. This is *why* Wikipedia-corroborated facts surface so often — and why earning legitimate Wikipedia/Wikidata presence (without astroturfing) helps. → [07 · Research & Cases](07-research-cases.md#why-some-sources-dominate-the-training-corpus-papers)

---

## Z

### Zero-click search

A search that **ends without a click** to an external site, because the answer was shown in place (a featured snippet, an AI Overview, a chat answer). The structural shift behind GEO's importance: in early 2026, ~**68% of U.S. Google searches** ended click-free ([SparkToro/Similarweb, 2026](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/)). If you're not *in* the answer, the zero-click majority never sees you. → [01 · Foundations](01-foundations.md#why-it-matters-now-2026)

---

## A note on evidence tiers

Several entries reference how strongly a claim is supported. The handbook uses a consistent scale, defined in full in **[07 · Research & Cases](07-research-cases.md#how-to-read-the-evidence-in-this-handbook)**:

| Tier | Meaning |
|---|---|
| **Demonstrated** | Shown in a controlled/peer-reviewed study or measured experiment |
| **Observed at scale** | Large correlational/industry dataset — real but not proof of cause |
| **Behavioral** | Measured human behavior (e.g. click studies) |
| **Consensus / plausible** | Reasoned from how the systems work; not isolated in a public test |
| **Documented** | A verifiable business/announcement fact |
| **Anecdotal** | A single reported result |

When an entry says a tactic's effect is "contested" or flags `⚠️`, it means the claim sits low on this scale — treat it as a hypothesis to measure, not a law.

---

## Sources

Primary and origin sources for the definitions above. All links verified as of **2026-08**. Where an entry cites a vendor, that's noted inline (vendors have incentives).

**Founding research & benchmark**
- Aggarwal, P., Murahari, V., Rajpurohit, T., Kalyan, A., Narasimhan, K., & Deshpande, A. (2024). **GEO: Generative Engine Optimization.** *KDD 2024.* [arXiv:2311.09735](https://arxiv.org/abs/2311.09735) · [DOI:10.1145/3637528.3671900](https://doi.org/10.1145/3637528.3671900) · [project page & data](https://generative-engines.com/GEO/) · [code](https://github.com/GEO-optim/GEO)
- Brown, T. et al. (2020). **Language Models are Few-Shot Learners** (GPT-3; training-mix weighting). [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- Dodge, J. et al. (2021). **Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus** (C4). *EMNLP 2021.* [arXiv:2104.08758](https://arxiv.org/abs/2104.08758)

**Standards, conventions & controls**
- **RFC 9309 — Robots Exclusion Protocol.** [rfc-editor.org](https://www.rfc-editor.org/info/rfc9309/)
- **`llms.txt` proposal** (Jeremy Howard / Answer.AI). [llmstxt.org](https://llmstxt.org/)
- **IndexNow.** [indexnow.org](https://www.indexnow.org/)
- **schema.org** and **Google — intro to structured data.** [schema.org](https://schema.org/) · [developers.google.com](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- **Google — Search Quality Rater Guidelines & E-E-A-T.** [developers.google.com](https://developers.google.com/search/blog/2022/12/google-raters-guidelines-e-e-a-t)

**Engines & crawler docs (vendor)**
- **Google — AI features (Overviews / AI Mode, "query fan-out", eligibility).** [developers.google.com](https://developers.google.com/search/docs/appearance/ai-features) · **Google common crawlers.** [developers.google.com](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- **OpenAI — bots (GPTBot, OAI-SearchBot, ChatGPT-User).** [developers.openai.com](https://developers.openai.com/api/docs/bots)
- **Perplexity — bots.** [docs.perplexity.ai](https://docs.perplexity.ai/guides/bots)
- **Anthropic — Claude crawler controls.** [support.claude.com](https://support.claude.com/en/articles/8896518)
- **Microsoft — Copilot Search in Bing** and **AI Performance in Bing Webmaster Tools.** [blogs.bing.com (Copilot)](https://blogs.bing.com/search/April-2025/Introducing-Copilot-Search-in-Bing) · [blogs.bing.com (AI Performance)](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)

**Industry data & context**
- **SparkToro / Similarweb (2026)** — zero-click majority. [sparktoro.com](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/)
- **Pew Research (2025)** — AI summaries reduce clicks. [pewresearch.org](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)
- **Ahrefs (2025–2026)** — AI-search myths & brand-visibility correlations (schema/no-effect, mentions). [searchenginejournal.com](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/) · [ahrefs.com](https://ahrefs.com/blog/ai-brand-visibility-correlations/)
- **Vercel (Dec 2024)** — AI crawlers don't run JavaScript. [vercel.com](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- **Cloudflare (2025)** — block-by-default & Pay-Per-Crawl. [cloudflare.com](https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/) · [Search Engine Land](https://searchengineland.com/cloudflare-to-block-ai-crawlers-by-default-with-new-pay-per-crawl-initiative-457708)
- **GrowthX (2026)** — branded co-occurrence. [growthx.ai](https://growthx.ai/learn/branded-co-occurrence-ai-search)
- **CJR (2025)** — AI licensing deals (Reddit, RSL). [cjr.org](https://www.cjr.org/analysis/reddit-winning-ai-licensing-deals-openai-google-gemini-answers-rsl.php)

> **Missing a term, or spot a definition that's drifted?** Add it in the right letter section with a one- to three-sentence, neutral definition, cite the origin if the term comes from a specific paper/standard/vendor, and flag anything unproven with `⚠️ needs verification`. See [CONTRIBUTING.md](../CONTRIBUTING.md). The rule that governs this handbook governs this glossary too: **a real source, or an honest flag — never an invented fact.**
