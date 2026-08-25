# 01 · Foundations

> Part of **[The GEO Handbook](../README.md)** — a free, community-maintained reference on Generative Engine Optimization. New to the project? Start at the [README](../README.md). Terms are defined once in the [Glossary](09-glossary.md).
>
> *Last substantive review: 2026-08. Time-sensitive figures are dated inline; verify anything marked `⚠️`.*

This is the ground floor. By the end of this chapter you should be able to say, precisely, **what GEO is, where it came from, how it differs from SEO and AEO, why it matters right now, and roughly how a generative engine turns a web page into a cited sentence** in an answer.

---

## TL;DR

- **GEO (Generative Engine Optimization)** is the practice of structuring, writing, and publishing content so that **generative AI engines** — ChatGPT, Perplexity, Google AI Overviews / AI Mode, Gemini, Copilot — understand it, trust it, and **cite or recommend it** when answering a user's question.
- The term was **coined in a peer-reviewed 2023/2024 paper**, *"GEO: Generative Engine Optimization"* (Aggarwal et al.), presented at **KDD 2024**. It was the first controlled study to show that content can be deliberately optimized for visibility inside AI answers — reporting gains of **up to ~40%** ([arXiv:2311.09735](https://arxiv.org/abs/2311.09735)).
- **SEO gets a page ranked; GEO gets a passage quoted.** They share foundations (crawlability, authority, relevance) but optimize for different outcomes. **AEO (Answer Engine Optimization)** is a closely related, often-overlapping term — usage varies (see [below](#geo-vs-seo-vs-aeo-and-the-rest-of-the-acronym-soup)).
- **Why now:** search is shifting from "a list of links" to "one synthesized answer." As of early **2026, ~68% of U.S. Google searches end without a click** to an outside site ([SparkToro/Similarweb, 2026](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/)). If your content isn't *in* the answer, it may not be seen at all.
- The counter-intuitive finding at the heart of GEO: the tactics that win are **citing sources, adding statistics, and quoting credible authorities** — *not* keyword stuffing.

---

## What is GEO?

> **Generative Engine Optimization (GEO)** is the practice of structuring, writing, and publishing content so that generative AI engines understand it, trust it, and **cite or recommend it** when they answer a user's question.

Where classic search returns a ranked *list of links* and lets the user choose, a **generative engine** composes a single, synthesized answer in natural language — and increasingly backs that answer with a handful of **inline citations**. GEO's target outcome is not "rank #1 on a results page." It is **"be one of the sources the model quotes, links, or names inside the answer."**

A useful one-line contrast:

> **SEO optimizes for *ranking a page*. GEO optimizes for *being quoted inside the answer*.**

### What counts as a "generative engine"?

The founding paper defines a **generative engine (GE)** as a system that uses generative models (LLMs) to *gather information from multiple sources and synthesize a response* to a query, typically **grounded in retrieved documents with inline attribution** ([Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735)). In 2026 that includes, among others:

- **ChatGPT** (with web search / browsing)
- **Perplexity**
- **Google AI Overviews** and **AI Mode**
- **Google Gemini**
- **Microsoft Copilot**

These engines differ in *how* they retrieve and cite — that comparison lives in **[02 · The Engines](02-engines.md)**. What they share is the shape of the problem GEO addresses: your content is no longer competing to be *clicked*; it is competing to be *ingested and repeated*.

---

## Where GEO came from: the founding paper

GEO is not a marketing coinage — it originates in academic research, which is part of why this handbook treats the paper as its anchor.

### The paper at a glance

| Field | Detail |
|---|---|
| **Title** | *GEO: Generative Engine Optimization* |
| **Authors** | Pranjal Aggarwal, Vishvak Murahari (equal contribution), Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, Ameet Deshpande |
| **Affiliations** | **Princeton University** (Murahari, Narasimhan, Deshpande); **IIT Delhi** (Aggarwal); independent researchers (Rajpurohit, Kalyan) |
| **First posted** | arXiv v1, **16 Nov 2023**; final v3, 28 Jun 2024 |
| **Published** | **KDD 2024** — 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Barcelona |
| **Links** | [arXiv:2311.09735](https://arxiv.org/abs/2311.09735) · [PDF](https://arxiv.org/pdf/2311.09735) · [DOI:10.1145/3637528.3671900](https://doi.org/10.1145/3637528.3671900) · [project page + data](https://generative-engines.com/GEO/) · [Princeton listing](https://collaborate.princeton.edu/en/publications/geo-generative-engine-optimization/) |

> The paper is frequently called "the Princeton GEO study." That is a fair shorthand — three of the six authors were at Princeton and the lead author (Aggarwal) was at IIT Delhi. It is *not* a Google or OpenAI paper.

### What the paper actually did

The authors argue that traditional SEO does **not** transfer to generative engines: an LLM "is not limited to keyword matching," and reads both source documents and the query with a more nuanced understanding, so *new techniques are needed* ([Aggarwal et al., 2024, §2.2](https://arxiv.org/abs/2311.09735)). To study those techniques rigorously, they built two things:

1. **GEO-bench** — a benchmark of **10,000 queries** drawn from diverse domains and public datasets (e.g., MS MARCO, ORCAS, Natural Questions, ELI5), paired with web sources, and adapted specifically for generative engines. This let them measure visibility changes at scale rather than anecdotally.
2. **Visibility ("impression") metrics** designed for answers rather than link lists — because in a synthesized paragraph, "rank #1" is not well-defined. Two metrics do most of the work:

| Metric | What it measures | Intuition |
|---|---|---|
| **Position-Adjusted Word Count** | How many words of the answer are attributed to your source, **discounted the later they appear** (an exponential decay by citation position) | A source quoted early and at length is "more visible" than one mentioned briefly at the end |
| **Subjective Impression** | An LLM-judged composite (via G-Eval) across ~7 sub-dimensions — relevance, influence, uniqueness, position, count, click-likelihood, diversity | Captures *qualitative* prominence a raw word count misses |

They then applied **nine content-rewrite methods** to source pages and measured the effect on those metrics.

### The nine methods — and the headline result

The nine methods tested ([Aggarwal et al., 2024, §2.2.2](https://arxiv.org/abs/2311.09735)):

`Authoritative` · `Statistics Addition` · `Keyword Stuffing` · `Cite Sources` · `Quotation Addition` · `Easy-to-Understand` · `Fluency Optimization` · `Unique Words` · `Technical Terms`

The central finding, in the authors' own words, is that GEO methods **"can boost visibility by up to 40% in generative engine responses,"** with the biggest, most reliable gains coming from a specific cluster:

> "…including citations, quotations from relevant sources, and statistics can significantly boost source visibility, with an increase of **over 40% across various queries**." — *Aggarwal et al., 2024, §1*

The three top methods were **Cite Sources, Quotation Addition, and Statistics Addition** — all of which *add concrete, verifiable material* to the page. Meanwhile **Keyword Stuffing** — the caricature of old-school SEO — was among the weakest and, in places, counter-productive. The lesson is not subtle:

> **Generative engines reward content that reads like a credible, evidence-backed source. They are largely unmoved by keyword density.**

The authors also validated the approach outside their own test harness, reporting **visibility improvements of up to 37% on Perplexity.ai**, a live generative engine ([Aggarwal et al., 2024, §1](https://arxiv.org/abs/2311.09735)).

> ⚠️ **Read the numbers as directional, not eternal.** These results are from 2023–24 experiments on the engines of that moment. Exact per-method percentages vary by domain (the paper stresses domain-specific effects), and engines have changed since. The *robust* takeaway — evidence and credibility beat keyword tricks — has held up in later work, but treat any single percentage as "as measured then," and see **[07 · Research & Case Studies](07-research-cases.md)** for replications and newer studies.

---

## How a generative engine turns your page into a cited answer

You cannot optimize for a black box you can't picture. Here is the mental model — deliberately simplified — of the pipeline most consumer AI search runs, drawn from the paper's formulation of a generative engine and from how these systems are documented to work ([Aggarwal et al., 2024, §2.1](https://arxiv.org/abs/2311.09735)):

1. **Query reformulation.** The engine rewrites the user's question into one or more search queries an underlying search index can serve.
2. **Retrieval.** A search backend returns a set of candidate sources (this is the **RAG** — *retrieval-augmented generation* — step). Being *retrievable* here is the price of entry: if the engine's crawler can't access or make sense of your page, nothing downstream matters. (See **[04 · Technical GEO](04-technical.md)**.)
3. **Selection / chunking.** The engine picks the passages ("**chunks**") it will actually use. This is why GEO cares about **chunk-level extractability**, not just whole-page quality: a single self-contained, quotable passage can get lifted even from a page that wouldn't "rank."
4. **Synthesis.** The LLM composes an answer grounded in the selected passages.
5. **Citation.** The engine attributes some sentences to some sources — the citation is your visible payoff.

```
User question
   │
   ▼
[1] Reformulate → [2] Retrieve (RAG) → [3] Select/chunk → [4] Synthesize → [5] Cite
                                          ▲
                              your content competes HERE
                       (retrievable? extractable? credible? quotable?)
```

Two consequences fall out of this model, and they shape the rest of the handbook:

- **Extractability > page-level ranking.** The unit of competition is the *passage*, not the URL. Content that packages a correct, self-contained answer into a clean chunk (a clear heading, a direct claim, a stat, a source) is easier to lift. This is the through-line of **[03 · Content Strategy](03-content.md)**.
- **Credibility is a machine signal, not just a human one.** The paper's winning methods (cite, quote, quantify) are exactly the signals an LLM uses to judge whether a passage is trustworthy enough to repeat. Authority and trust get their own chapter, **[05 · Authority & Trust](05-authority.md)**.

---

## GEO vs. SEO vs. AEO — and the rest of the acronym soup

The field is young and its vocabulary is unsettled. You will see **GEO**, **AEO**, **AIO** (AI Optimization), **LLMO** (LLM Optimization), **GAIO**, and "AI SEO" used — sometimes as synonyms, sometimes with fine distinctions. The three that matter most:

| | **SEO** (Search Engine Optimization) | **AEO** (Answer Engine Optimization) | **GEO** (Generative Engine Optimization) |
|---|---|---|---|
| **Optimizes for** | Ranking a page in a list of results | Being the source of a **direct answer** (featured snippets, knowledge panels, voice, AI Overviews) | Being **cited / quoted / recommended inside a generative, synthesized answer** |
| **Target surface** | The classic blue-links SERP | Answer boxes, zero-click surfaces, assistants | ChatGPT, Perplexity, AI Overviews / AI Mode, Gemini, Copilot |
| **Win condition** | User clicks your #1 result | Your content *is* the answer shown | The model names/links you as a source |
| **Signature tactics** | Keywords, links, technical SEO, page speed | Structured data, concise Q&A formatting, snippet-friendly structure | Citations, statistics, quotable passages, entity clarity, off-site authority |
| **Origin of term** | 1990s–2000s SEO industry | Marketing/SEO industry, term usage varies `⚠️` | Coined in [Aggarwal et al., 2024](https://arxiv.org/abs/2311.09735) |

### How they relate (the honest version)

These are **not** three competing strategies you pick between. The prevailing 2026 view among practitioners is that they **layer**: SEO builds the crawlable, authoritative foundation; AEO structures individual pages to be answer-ready; GEO builds the wider credibility and extractability that gets a brand *named inside an AI response*. Generative engines lean on many of the **same authority and relevance signals** that classic search does, so good SEO is largely a prerequisite for good GEO rather than a rival to it.

> **On "AEO" specifically:** AEO and GEO overlap heavily and are often used interchangeably. Some practitioners reserve **AEO** for *answer surfaces on traditional search* (featured snippets, Google's AI Overviews) and **GEO** for *standalone LLM assistants* (ChatGPT, Perplexity); others use one term for everything. **There is no single authoritative definition of AEO** — unlike GEO, it wasn't introduced by a specific paper. `⚠️ needs verification` on any claim about who coined "AEO" or a canonical boundary between the two. This handbook uses **GEO** as the umbrella term and notes AEO where the distinction is load-bearing.

---

## Why it matters now (2026)

The strategic case for GEO rests on one structural shift: **search is moving from "click to a site" to "read the answer in place."** The evidence, dated:

- **Most searches no longer produce a click to an outside site.** In the first four months of **2026, 68.01% of U.S. Google searches ended without a click** to a non-Google web property, per SparkToro's analysis of Similarweb clickstream data — up from ~45% a decade earlier ([SparkToro, 2026](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/); [Search Engine Land, 2026](https://searchengineland.com/google-zero-click-searches-2026-study-479717)). This "**zero-click**" majority is the backdrop for everything that follows.
- **AI Overviews depress click-through when they appear.** When Google shows an AI Overview, click-through rates to results drop by close to 60%, and these overviews appear on a large and growing share of searches ([SparkToro, 2026](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/)). Their prevalence has been volatile — Semrush's study of 10M+ keywords found AI Overviews on ~6.5% of queries in Jan 2025, peaking near 24.6% in Jul 2025, then settling around 15–16% by late 2025 as Google calibrated where to show them ([Search Engine Land on Semrush data, 2025](https://searchengineland.com/google-ai-overviews-surge-pullback-data-466314)).
- **Standalone AI answer engines are now mainstream.** OpenAI has reported ChatGPT surpassing **800 million weekly active users** (2025), and Google reported at I/O 2026 that **AI Mode passed 1 billion monthly users**. `⚠️ Exact, current user counts move monthly and are often reported via secondary trackers — verify the latest figure against the vendor's own announcement before quoting a specific number.` The *direction* — hundreds of millions of people now getting answers from generative engines — is not in dispute.

Put together: a growing share of the audience that classic SEO used to deliver never reaches your site, because the engine answered them directly. **GEO is how you stay present in that answer.** It doesn't replace SEO — it addresses the traffic and visibility SEO alone no longer captures.

> **A caveat for balance.** Some of the sharpest zero-click and AI-Overview statistics come from vendors and tools with a stake in the "AI is changing search" narrative. The underlying trend is well-corroborated across independent clickstream datasets, but treat any single dramatic number as *directional*, check its date, and prefer primary sources — a standard this handbook holds itself to. See [Measurement](06-measurement.md) for how to quantify this for *your own* content rather than relying on headline stats.

---

## Key terminology

Full definitions live once in the **[Glossary](09-glossary.md)** — link there, don't re-define. The essential handful to carry into the rest of the handbook:

- **Generative engine** — an AI system (LLM + retrieval) that synthesizes an answer to a query, usually grounded in retrieved sources with inline citations. *(Term from the founding paper.)*
- **RAG (Retrieval-Augmented Generation)** — the architecture where the engine retrieves relevant documents and conditions its generated answer on them. The mechanism most consumer AI search relies on.
- **Grounding** — tying the model's output to retrieved source material, so claims are backed by (and can cite) real documents.
- **Chunk** — a passage-sized unit of content a retrieval system indexes and an engine may lift into an answer. GEO optimizes at the *chunk* level.
- **Extractability** — how easily a correct, self-contained answer can be lifted from your content *without* its surrounding context.
- **Citation** — a source an engine links or references in its answer. Being cited is GEO's primary target outcome.
- **Entity** — a distinct, identifiable thing (person, product, org, concept) that engines and knowledge graphs recognize and disambiguate.
- **Share of voice / citation share** — how often your content is cited across a set of prompts relative to competitors; a core [measurement](06-measurement.md) metric.
- **Zero-click search** — a search that ends without the user clicking through to an external site because the answer was shown in place.

---

## Common misconceptions

Clearing these up early saves a lot of wasted effort:

- **"GEO replaces SEO."** No. GEO builds *on* SEO's foundation — crawlability, authority, and relevance are shared inputs. A page an AI crawler can't fetch can't be cited. They layer; they don't compete.
- **"It's just keyword stuffing for robots."** The opposite. The founding paper found keyword stuffing among the *least* effective methods; evidence, statistics, and credible quotations won. See [the results above](#the-nine-methods--and-the-headline-result).
- **"GEO means gaming or tricking the model."** Deliberately manipulating an engine's answer (e.g., adversarial or deceptive text injected to hijack citations) is a documented risk, but it is a *different, riskier* activity than legitimate GEO — and it invites detection and penalties. The ethics and manipulation-vs-optimization line are covered in **[08 · Future & Ethics](08-future-ethics.md)**.
- **"There's one fixed GEO checklist."** Engines change almost weekly, and effects are domain-specific. Treat tactics as hypotheses to *measure*, not laws. That's why this handbook [updates weekly](../updates/README.md) and why every claim is dated.
- **"A percentage from the paper is a guarantee."** The "up to 40%" figure is a *measured average under specific 2023–24 conditions*, not a promise for your site today.

---

## Where to go next

- **[02 · The Engines](02-engines.md)** — how ChatGPT, Perplexity, AI Overviews / AI Mode, Gemini, and Copilot each retrieve and cite, and where they differ.
- **[03 · Content Strategy](03-content.md)** — writing extractable, citable, chunk-friendly content (the practical application of the paper's winning methods).
- **[04 · Technical GEO](04-technical.md)** — making your content retrievable by AI crawlers in the first place.
- **[07 · Research & Case Studies](07-research-cases.md)** — the founding paper in depth, replications, and newer literature.
- **[Glossary](09-glossary.md)** — every term, defined once.

---

## Sources

Primary source (the founding paper) first, then the current-state data used in "Why it matters now." All links verified as of 2026-08.

- Aggarwal, P., Murahari, V., Rajpurohit, T., Kalyan, A., Narasimhan, K., & Deshpande, A. (2024). **GEO: Generative Engine Optimization.** *KDD 2024.* [arXiv:2311.09735](https://arxiv.org/abs/2311.09735) · [PDF](https://arxiv.org/pdf/2311.09735) · [DOI:10.1145/3637528.3671900](https://doi.org/10.1145/3637528.3671900) · [project page & data](https://generative-engines.com/GEO/) · [Princeton listing](https://collaborate.princeton.edu/en/publications/geo-generative-engine-optimization/)
- SparkToro / Rand Fishkin (2026). **In 2026, Less than One Third of Google Searches Still Send a Click** (Similarweb clickstream, Jan–Apr 2026). [sparktoro.com](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/)
- Search Engine Land (2026). **Google zero-click searches reach 68% in early 2026: Study.** [searchengineland.com](https://searchengineland.com/google-zero-click-searches-2026-study-479717)
- Search Engine Land (2025), reporting Semrush's 10M-keyword study. **Google AI Overviews surged in 2025, then pulled back.** [searchengineland.com](https://searchengineland.com/google-ai-overviews-surge-pullback-data-466314)
- `llms.txt` proposal (referenced in later chapters): [llmstxt.org](https://llmstxt.org/)

> **Found an error, a dead link, or a newer figure?** This chapter is meant to be corrected. See [CONTRIBUTING.md](../CONTRIBUTING.md) — the one rule is that every claim carries a real source or an honest `⚠️ needs verification` flag.
