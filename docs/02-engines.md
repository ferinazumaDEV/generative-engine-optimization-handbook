# 02 · The AI Engines

> Part of **[The GEO Handbook](../README.md)** — a free, community-maintained reference on Generative Engine Optimization. New to GEO? Start with **[01 · Foundations](01-foundations.md)**. Every claim here is dated and sourced; when an engine's behavior shifts, it belongs in the **[weekly updates](../updates/README.md)**.
>
> **Last full review: 2026-08.** Engine behavior changes almost weekly — treat any dated claim as a snapshot, and re-verify before you bet a strategy on it.

---

## TL;DR

- **There is no single "AI search."** Each engine has its own index, its own crawlers, its own way of choosing and displaying citations, and its own publisher controls. Optimizing for one is not optimizing for all.
- **Two jobs, two kinds of bot.** Almost every vendor now runs *separate* crawlers for **model training** and for **live search/answers**. Blocking the training bot does **not** hurt your answer visibility — and blocking the search bot makes you invisible in that engine's answers. Know which is which before you edit `robots.txt`.
- **The eligibility gates differ.** Google AI Overviews/AI Mode reuse the *Google Search index* (be indexed, no special markup). Microsoft Copilot reuses the *Bing index* (be in Bing). ChatGPT Search blends a *Bing partnership + OpenAI's own `OAI-SearchBot` index*. Perplexity and Claude run their *own* index plus live fetches.
- **Everyone is moving from pages to passages.** Retrieval increasingly scores *chunks* of your page against a query (or many sub-queries), not the page as a whole. Extractable, self-contained passages win. See [03 · Content Strategy](03-content.md).
- **Citation density varies a lot.** Perplexity cites densely and inline on almost every answer; ChatGPT, Google AI Mode, and Copilot cite fewer sources, less consistently.

If you do only one thing after reading this chapter: **audit your `robots.txt` so you allow the *search/answer* crawlers of every engine you care about, and get indexed in both Google and Bing.**

---

## How to read this chapter

Every consumer AI answer engine runs some version of the same pipeline (covered in depth in [01 · Foundations](01-foundations.md)):

**query → (fan-out into sub-queries) → retrieve candidates → select passages → synthesize answer → attach citations**

What differs between engines — and what this chapter documents — is the *implementation* of each stage:

- **Where candidates come from** (own index, a partner's index, live fetch, a knowledge graph).
- **Which crawlers/user-agents** do the fetching, and whether they honor `robots.txt`.
- **How citations are chosen and rendered** (how many, how prominently, from where).
- **What controls publishers get** (opt-in, opt-out, structured data, feeds).

For each engine below you'll find a short **profile** in that shape, plus a per-engine **"how to optimize"** note. A [cross-engine comparison table](#cross-engine-comparison) and a [what actually differs](#the-differences-that-actually-matter) synthesis close the chapter.

---

## The crawler landscape at a glance

The single most actionable thing to understand is **which bot does what**, because that determines what you allow or block. As of **2026-09-14** (every row re-checked against the linked vendor page on that date), the major answer engines run these user-agents:

| User-agent (token) | Vendor | Job | Honors `robots.txt`? | Blocking it means… | Source |
|---|---|---|---|---|---|
| `GPTBot` | OpenAI | Model **training** | Yes | Excluded from future training data — **not** from ChatGPT Search | [OpenAI docs](https://developers.openai.com/api/docs/bots) |
| `OAI-SearchBot` | OpenAI | **Search indexing** for ChatGPT Search | Yes | **Not shown in ChatGPT search answers** | [OpenAI docs](https://developers.openai.com/api/docs/bots) |
| `ChatGPT-User` | OpenAI | **User-initiated** browsing/actions in ChatGPT | No (user action, not crawling) | Live user visits blocked at fetch time | [OpenAI docs](https://developers.openai.com/api/docs/bots) |
| `OAI-AdsBot` | OpenAI | Validating ad landing pages | Yes | Ad landing pages not validated | [OpenAI docs](https://developers.openai.com/api/docs/bots) |
| `PerplexityBot` | Perplexity | **Search indexing** for citations | Yes | Not eligible for Perplexity citations | [Perplexity docs](https://docs.perplexity.ai/guides/bots) |
| `Perplexity-User` | Perplexity | **User-initiated** page fetch | **Generally ignores** it | Little effect (user-initiated) | [Perplexity docs](https://docs.perplexity.ai/guides/bots) |
| `Googlebot` | Google | Search index (also **feeds AI Overviews, AI Mode, Gemini grounding**) | Yes | De-indexed from Google Search *and* its AI features | [Google Search Central](https://developers.google.com/search/docs/appearance/ai-features) |
| `Google-Extended` | Google | Opt-out **token** (not a distinct fetcher) for Gemini/Vertex training & grounding | Yes | Content withheld from Gemini training/grounding — **does not affect Search ranking** | [Google Search Central](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers) |
| `Bingbot` | Microsoft | Bing search index (also **feeds Copilot & Bing AI answers**) | Yes | Out of Bing → out of Copilot answers | [Bing Webmaster](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview) |
| `ClaudeBot` | Anthropic | Model **training** | Yes | Excluded from Claude training — **not** from Claude search | [Anthropic support](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) |
| `Claude-User` | Anthropic | **User-initiated** page fetch | Yes | User-directed fetches blocked | [Anthropic support](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) |
| `Claude-SearchBot` | Anthropic | **Search indexing** for Claude answers | Yes | Removed from Claude's search index | [Anthropic support](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) |
| `meta-externalagent` | Meta | Model **training** ("training foundation AI models or improving products") | Yes | Excluded from Meta's training crawl — the page does not say it affects Meta AI search | [Meta docs](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers) |
| `meta-webindexer` | Meta | **Search indexing** for Meta AI ("improve Meta AI search result quality") | Yes | Not indexed for Meta AI search (the page states the job, not the consequence) | [Meta docs](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers) |
| `meta-externalfetcher` | Meta | **User-initiated** link fetch for agentic features | "may bypass robots.txt rules" (user action) | Little effect (user-initiated) | [Meta docs](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers) |

> **The one mistake to avoid:** blocking the *training* bot (`GPTBot`, `ClaudeBot`, `Google-Extended`) is a legitimate rights choice and costs you **nothing** in answer visibility. Blocking the *search* bot (`OAI-SearchBot`, `PerplexityBot`, `Claude-SearchBot`, `Googlebot`, `Bingbot`) makes you **invisible** in that engine's answers. Many sites accidentally do the second while intending the first. Verify your rules per-token. (See [04 · Technical GEO](04-technical.md) for exact `robots.txt` recipes.)

> ⚠️ **Volatile — re-check before hard-coding a rule.** User-agent *version numbers* and IP-range files change over time. Verified **2026-09-14** against the vendor pages: OpenAI publishes `GPTBot/1.4`, `OAI-SearchBot/1.4` and `ChatGPT-User/1.0`, each with its own IP list (`openai.com/gptbot.json`, `openai.com/searchbot.json`, `openai.com/chatgpt-user.json`; `openai.com/adsbot.json` is `OAI-AdsBot`'s) ([OpenAI docs](https://developers.openai.com/api/docs/bots)); Perplexity publishes `PerplexityBot/1.0` and `Perplexity-User/1.0`, each with its own IP-list JSON linked from the page ([Perplexity docs](https://docs.perplexity.ai/guides/bots)); Meta's five tokens are all at `/1.1` ([Meta docs](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)); Anthropic names its three bots without version numbers ([Anthropic support](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)). The machine-readable IP list is the thing to automate against; the version number is the thing that will silently change.

> **Re-verified 2026-09-23 against the vendor pages — nothing moved.** OpenAI still publishes `GPTBot/1.4`, `OAI-SearchBot/1.4`, `ChatGPT-User/1.0` and `OAI-AdsBot`, and still states that each robots.txt setting is independent of the others ([OpenAI bots page](https://developers.openai.com/api/docs/bots)); its API changelog's September entries (latest 22 Sep) contain nothing about search, citations or crawlers ([changelog](https://developers.openai.com/api/docs/changelog)). Anthropic's support article (updated 7 Apr 2026) still names `ClaudeBot`, `Claude-User` and `Claude-SearchBot` without version strings, and its IP file `claude.com/crawling/bots.json` carries creationTime 2026-08-18 with 26 prefixes ([Anthropic](https://support.claude.com/en/articles/8896518)). Perplexity's `perplexitybot.json` is byte-identical on `www.perplexity.com` and `www.perplexity.ai` (creationTime 2025-02-07, eight prefixes) and `perplexity-user.json` dates from 2025-10-17 ([Perplexity crawler docs](https://docs.perplexity.ai/guides/bots)). Meta's five tokens remain at `/1.1` ([Meta](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers)). Neither the OpenAI nor the Perplexity nor the Meta page prints a last-updated stamp, so "unchanged" means unchanged between the 14 Sep and 23 Sep reads.

---

## ChatGPT & ChatGPT Search (OpenAI)

> **TL;DR:** A hybrid engine — it blends a Bing search partnership with OpenAI's own `OAI-SearchBot` index, fetches candidate pages, and synthesizes an answer with inline citations. To be eligible you must **allow `OAI-SearchBot`** and, in practice, **be indexed in Bing**.

**Retrieval.** OpenAI launched ChatGPT Search on **31 October 2024**, built on a partnership with Microsoft Bing, and supplements Bing's results with its own crawler, `OAI-SearchBot` ([Yoast overview](https://yoast.com/chatgpt-search/); [OpenAI docs](https://developers.openai.com/api/docs/bots)). When a query needs fresh information, ChatGPT retrieves ranked web results, fetches candidate pages, extracts content, and synthesizes an answer with citations. OpenAI describes a multi-step process: query formulation → retrieve results → select and visit pages → extract content → synthesize with citations.

> ⚠️ **needs verification (evolving):** through 2025–2026, independent trackers report ChatGPT's citations drifting *away* from a pure Bing footprint toward OpenAI's own index and re-ranking (e.g. Profound and Ahrefs measurements circulated widely, but the precise blend is not officially documented). Treat "ChatGPT = Bing" as a useful heuristic, not a fixed fact. Practically: **be strong in Bing *and* allow `OAI-SearchBot`.**

**Citation behavior.** Answers show inline source links and a sources list. Citation is not guaranteed on every answer; ChatGPT cites more when a query is clearly informational and time-sensitive. Independent write-ups note that the pages ChatGPT cites are "not necessarily the largest or best known… they are the websites that provide the best answer to the exact question the user is asking" ([AEO Expert](https://aeo-expert.nl/en/blog/how-chatgpt-selects-and-cites-sources), industry source).

**Crawlers / user-agents.** `OAI-SearchBot` (search indexing — the one that governs ChatGPT Search visibility), `GPTBot` (training), `ChatGPT-User` (live user actions/browsing), `OAI-AdsBot` (ad landing validation). Exact strings and IP lists are published by OpenAI ([docs](https://developers.openai.com/api/docs/bots)). Key official statement: *"Sites that are opted out of `OAI-SearchBot` will not be shown in ChatGPT search answers."*

**Publisher controls.** Allow `OAI-SearchBot` in `robots.txt`; you may independently block `GPTBot` if you don't want to be used for training — this does not affect search visibility. OpenAI publishes IP ranges for each bot for verification. There is no schema or special markup requirement.

**Vertical connectors and paid surfaces (added 2026-09-14).** Two September 2026 moves change *what* ChatGPT draws on rather than *how* it crawls. First, for whole verticals OpenAI is wiring in **licensed structured data instead of ranked web pages**: read-only connectors to official healthcare databases (1 Sep 2026 — [TechCrunch](https://techcrunch.com/2026/09/01/chatgpt-health-adds-epic-integration-for-clinicians-to-import-patient-data/), secondary) and **ChatGPT for Financial Services** (10 Sep 2026), which *"combines OpenAI's latest GPT-6 Astra model with embedded institutional content from premier financial data providers, including PitchBook, Daloopa, and LSEG News"* and offers *"granular, line-item citations"* back to source documents ([Yahoo Finance, 10 Sep 2026](https://finance.yahoo.com/technology/ai/articles/openai-launches-chatgpt-financial-services-204024031.html), syndicated coverage — OpenAI's own post returns HTTP 403 to automated fetchers). In those verticals the open web competes with a licensed feed for the citation slot. Second, **ads**: since 10 Sep 2026 select US advertisers can buy ChatGPT placements through **Amazon DSP**; the units appear *"as text and image units beneath organic ChatGPT responses"* and *"OpenAI will continue to control ad delivery and placement through its own systems"* ([Amazon Ads, 10 Sep 2026](https://advertising.amazon.com/library/news/amazon-ads-chat-gpt-advertising-integration) · [Search Engine Land, 10 Sep 2026](https://searchengineland.com/amazon-pilots-chatgpt-ads-through-its-dsp-488026)). OpenAI's position is that ads do not influence answers; organic GEO remains a separate discipline, and that separation should be tested, not assumed.

**The vertical pattern completes: law (added 2026-09-21).** Three verticals in seventeen days now answer from a curated or licensed corpus rather than from ranked open-web pages — healthcare (1 Sep), financial services (10 Sep) and now **law**. *Introducing Astra for Law* (**17 Sep 2026**) pairs GPT-6 Astra with a dedicated index: *"By using the legal search index, Astra for Law can search U.S. case law, statutes, regulations, court rules, and administrative decisions across a corpus of more than 230 million URLs, with sources added daily."* The corpus is assembled from partners, not crawled — OpenAI names **Thomson Reuters** for licensed content, and its work with the **Free Law Project** (the nonprofit behind **CourtListener**) for a case-law collection covering more than 99.9% of published U.S. precedential case law. Launch is to selected firms via Trusted Access in ChatGPT and Codex, API to follow ([OpenAI, 17 Sep 2026](https://openai.com/index/astra-for-law/) — `openai.com` returns HTTP 403 to automated fetchers, read from the Internet Archive raw mirror; corroborated by [Artificial Lawyer, 18 Sep 2026](https://www.artificiallawyer.com/2026/09/18/openai-launches-astra-for-law/)).

> **What this means for GEO, stated plainly.** In a vertical OpenAI has licensed, **the ceiling on open-web citation is set by the licensing deal, not by your content**. No amount of structure, freshness or entity clarity promotes an open-web page into a corpus it was never admitted to. In health, finance and law the honest advice is to redirect effort from *"be citable"* to *"be in the corpus"* — a business-development problem, not a content one — and to measure what share of answers in your vertical still draw on the open web at all before investing further.

**Sponsored Agents (added 2026-09-21).** OpenAI is testing an ad format that opens a brand-run conversation inside ChatGPT. Its separation claim, verbatim: *"The conversation with a Sponsored Agent is distinct from ChatGPT's independent answers and separate from the original conversation that the user started in ChatGPT. Sponsored Agents are now being tested with select advertisers in the United States."* ([OpenAI, 16 Sep 2026](https://openai.com/index/reimagining-advertising-with-ai/) · [Search Engine Roundtable, 16 Sep 2026](https://www.seroundtable.com/openai-chatgpt-sponsored-agents-42104.html)). The paid surface is now conversational and sits beside the organic answer; the "does not influence answers" claim remains a **vendor claim to be tested, not assumed**.

**Model-configuration changes are a measurement confound (added 2026-09-21).** On **14 Sep 2026** OpenAI retired automatic escalation to reasoning for paid users: *"We're retiring automatic switching from Instant to Thinking (reasoning) for ChatGPT Plus and Pro users globally."* ([ChatGPT Release Notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — 403 to automated fetchers, read from the Internet Archive raw mirror). Reasoning depth drives how many sub-queries are fired and how many sources are fetched, so a citation panel running on Plus/Pro accounts may see sources-per-answer drop for reasons that have nothing to do with the sites being measured. See [06 · Measurement](06-measurement.md).

**How to optimize for ChatGPT Search.**
- **Get and stay indexed in Bing** (Bing Webmaster Tools, sitemap, IndexNow) — it's the historical backbone and a low-effort, high-leverage move that also feeds Copilot.
- **Allow `OAI-SearchBot`.** Double-check you aren't blocking it while blocking `GPTBot`.
- **Write direct, question-shaped answers.** A page that names the exact user-agent to allow, the file to edit, and the mistake to avoid is easier to lift into an answer than a discursive essay.
- **Freshness and clear entity naming help**, as ChatGPT favors current, specific content for time-sensitive queries.

**Dated note (2026-09-23) — Voice now searches, and its citation display is unmeasured.** The ChatGPT release notes entry of **9 Sep 2026** says *"ChatGPT Voice can now use GPT-5.6 or GPT-6 Astra when it needs to search or reason through harder questions. Choose your model and reasoning effort using the same controls as text chat."* ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — 403 to automated clients; read from the Internet Archive raw mirror, snapshot 2026-09-18, whose newest entry is 17 Sep). Whether a Voice answer shows attributable sources, and in what form, is not stated by OpenAI and has not been measured here — the same gap as Siri AI and Search Live. *Re-checked 2026-09-23: the user-agent list above is unchanged; the "ChatGPT = Bing" heuristic remains `needs verification` — the Peec AI in-house-index claim logged in W39 is still single-source.*

*Last verified: 2026-08.*

---

## Perplexity

> **TL;DR:** A retrieval-first "answer engine" built on its own index plus live fetches. It **cites densely and inline** on nearly every answer, favors fresh and well-structured sources, and even *pays* some publishers when their content is cited. To be eligible, **allow `PerplexityBot`.**

**Retrieval.** Perplexity uses Retrieval-Augmented Generation to search the web in real time and ground answers in retrieved sources. Its own crawler, `PerplexityBot`, is "designed to surface and link websites in search results on Perplexity" and is *not* used for model training ([Perplexity docs](https://docs.perplexity.ai/guides/bots)). Independent observation suggests it retrieves on the order of ~10 pages per query and cites ~3–4 in the visible answer, though this varies ([AI Labs Audit](https://ailabsaudit.com/blog/en/perplexity-guide-maximize-citations), industry source — *treat the exact numbers as illustrative, not official*).

**Citation behavior.** Perplexity is, functionally, **a citation system, not a ranking system** — numbered inline citations appear on almost every answer, and visibility depends on whether a passage can be *extracted and cited* rather than on a traditional ranking position. It has no fixed knowledge cutoff and prefers recently updated sources.

**Crawlers / user-agents.** `PerplexityBot` (search indexing; honors `robots.txt`; string `…compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot`) and `Perplexity-User` (user-initiated fetch that *"generally ignores robots.txt rules"* because it acts on a specific user request). IP ranges are published at `perplexity.com/perplexitybot.json` and `perplexity.com/perplexity-user.json` ([Perplexity docs](https://docs.perplexity.ai/guides/bots)).

**Publisher controls.**
- **`robots.txt`:** allow `PerplexityBot` to be eligible for citations. Note that blocking `Perplexity-User` has limited effect, as it is user-initiated.
- **Publisher revenue-share (opt-in):** Perplexity's **Comet Plus** program shares revenue with participating publishers when their content is cited — reported as an **80/20 split** (80% to publishers) from an initial pool, paying across human visits via the Comet browser, search citations, and agent actions ([Search Engine Journal](https://www.searchenginejournal.com/perplexity-launches-comet-plus-shares-revenue-with-publishers/554596/); [LLM Pulse breakdown](https://llmpulse.ai/blog/perplexity-publishers-program/)). *Program terms and partner counts change frequently — verify current status before relying on them.*

**API and research notes (added 2026-09-14).**
- **The Sonar chat-completions endpoint retires on 27 Sep 2026.** Perplexity staff reconfirmed on 10 Sep 2026: *"The Sonar chat completions endpoint will retire on September 27. You will need to migrate to the Agent API responses endpoint before then."* Re-checked 2026-09-21: the guide states *"Sonar will be supported until September 27, 2026"*, names `https://api.perplexity.ai/v1/agent` as the endpoint, and the notice still appears in the forum and the migration guide but **not** in the developer changelog ([Perplexity API forum, 10 Sep 2026](https://community.perplexity.ai/t/sonar-moving-to-agents-api/6061) · [migration guide](https://docs.perplexity.ai/docs/agent-api/migrate-from-sonar/overview)). Any citation-tracking pipeline built on `sonar`/`sonar-pro` needs to migrate **and re-baseline**, since a different endpoint is not guaranteed to retrieve or cite identically — see [06 · Measurement](06-measurement.md#google-search-console-the-ai-performance-report).
- **Perplexity's own retrieval benchmark uses agent citations as relevance labels.** *Q2D-Web* ([arXiv:2609.08887](https://arxiv.org/abs/2609.08887), submitted 8 Sep 2026; announced on Perplexity's forum on 9 Sep) pairs a **190M-document web corpus** with **70k agentic search queries in ten languages, "reformulated from real-world user queries in production systems"**, and provides *"three sets of fixed relevance judgments: agent citations, production rankings, and a combined set."* Two things to take from the abstract: the first-stage retriever serves **machine-rewritten queries, not the user's words**, and **what the agent cited is treated as a ground-truth signal** — a public corpus on which "retrieved" and "cited" can be told apart. Preprint; vendor-released; not peer-reviewed.

**How to optimize for Perplexity.**
- **Source depth beats content volume.** Getting cited "is not a content-volume problem — it is a source-depth problem": original data, primary sources, specificity ([Authority Tech](https://authoritytech.io/curated/perplexity-citations-source-depth-not-more-blog-posts), industry source).
- **Keep pages fresh and structurally clean** — clear headings, factual, well-attributed.
- **Allow `PerplexityBot`** and monitor server logs for its visits to see what's being indexed.

**Dated notes (2026-09-23).**
- **Sonar deadline unchanged, retirement still unannounced in the changelog.** The migration guide still says *"Sonar will be supported until September 27, 2026"* ([migration guide](https://docs.perplexity.ai/docs/agent-api/migrate-from-sonar/overview)); the developer changelog's five September entries cover new Agent API models, custom MCP connectors and OAuth for the remote MCP server, and none mentions the retirement ([changelog](https://docs.perplexity.ai/changelog.md)). The next pass must record whether the endpoint actually stopped.
- **Citation markup differs by preset.** The July 2026 changelog entry states that the `fast` preset cites with numbered markers such as `[1]`, while `low`, `medium` and `high` cite with source-typed markers such as `[web:1]`, and that *"after a successful tool call, the `low`, `medium`, and `high` presets include at least one citation in the final answer"* ([changelog, July 2026](https://docs.perplexity.ai/changelog.md)). A parser that counts `[n]` alone misses every `[web:n]` — see [06 · Measurement](06-measurement.md).
- **IP files.** `perplexitybot.json` is byte-identical on `www.perplexity.com` and `www.perplexity.ai` (creationTime 2025-02-07, eight prefixes, not regenerated in nineteen months); the docs give the `.com` host as canonical ([Perplexity crawler docs](https://docs.perplexity.ai/guides/bots)).

*Last verified: 2026-08.*

---

## Google — AI Overviews, AI Mode & Gemini

> **TL;DR:** Three surfaces, **one foundation: the Google Search index + Knowledge Graph, grounded by Gemini.** Eligibility is simply *being indexed and eligible for a snippet* — **no special markup, no separate opt-in.** Selection has shifted from pages to **passages**, chosen via **query fan-out** (one question splits into many parallel sub-queries).

Google runs three distinct AI answer surfaces that share plumbing but behave differently ([Green Flag Digital comparison](https://greenflagdigital.com/learning-ai/google-ai-overviews-vs-ai-mode-vs-gemini/), industry source):

- **AI Overviews** — the AI summary box atop many traditional search results pages.
- **AI Mode** — a full conversational search surface that decomposes a query into sub-queries and reasons across them.
- **Gemini app** — the standalone assistant; when it searches, it grounds on Google Search.

**Retrieval.** All three rely on **Gemini grounding**: they anchor responses in live Google Search results and the Search index, and pull from the **Knowledge Graph** and **Shopping Graph** where relevant. AI Mode uses **query fan-out**: it decomposes a prompt into multiple sub-queries run in parallel, then synthesizes the strongest passages into one answer with inline citation links ([Search Atlas](https://searchatlas.com/blog/google-ai-mode/), industry source).

**Citation behavior.** Selection is **largely independent of a single ranking position** and works at the **passage level**, drawing from a broader retrieval pool shaped by fan-out. Independent studies report that pages ranking in the top 10/20 are far more likely to be cited than lower-ranked pages, but the visible #1 result is often *not* the cited source — and citation overlap between AI Mode and AI Overviews is low (multiple 2026 analyses put it around **~14%**, meaning the two surfaces cite very differently despite shared infrastructure).

> ⚠️ **needs verification:** the passage-selection specifics (e.g. cosine-similarity of scroll-to-text fragments to sub-queries) and the "~14% overlap" figure come from third-party SEO measurements, not Google. They're directionally useful but not officially confirmed — cite them as third-party observations, and expect them to move.

> **Correction and addition (2026-09-23) — the source of the "~14%" figure, and what it actually compares.** SE Ranking's June 2025 sample of 10,000 keywords reports *"AI Mode and AI Overviews share a response overlap in 10.7% of URLs and 16% of domains. Overlap between AIM and organic results is also limited: 14% at the URL level"* (21.9% at domain level) ([SE Ranking, 29 Aug 2025](https://seranking.com/blog/ai-mode-research/), industry-study). So **14% is AI Mode vs. the organic top 10; AI Mode vs. AI Overviews is 10.7%** — the sentence above conflates them. The original wording is left in place; the attribution to this study is the handbook's, not SE Ranking's. A later SE Ranking pass (68,313 keywords, 1,321,398 AI Mode citations collected 12 Feb 2026) reports **google.com as the most-cited domain at 17.42%**, up from 5.7% in June 2025, *"more than the next six domains combined"* ([SE Ranking, 6 Mar 2026](https://seranking.com/blog/google-links-in-ai-mode-answers/), industry-study, single SEO-tool dataset) — self-citation share is now a variable a panel must report.

**Crawlers / user-agents.** There is **no AI-specific fetching crawler**: `Googlebot` crawls for the Search index, and the AI features draw from that same index. `Google-Extended` is **not a separate crawler that appears in your logs** — it's a `robots.txt` *token* that lets you opt out of having your already-crawled content used for Gemini/Vertex generative training and grounding.

**Publisher controls (from Google's official [AI features guidance](https://developers.google.com/search/docs/appearance/ai-features)).**
- *"There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary."* A page just needs to be **indexed and eligible to be shown with a snippet.**
- *"You don't need to create new machine readable files, AI text files, or markup to appear in these features. There's also no special schema.org structured data that you need to add."*
- Standard snippet controls apply: `nosnippet`, `max-snippet`, `data-nosnippet` limit what text can be used (but also limit your citation surface — a trade-off).
- **`Google-Extended`** opts you out of Gemini training/grounding **without affecting your Google Search ranking or inclusion** — a genuinely separate lever from Search visibility ([Google crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers); that ranking/inclusion sentence is on the crawlers page, not the AI-features page).
- Clicks from AI features are counted in **Search Console**'s overall search traffic. Search Console also carries an **AI performance report** covering AI Overviews and AI Mode (impressions, pages, countries, devices, dates — **no click data**) ([Search Engine Land, 31 Aug 2026](https://searchengineland.com/google-search-console-ai-performance-reports-and-search-generative-ai-control-rolling-out-globally-486269)).
- **New (31 Aug 2026) — the `Search generative AI control`, now worldwide.** Google's Search Console help page states *"As of August 31, 2026, we've rolled out this control to all websites worldwide."* It decides whether your content *"can appear in Search generative AI features, including showing up as links and helping to ground AI responses"* — **AI Overviews, AI Mode, and generative AI in Discover**. Critically, Google says it *"isn't used as a ranking or inclusion signal affecting other parts of Search"*, and that opting out means *"You won't receive any traffic or impressions from these features"* ([Google Search Console Help](https://support.google.com/webmasters/answer/16908024)). This is the first control that separates *AI-answer presence* from *Search presence* for everyone, everywhere — see [04 · Technical GEO](04-technical.md#snippet-directives--and-the-new-opt-out-toggle). For GEO the default advice is unchanged: leave it on.
- **New (Aug 2026) — the embeddable "Preferred Sources" button.** Publishers can drop in a one-click button (implementation code in Search Central) that lets a reader mark their site as a **Preferred Source**; those sources then get a "preferred" badge and surface more in **Top Stories, AI Overviews, and AI Mode** for that reader. Google reported **600,000+** sources already selected ([Press Gazette, 24 Aug 2026](https://pressgazette.co.uk/platforms/google-preferred-source-article-users-curate-sources-top-stories-ai-overview-search/)). This is Google's first genuinely *publisher-controlled* lever on AI-answer placement — drive reader opt-ins where relevant. Relatedly, Google extended **link carousels for "developing topics"** (already in AI Overviews) into **AI Mode** answers, adding a new inline link slot that surfaces preferred/original-coverage sources ([Search Engine Land, 26 Aug 2026](https://searchengineland.com/google-adds-link-carousels-for-developing-topics-in-ai-mode-485884)).

- **New (2026-09-21) — three more surfaces, and one of them blurs paid and earned.** (a) **Local knowledge panels are being rendered as AI Overviews**: *"Google is turning the local knowledge panels, your Google Business Profile, into an AI Overview listing"* — an "AI Overview" header with a **Show more** button expanding into a chat-style interface; spotted by Ben Fisher, replicated by Barry Schwartz, no Google announcement ([Search Engine Roundtable, 17 Sep 2026](https://www.seroundtable.com/google-local-knowledge-panel-ai-overview-42105.html)). The local panel was a structured-data surface a business largely controlled; a generated layer on top imports AI Overview staleness and paraphrase risk onto it. (b) **AI Mode is testing text-link ads** rendered as in-line anchor text inside the answer, labelled *"Sponsored"* above the response ([Search Engine Roundtable, 15 Sep 2026](https://www.seroundtable.com/google-ai-mode-text-link-ads-42082.html)). **Any pipeline that counts "links inside the AI Mode answer" as earned citations must now read the `Sponsored` label and exclude them**, or paid placements silently inflate the citation count. (c) **Search Live now runs on Gemini 3.8 Live** ([Google, 15 Sep 2026](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)), making it a third Google answer surface to audit — and a voice-first one. Google's post says nothing about grounding, sources or link display, so **treat Search Live's citation behaviour as unmeasured rather than assuming it matches AI Mode.**

- **New (Sep 2026) — "People also ask" answers are now almost entirely AI Overviews.** Two vendor datasets converge: AlsoAsked, from *"roughly 19.2 million English-language queries logged during 2026"*, puts AI-generated PAA answers at **86% in August and 97% in the first week of September 2026**, against about 12% fourteen months earlier; Allintitle's *Also Ask Miner* records 100% since August ([Search Engine Roundtable, 9 Sep 2026](https://www.seroundtable.com/ppa-ai-overviews-google-42047.html), relaying both vendors' LinkedIn posts — `⚠️ vendor data; primary posts not independently retrieved`). For GEO it means the PAA box is no longer a separate citation surface: those answers carry AI Overview citations, and Google was simultaneously testing a **thinner AI Overview citations panel** ([Search Engine Roundtable, 8 Sep 2026](https://www.seroundtable.com/google-thinner-ai-overview-citations-panel-42040.html), unconfirmed test).
- **Citation display is a per-model property — and it can regress.** On 2–3 Sep 2026, AI Mode running the new Gemini 3.8 Flash model returned answers **with no links or citations** for many top-of-funnel queries; Google's Robby Stein replied *"This isn't working as intended, and we'll roll out a fix soon"*, and links were back the next morning ([Search Engine Land, 3 Sep 2026](https://searchengineland.com/google-to-fix-citation-bug-with-gemini-3-8-flash-in-ai-mode-486892) · [Search Engine Roundtable, 3 Sep 2026](https://www.seroundtable.com/google-ai-mode-gemini-38-no-links-42011.html)). Record **which model served the answer** in any citation measurement; a day of zero citations is a model bug, not a visibility loss.

**How to optimize for Google's AI surfaces.**
- **Win classic Google fundamentals first** — indexing, helpful content, snippet eligibility. AI features are built *on top of* the same index; there is no separate door.
- **Optimize for fan-out, not just your head term.** Cover the *sub-questions* a topic implies; entity-rich passages that name specific tools, stats, and steps score better in passage retrieval.
- **Write self-contained passages** (~40–60 words) that answer one sub-query cleanly, with clear headings around them.
- **Don't reach for special AI markup** — Google explicitly says none is needed. Spend that effort on clarity and coverage instead. (Schema still helps *classic* rich results and entity understanding; see [04 · Technical GEO](04-technical.md).)

**Re-checked 2026-09-23.** Google's help page for the Search generative AI performance report still defines impressions only (links shown in a generative AI feature, grouped by page, country, device and date) and no click or query metric; it says *"As of August 31, 2026, we've rolled out these insights to all websites worldwide"* while a later paragraph still reads "Not all properties have access to the report, as we're rolling out" ([Google Search Console Help](https://support.google.com/webmasters/answer/16984139?hl=en)). A separate report exists for **Discover** ([Google Search Console Help](https://support.google.com/webmasters/answer/16983858?hl=en)). Comscore's Q2 2026 panel puts an AI Overview on **39.4%** of desktop Google searches in June 2026, up from 25.8% in July 2025 ([Comscore press release, 22 Sep 2026](https://www.comscore.com/Insights/Press-Releases/2026/9/Comscores-Q2-2026-AI-Intelligence-Report), industry-study; desktop panel; the release states no geography) — a different instrument from the Semrush keyword-based prevalence figures in [01 · Foundations](01-foundations.md#why-it-matters-now-2026), so do not splice the series.

*Last verified: 2026-08.*

---

## Microsoft Copilot & Bing

> **TL;DR:** Copilot's web answers ride on the **Bing index** (crawled by `Bingbot`) — there's **no separate Copilot web crawler**. Cite prominently and inline. High-leverage lever: **be in Bing** (which also partly feeds ChatGPT Search) and use **IndexNow** for near-instant freshness.

**Retrieval.** Microsoft introduced **Copilot Search in Bing** in April 2025 ([Bing blog](https://blogs.bing.com/search/April-2025/Introducing-Copilot-Search-in-Bing)). Copilot uses Retrieval-Augmented Generation over the Bing index, separating the steps of *retrieving* search results and *summarizing* them into a cohesive, grounded answer ([Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/generative-ai-public-websites)). Copilot "pulls from the Bing index, crawled by `Bingbot`, with no separate Copilot-specific crawler for web content" ([industry summary](https://llmpulse.ai/ai-crawler-index/bingbot), industry source; `Bingbot` itself is documented by Microsoft at [Bing Webmaster Tools](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0)).

**Citation behavior.** Copilot Search "cites its sources prominently"; sentences and passages are inline-linked so users can navigate to the source, and cited sources plus relevant web results are surfaced alongside the answer ([Bing blog](https://blogs.bing.com/search/April-2025/Introducing-Copilot-Search-in-Bing)). For the Bing results Copilot grounds on, Microsoft Learn lists Bing's main *ranking* parameters for a URL used as a knowledge source as **relevance, user engagement, and freshness** — ranking parameters, not a stated citation rule ([Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/generative-ai-public-websites)).

**Crawlers / user-agents.** `Bingbot` (the same crawler that builds the Bing search index). Bing respects `robots.txt` and the `Crawl-delay` directive.

**Publisher controls & measurement.**
- **Be in the Bing index:** allow `Bingbot`, submit a sitemap, verify in **Bing Webmaster Tools**.
- **IndexNow** (Microsoft's open push protocol) *notifies* Bing the moment content changes — Microsoft's own wording is that it "notifies multiple search engines of your content changes as soon as they happen" ([Why IndexNow, Bing Webmaster Tools](https://www.bing.com/indexnow)). **Notification is not indexing:** Microsoft is explicit that submitting a URL does not guarantee it will be indexed, because the engine still has to crawl and process it. So IndexNow removes the *discovery* delay, which is the part that used to be measured in days; what happens after that is the engine's decision. `⚠️ The previous version of this line claimed it collapses indexing lag "from days to minutes", sourced to a marketing blog whose domain now fails TLS. No primary source gives a figure; if you have one, open a PR.`
- **AI Performance report** (Bing Webmaster Tools, public preview since Feb 2026): shows total citations, cited pages, and "**grounding queries**" — the phrases the AI used to retrieve your content — across Copilot, Bing AI summaries, and select partner integrations ([Bing Webmaster blog](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)). Microsoft frames this explicitly as a step toward **GEO** tooling for publishers. This is one of the few *first-party* AI-citation dashboards available — use it.

**How to optimize for Copilot.**
- **Prioritize Bing indexing and IndexNow** — the highest-leverage, lowest-effort move, and it double-dips into ChatGPT Search.
- **Structure for liftability:** clear headings, definitions, tables; put the answer near the top.
- **Lean into Microsoft-adjacent authority** where relevant (Microsoft Learn, LinkedIn, well-structured docs) — Copilot draws heavily on these.

**Dated notes (2026-09-23).**
- **Deep citations slipped.** Microsoft 365 roadmap item 523223, *Deep citations in Copilot*, shows status "In development", public preview **October CY2026** and general availability **November CY2026**, modified 2026-09-16; scope starts with Word and PowerPoint files, *"then adding Meetings, Web, and PDF references"* ([Microsoft 365 roadmap API](https://www.microsoft.com/releasecommunications/api/v1/m365?id=523223)) — so no web-citation change ships this quarter. Whether an earlier GA date was carried in July stays `needs verification`; the API returns current values only.
- **Where web citations show at all.** Microsoft documents that web-search query citations appear only in Microsoft 365 Copilot Chat, not in the Copilot pane inside Word or PowerPoint, and that queries expire from the thread after 24 hours; the queries sent to Bing do not affect Bing ranking ([Microsoft Learn, 2026-08-18](https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access)).
- **Enterprise-only citation analytics.** Message Center post MC1247902 (roadmap 480725) says SharePoint will show *"how often content is referenced by Microsoft 365 Copilot chat"* — popular content ranked by citations and a "Total citations" card — for tenants with more than 50 Copilot licences, rolling out end of August to end of September 2026 ([community mirror of the Message Center post, published 9 Mar, updated 2 Sep 2026](https://mc.merill.net/message/MC1247902); the first-party admin-center post needs a tenant login). That no public-web equivalent exists is this handbook's inference. Details in [06 · Measurement](06-measurement.md#bing-webmaster-tools-ai-performance--the-16-jun-2026-expansion-added-2026-09-23).
- **Bing crawler list.** Bing names five crawlers — `Bingbot`, `AdIdxBot`, `BingPreview`, `MicrosoftPreview` and `BingVideoPreview`; `MicrosoftPreview/2.0` generates page snapshots for Microsoft products ([Bing Webmaster help](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0)). Comscore's panel puts Copilot Search on **17.3%** of Bing searches in June 2026, from 11.8% a year earlier ([Comscore press release, 22 Sep 2026](https://www.comscore.com/Insights/Press-Releases/2026/9/Comscores-Q2-2026-AI-Intelligence-Report), industry-study).
- *Re-checked 2026-09-23: the Bing Search blog's newest post is still 16 Jun 2026; the M365 Copilot release notes' newest entry is 25 Aug 2026 ([Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)).*

*Last verified: 2026-08.*

---

## Claude (Anthropic)

> **TL;DR:** Claude can search the web and returns **structured citations with clickable source URLs**. Anthropic separates **training** (`ClaudeBot`), **user fetches** (`Claude-User`), and **search indexing** (`Claude-SearchBot`) into distinct bots — to appear in Claude's answers, **allow `Claude-User` and `Claude-SearchBot`** even if you block training.

**Retrieval.** Claude performs web search on demand and grounds answers in retrieved pages. `Claude-SearchBot` "navigates the web to improve search result quality… It analyzes online content specifically to enhance the relevance and accuracy of search responses," while `Claude-User` fetches specific pages when a user's question requires it ([Anthropic support](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)).

**Citation behavior.** When Claude cites, it returns **structured citations with clickable source URLs**, creating a direct referral path to the source ([Anthropic, web search tool documentation — *Citations*](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool), primary source: each citation carries the source URL, title and cited text). Anthropic's move to *three granular bots* (announced 2025) is significant because it lets publishers **opt out of training while staying visible in search** — a distinction not every vendor makes as cleanly ([Search Engine Journal](https://www.searchenginejournal.com/anthropics-claude-bots-make-robots-txt-decisions-more-granular/568253/)).

**Crawlers / user-agents.** `ClaudeBot` (training), `Claude-User` (user-initiated fetch), `Claude-SearchBot` (search indexing). All respect `robots.txt` and support `Crawl-delay`; IP ranges are published at `claude.com/crawling/bots.json` ([Anthropic support](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)). A `claude-code` agent also exists for the Claude Code CLI.

**Publisher controls.** Per-bot `robots.txt` rules. To maximize visibility while controlling training use:

```
# Allow Claude to find and cite you in answers
User-agent: Claude-SearchBot
Allow: /
User-agent: Claude-User
Allow: /

# But keep your content out of model training
User-agent: ClaudeBot
Disallow: /
```

**How to optimize for Claude.**
- **Allow `Claude-SearchBot` and `Claude-User`** — the two that govern answer visibility. Block `ClaudeBot` only if opting out of training.
- **Clarity and accuracy signals matter**, given Claude-SearchBot's stated goal of relevance and accuracy — well-structured, factually clean, well-attributed content.
- **Standard extractability wins:** self-contained passages, clear definitions, sources cited on your own page.

**Re-checked 2026-09-23.** The support article (updated 7 Apr 2026) is unchanged: three bots, no version strings, and the sentence that matters for visibility — *"Disabling Claude-SearchBot on your site prevents our system from indexing your content for search optimization, which may reduce your site's visibility and accuracy in user search results."* ([Anthropic](https://support.claude.com/en/articles/8896518)). Comscore's panel has Claude's share of AI prompt volume rising from 2% to 11% between January and June 2026 ([Comscore press release, 22 Sep 2026](https://www.comscore.com/Insights/Press-Releases/2026/9/Comscores-Q2-2026-AI-Intelligence-Report), industry-study) — enough that a citation panel that omits Claude is omitting a measurable slice.

*Last verified: 2026-08.*

---

## Emerging & other engines

The long tail is growing and worth tracking; treat this section as a watchlist rather than settled fact.

- **Grok (xAI)** — built into X, with privileged real-time access to the X timeline plus open-web search. Reporting suggests Grok's WebSearch leans on a **pre-built index** rather than always crawling live at query time ([tryProfound guide](https://www.tryprofound.com/blog/understanding-grok-a-comprehensive-guide-to-grok-websearch-grok-deepsearch), industry source). Strong on real-time social/trending queries. *Crawler user-agent specifics — verify against xAI's current docs.*
- **Meta AI** — deployed across WhatsApp, Instagram, and Facebook (3B+ users), powered by Llama, retrieving from the open web plus Meta's own platform signals. Meta documents five crawlers ([Meta docs](https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers), verified 2026-09-14): `meta-webindexer/1.1` *"navigates the web to improve Meta AI search result quality"* (the search-index bot), `meta-externalagent/1.1` *"crawls the web for use cases such as training foundation AI models or improving products"* (the training bot), `meta-externalfetcher/1.1` *"fetches individual links at a user's request"* and *"may bypass robots.txt rules"*, plus `facebookexternalhit/1.1` (link previews) and `meta-externalads/1.1` (ads). Same rule as for every vendor in the table above: blocking the training bot is a rights choice; blocking `meta-webindexer` is a visibility choice.
- **DeepSeek** — a reasoning-focused model that integrated web search; popular as a free, uncapped option. ⚠️ **needs verification — no first-party crawler documentation found.** Searched again 2026-09-21, and the check that settles it: the user-agent string the directories attribute to DeepSeek is `Mozilla/5.0 (compatible; DeepSeekBot/1.0; +https://www.deepseek.com/about)`, and **that URL — the one inside the token, whose whole purpose is to identify the operator — returns 404**. `deepseek.com/robots.txt` is `User-Agent: * / Allow: /` and names no DeepSeek crawler. So the community [ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt) list and several bot directories carry a `DeepseekBot/1.0` token whose self-identification link does not resolve, while one directory states the opposite — *"DeepSeek does not publish a user agent for its crawler"* and its fetches *"look like regular browser traffic in your logs"* ([xSeek, updated Apr 2026](https://www.xseek.io/docs/deepseek-user-agents)); no page on DeepSeek's own site or API docs describing a crawler turned up in that search (which proves only that the search found none). Treat any DeepSeek token as unconfirmed until DeepSeek publishes one.
- **Brave Search (AI answer), You.com, Arc** — smaller answer engines. In a one-pass observation on **2026-09-13**, **Brave Search's AI answer showed inline citation markers on 6 of 6 fixed queries** (3–12 link chips per answer, plus a sources list under the answer). **You.com** could not be observed: in a clean session its search redirects to a sign-in page. **Arc** has no Linux client and was not observed. Method, queries, timestamps and limits: [`protocols/minor-engines-citations.md`](protocols/minor-engines-citations.md). Lower reach than the majors; sometimes their own crawlers and controls. *Scope: one pass per query, from Spain, no login, on the date given; two follow-up requests minutes later returned no AI answer, so this describes the product that day, not a stable rate.*

- **DuckDuckGo — Duck.ai / DuckAssist (added 2026-09-23).** The first of the "not swept" engines, now read from first-party pages. DuckDuckGo's help page states that `DuckAssistBot` *"crawls pages in real-time for our AI-assisted answers, which prominently cite their sources. This data is not used in any way to train AI models."* A `robots.txt` disallow takes effect after **72 hours** and does not affect organic rankings or inclusion; the user agent is `DuckAssistBot/1.2` and IPs are published at `duckduckgo.com/duckassistbot.json` (creationTime 2026-09-01, 486 prefixes) ([DuckDuckGo help](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot); the help page prints no date). Citation behaviour of the answer surface itself is not measured here.

> ⚠️ **needs verification:** the emerging-engine details above lean on secondary sources and move quickly. Before optimizing for any of them, confirm the current crawler tokens, index source, and citation behavior against first-party documentation, and log material changes in [`updates/`](../updates/README.md).

---

## Cross-engine comparison

As of **2026-08**. "Index source" = where answer candidates primarily come from. Verify each cell before betting on it.

> **Dated note (2026-09-23) — which engines a panel should weight.** Comscore's Q2 2026 report says ChatGPT's share of AI prompt volume fell from 70% to 50% between January and June 2026 while Gemini rose from 17% to 30% and Claude from 2% to 11% ([Comscore press release, 22 Sep 2026](https://www.comscore.com/Insights/Press-Releases/2026/9/Comscores-Q2-2026-AI-Intelligence-Report), industry-study; opt-in panel, the underlying report was not opened). The table's rows are unchanged; the weight a measurement panel gives each row is not.

| Engine | Primary index / retrieval source | Search/answer crawler to **allow** | Training bot you may **block** separately | Citation density | First-party publisher controls |
|---|---|---|---|---|---|
| **ChatGPT Search** | Bing partnership **+** OpenAI's own `OAI-SearchBot` index | `OAI-SearchBot` | `GPTBot` | Medium, inconsistent | `robots.txt` per-bot; IP lists |
| **Perplexity** | Own index + live RAG fetch | `PerplexityBot` | *(no training bot; neither bot trains)* | **High**, inline on ~every answer | `robots.txt`; **Comet Plus** revenue-share (opt-in) |
| **Google AI Overviews / AI Mode / Gemini** | **Google Search index** + Knowledge/Shopping Graph, Gemini-grounded | `Googlebot` | `Google-Extended` (token; no ranking impact) | Low–medium; passage-level; low overlap between surfaces | Snippet controls; Search Console reporting; **no special markup needed** |
| **Microsoft Copilot / Bing** | **Bing index** | `Bingbot` | *(training governed via Bing controls)* | Medium, prominent inline | Bing Webmaster Tools; **IndexNow**; **AI Performance** dashboard |
| **Claude** | Own index + live fetch | `Claude-SearchBot`, `Claude-User` | `ClaudeBot` | Structured, clickable | `robots.txt` per-bot; IP list |
| **Grok / Meta AI / DeepSeek / others** | Varies (own index, platform signals, live search) | ⚠️ verify per vendor | ⚠️ verify per vendor | Varies (You.com/Brave high) | Emerging — ⚠️ verify |

---

## The differences that actually matter

If the profiles blur together, these are the distinctions that change what you *do*:

1. **Training vs. search is a hard split — and it's your biggest footgun.** Every major vendor except Perplexity now separates a *training* crawler from a *search/answer* crawler. You can (and often should) block training while **allowing** search. Blocking the wrong token silently deletes you from an engine's answers. Audit per-token.

2. **Two indexes give you most of the reach.** Being in the **Google index** unlocks AI Overviews, AI Mode, and Gemini grounding. Being in the **Bing index** unlocks Copilot *and* feeds ChatGPT Search. Get those two right and you've covered the majority of consumer AI-answer traffic before touching anything engine-specific.

3. **No special "AI markup" gate exists on Google — clarity is the gate.** Google is explicit: no AI files, no special schema, no extra optimizations to appear in AI features. Every engine rewards the same thing — **extractable, self-contained, well-sourced passages.** That's a content problem ([03](03-content.md)), not a markup trick.

4. **Passages beat pages.** Retrieval scores *chunks*, and Google AI Mode explicitly fans one query out into many. Optimize for the *sub-questions*, not just your head keyword, and make each answer liftable on its own.

5. **Citation economics are starting to exist.** Perplexity's Comet Plus revenue-share and Microsoft's AI Performance dashboard are early signs that "being cited" is becoming a measurable — and occasionally *paid* — outcome. Measurement is covered in [06 · Measurement](06-measurement.md).

6. **The traffic math changed.** In a controlled behavioral study, Google users clicked a traditional result in just **8%** of visits when an AI summary was present versus **15%** without one, and clicked a link *inside* the summary in only **1%** of visits ([Pew Research Center, 2025](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/); n = 900 U.S. adults, 68,879 searches, March 2025). Being *cited* is increasingly the win — not the click. This reframes the whole point of GEO.

---

## What to do about it (action checklist)

- [ ] **Audit `robots.txt` per user-agent.** Allow the search/answer bots (`OAI-SearchBot`, `PerplexityBot`, `Googlebot`, `Bingbot`, `Claude-SearchBot`, `Claude-User`). Block *training* bots (`GPTBot`, `ClaudeBot`, `Google-Extended`) only if that's a deliberate rights choice. → recipes in [04 · Technical GEO](04-technical.md).
- [ ] **Confirm indexation in both Google and Bing.** Submit sitemaps; verify in both webmaster tools; enable **IndexNow**.
- [ ] **Verify crawler identities by IP**, not just user-agent string, using each vendor's published IP-range JSON (spoofing is common).
- [ ] **Write for passages:** self-contained 40–60-word answers under clear headings, entity-rich, with your own citations. → [03 · Content Strategy](03-content.md).
- [ ] **Cover the fan-out:** answer the sub-questions a topic implies, not just the head term.
- [ ] **Turn on first-party measurement:** Bing Webmaster **AI Performance**, Google **Search Console**, and server-log monitoring for AI crawlers. → [06 · Measurement](06-measurement.md).
- [ ] **Re-verify quarterly.** Every dated claim in this chapter is a snapshot; engines ship fast. Log material shifts in [`updates/`](../updates/README.md).

---

## Sources

**Added 2026-09-23 (cluster review):**

- OpenAI — [API changelog](https://developers.openai.com/api/docs/changelog) (no search/crawler entry in September 2026) · [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) (read via Internet Archive raw mirror, snapshot 2026-09-18)
- Perplexity — [Developer changelog](https://docs.perplexity.ai/changelog.md) (preset citation formats, July 2026) · [Sonar migration guide](https://docs.perplexity.ai/docs/agent-api/migrate-from-sonar/overview)
- Microsoft — [Microsoft 365 roadmap API, item 523223](https://www.microsoft.com/releasecommunications/api/v1/m365?id=523223) · [Manage public web access in Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access) · [Which crawlers does Bing use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0) · [Message Center MC1247902 (community mirror)](https://mc.merill.net/message/MC1247902)
- Google — [Generative AI performance report (Search)](https://support.google.com/webmasters/answer/16984139?hl=en) · [Generative AI performance report (Discover)](https://support.google.com/webmasters/answer/16983858?hl=en)
- DuckDuckGo — [DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot)
- SE Ranking — [AI Mode research (June 2025 sample)](https://seranking.com/blog/ai-mode-research/) · [Google links in AI Mode answers (Feb 2026 sample)](https://seranking.com/blog/google-links-in-ai-mode-answers/) — industry source
- Comscore — [Q2 2026 AI Intelligence Report press release (comscore.com)](https://www.comscore.com/Insights/Press-Releases/2026/9/Comscores-Q2-2026-AI-Intelligence-Report) — industry source

**Primary / official**

- OpenAI — *Crawlers & bots* (GPTBot, OAI-SearchBot, ChatGPT-User, OAI-AdsBot; user-agent strings, IP ranges, opt-out effects). [developers.openai.com/api/docs/bots](https://developers.openai.com/api/docs/bots)
- Perplexity — *Bots* (PerplexityBot, Perplexity-User; strings, IP ranges, robots.txt behavior). [docs.perplexity.ai/guides/bots](https://docs.perplexity.ai/guides/bots)
- Google Search Central — *AI features and your website* (eligibility, "no special markup", Google-Extended, query fan-out, Search Console). [developers.google.com/search/docs/appearance/ai-features](https://developers.google.com/search/docs/appearance/ai-features)
- Anthropic / Claude — *Does Anthropic crawl data from the web…* (ClaudeBot, Claude-User, Claude-SearchBot; strings, IP ranges, robots.txt). [support.claude.com](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
- Microsoft Bing — *Introducing Copilot Search in Bing* (April 2025). [blogs.bing.com](https://blogs.bing.com/search/April-2025/Introducing-Copilot-Search-in-Bing)
- Microsoft Bing Webmaster Tools — *Which crawlers does Bing use?* (Bingbot and the other Bing user-agents). [bing.com/webmasters/help](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0)
- Microsoft Bing Webmaster — *Introducing AI Performance in Bing Webmaster Tools (Public Preview)* (Feb 2026). [blogs.bing.com/webmaster](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)
- Microsoft Learn — *Use public websites to improve generative answers (Copilot Studio; RAG).* [learn.microsoft.com](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/generative-ai-public-websites)
- Pew Research Center — *Google users are less likely to click on links when an AI summary appears in the results* (2025; behavioral study). [pewresearch.org](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)
- Search Engine Journal — *Perplexity Launches Comet Plus, Shares Revenue With Publishers.* [searchenginejournal.com](https://www.searchenginejournal.com/perplexity-launches-comet-plus-shares-revenue-with-publishers/554596/)
- Search Engine Journal — *Anthropic's Claude Bots Make Robots.txt Decisions More Granular.* [searchenginejournal.com](https://www.searchenginejournal.com/anthropics-claude-bots-make-robots-txt-decisions-more-granular/568253/)
- Aggarwal et al. — *GEO: Generative Engine Optimization*, KDD 2024. [arXiv:2311.09735](https://arxiv.org/abs/2311.09735)

**Secondary / industry (useful context; vendors and SEO firms have incentives — treat as reported, not confirmed)**

- Yoast — *What is ChatGPT Search (and how does it use Bing data)?* [yoast.com](https://yoast.com/chatgpt-search/)
- AEO Expert — *How ChatGPT selects and cites sources.* [aeo-expert.nl](https://aeo-expert.nl/en/blog/how-chatgpt-selects-and-cites-sources)
- AI Labs Audit — *How to Get Cited by Perplexity AI in 2026.* [ailabsaudit.com](https://ailabsaudit.com/blog/en/perplexity-guide-maximize-citations)
- Authority Tech — *Perplexity Citations Require Source Depth, Not More Blog Posts.* [authoritytech.io](https://authoritytech.io/curated/perplexity-citations-source-depth-not-more-blog-posts)
- LLM Pulse — *Perplexity Publishers' Program.* [llmpulse.ai](https://llmpulse.ai/blog/perplexity-publishers-program/)
- Search Atlas — *Google AI Mode: How It Works & What It Means for SEO (2026).* [searchatlas.com](https://searchatlas.com/blog/google-ai-mode/)
- Green Flag Digital — *Google AI Overviews vs. AI Mode vs. Gemini.* [greenflagdigital.com](https://greenflagdigital.com/learning-ai/google-ai-overviews-vs-ai-mode-vs-gemini/)
- LLM Pulse — *Bingbot: Microsoft's Web Crawler.* [llmpulse.ai](https://llmpulse.ai/ai-crawler-index/bingbot)
- Microsoft — *Why IndexNow*, Bing Webmaster Tools. [bing.com/indexnow](https://www.bing.com/indexnow). Replaced a Subscribe PR blog post cited here until 2026-09-21: `subscribepr.com` resolves to Netlify and serves a `*.netlify.app` certificate, so the hostname fails validation for every client, not just for the link checker. The primary source says less than the blog did, and the chapter now says what the primary source says.
- tryProfound — *Understanding Grok: WebSearch & DeepSearch.* [tryprofound.com](https://www.tryprofound.com/blog/understanding-grok-a-comprehensive-guide-to-grok-websearch-grok-deepsearch)
- Anthropic — *Web search tool: Citations* (primary source). [platform.claude.com](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)
- This handbook — *Protocol: inline citation density in the smaller answer engines*, observation of 2026-09-13. [protocols/minor-engines-citations.md](protocols/minor-engines-citations.md)

---

> **Contribute:** an engine changed how it cites, exposed a new control, or you measured its behavior? Open a PR ([CONTRIBUTING.md](../CONTRIBUTING.md)) with a dated, sourced update — and add a line to the current [`updates/`](../updates/README.md) week. Correction of any claim here, especially the `needs verification` ones, is exactly the kind of contribution this handbook needs.


---

## Siri AI (Apple) — new, large, and unmeasured

> **Added 2026-09-21.** Apple shipped **Siri AI** on **14 Sep 2026**, *"rolling out today in beta in English"* across **iOS 27, iPadOS 27, macOS 27, watchOS 27 and visionOS 27** ([Apple Newsroom, 14 Sep 2026](https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/)). It answers from the open web — *"Siri AI can also use broad world knowledge to get up-to-date information on virtually any topic"* — on a model layer Apple states is *"custom-built in collaboration with Google and its Gemini models for deeply integrated Apple Intelligence experiences."*

**Why it belongs in this chapter despite having no optimization advice yet.** This is a **default assistant on hundreds of millions of devices**, not a destination users choose — structurally the position AI Overviews holds inside Google. Apple's announcement says nothing about links, sources, citations or publishers, and no independent study of Siri AI's citation behaviour exists.

**Publisher controls.** Apple documents two separate levers ([Apple Support, updated 4 Sep 2026](https://support.apple.com/en-us/119829)):

- **`Applebot-Extended`** — disallow in `robots.txt` to refuse **training** of Apple's generative models, without affecting search appearance. This is the well-behaved control.
- **`nosnippet`** — the opt-out for the answers themselves: *"Web publishers can opt out of their content being used in these broad world knowledge answers by applying the `nosnippet` meta tag to specific content."*

> ⚠️ **Note the asymmetry before anyone reaches for it.** `nosnippet` also removes your ordinary search snippets. Unlike Google's *Search generative AI* control — which Google states *"isn't used as a ranking or inclusion signal affecting other parts of Search"* — Apple offers **no way to leave the AI answers while keeping normal snippet presentation**. For almost every reader the correct action here is **no action**.

**How to optimize for Siri AI.** *Honestly: nobody knows yet.* No vendor guidance, no measured study, no documented citation format. The defensible moves are the ones that are true regardless — don't block `Applebot`, keep pages machine-readable, keep entity identity clean — plus the one that would actually advance the field: **measure it**. A fixed-query observation protocol like [`docs/protocols/minor-engines-citations.md`](protocols/minor-engines-citations.md) applied to Siri AI would produce data nobody has published.

*Last verified: 2026-09-21.*
