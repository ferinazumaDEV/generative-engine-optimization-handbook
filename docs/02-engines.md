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

The single most actionable thing to understand is **which bot does what**, because that determines what you allow or block. As of **2026-08**, the major answer engines run these user-agents:

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

> **The one mistake to avoid:** blocking the *training* bot (`GPTBot`, `ClaudeBot`, `Google-Extended`) is a legitimate rights choice and costs you **nothing** in answer visibility. Blocking the *search* bot (`OAI-SearchBot`, `PerplexityBot`, `Claude-SearchBot`, `Googlebot`, `Bingbot`) makes you **invisible** in that engine's answers. Many sites accidentally do the second while intending the first. Verify your rules per-token. (See [04 · Technical GEO](04-technical.md) for exact `robots.txt` recipes.)

> ⚠️ **needs verification / volatile:** exact user-agent *version numbers* (e.g. `GPTBot/1.4`, `OAI-SearchBot/1.4`) and published IP-range JSON files change over time. Always confirm against the vendor's live docs and their machine-readable IP list (linked in each profile) before hard-coding a rule.

---

## ChatGPT & ChatGPT Search (OpenAI)

> **TL;DR:** A hybrid engine — it blends a Bing search partnership with OpenAI's own `OAI-SearchBot` index, fetches candidate pages, and synthesizes an answer with inline citations. To be eligible you must **allow `OAI-SearchBot`** and, in practice, **be indexed in Bing**.

**Retrieval.** OpenAI launched ChatGPT Search on **31 October 2024**, built on a partnership with Microsoft Bing, and supplements Bing's results with its own crawler, `OAI-SearchBot` ([Yoast overview](https://yoast.com/chatgpt-search/); [OpenAI docs](https://developers.openai.com/api/docs/bots)). When a query needs fresh information, ChatGPT retrieves ranked web results, fetches candidate pages, extracts content, and synthesizes an answer with citations. OpenAI describes a multi-step process: query formulation → retrieve results → select and visit pages → extract content → synthesize with citations.

> ⚠️ **needs verification (evolving):** through 2025–2026, independent trackers report ChatGPT's citations drifting *away* from a pure Bing footprint toward OpenAI's own index and re-ranking (e.g. Profound and Ahrefs measurements circulated widely, but the precise blend is not officially documented). Treat "ChatGPT = Bing" as a useful heuristic, not a fixed fact. Practically: **be strong in Bing *and* allow `OAI-SearchBot`.**

**Citation behavior.** Answers show inline source links and a sources list. Citation is not guaranteed on every answer; ChatGPT cites more when a query is clearly informational and time-sensitive. Independent write-ups note that the pages ChatGPT cites are "not necessarily the largest or best known… they are the websites that provide the best answer to the exact question the user is asking" ([AEO Expert](https://aeo-expert.nl/en/blog/how-chatgpt-selects-and-cites-sources), industry source).

**Crawlers / user-agents.** `OAI-SearchBot` (search indexing — the one that governs ChatGPT Search visibility), `GPTBot` (training), `ChatGPT-User` (live user actions/browsing), `OAI-AdsBot` (ad landing validation). Exact strings and IP lists are published by OpenAI ([docs](https://developers.openai.com/api/docs/bots)). Key official statement: *"Sites that are opted out of `OAI-SearchBot` will not be shown in ChatGPT search answers."*

**Publisher controls.** Allow `OAI-SearchBot` in `robots.txt`; you may independently block `GPTBot` if you don't want to be used for training — this does not affect search visibility. OpenAI publishes IP ranges for each bot for verification. There is no schema or special markup requirement.

**How to optimize for ChatGPT Search.**
- **Get and stay indexed in Bing** (Bing Webmaster Tools, sitemap, IndexNow) — it's the historical backbone and a low-effort, high-leverage move that also feeds Copilot.
- **Allow `OAI-SearchBot`.** Double-check you aren't blocking it while blocking `GPTBot`.
- **Write direct, question-shaped answers.** A page that names the exact user-agent to allow, the file to edit, and the mistake to avoid is easier to lift into an answer than a discursive essay.
- **Freshness and clear entity naming help**, as ChatGPT favors current, specific content for time-sensitive queries.

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

**How to optimize for Perplexity.**
- **Source depth beats content volume.** Getting cited "is not a content-volume problem — it is a source-depth problem": original data, primary sources, specificity ([Authority Tech](https://authoritytech.io/curated/perplexity-citations-source-depth-not-more-blog-posts), industry source).
- **Keep pages fresh and structurally clean** — clear headings, factual, well-attributed.
- **Allow `PerplexityBot`** and monitor server logs for its visits to see what's being indexed.

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

**Crawlers / user-agents.** There is **no AI-specific fetching crawler**: `Googlebot` crawls for the Search index, and the AI features draw from that same index. `Google-Extended` is **not a separate crawler that appears in your logs** — it's a `robots.txt` *token* that lets you opt out of having your already-crawled content used for Gemini/Vertex generative training and grounding.

**Publisher controls (from Google's official [AI features guidance](https://developers.google.com/search/docs/appearance/ai-features)).**
- *"There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary."* A page just needs to be **indexed and eligible to be shown with a snippet.**
- *"You don't need to create new machine readable files, AI text files, or markup to appear in these features. There's also no special schema.org structured data that you need to add."*
- Standard snippet controls apply: `nosnippet`, `max-snippet`, `data-nosnippet` limit what text can be used (but also limit your citation surface — a trade-off).
- **`Google-Extended`** opts you out of Gemini training/grounding **without affecting your Google Search ranking or inclusion** — a genuinely separate lever from Search visibility ([Google crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers); that ranking/inclusion sentence is on the crawlers page, not the AI-features page).
- Clicks from AI features are counted in **Search Console**'s overall search traffic.
- **New (Aug 2026) — the embeddable "Preferred Sources" button.** Publishers can drop in a one-click button (implementation code in Search Central) that lets a reader mark their site as a **Preferred Source**; those sources then get a "preferred" badge and surface more in **Top Stories, AI Overviews, and AI Mode** for that reader. Google reported **600,000+** sources already selected ([Press Gazette, 24 Aug 2026](https://pressgazette.co.uk/platforms/google-preferred-source-article-users-curate-sources-top-stories-ai-overview-search/)). This is Google's first genuinely *publisher-controlled* lever on AI-answer placement — drive reader opt-ins where relevant. Relatedly, Google extended **link carousels for "developing topics"** (already in AI Overviews) into **AI Mode** answers, adding a new inline link slot that surfaces preferred/original-coverage sources ([Search Engine Land, 26 Aug 2026](https://searchengineland.com/google-adds-link-carousels-for-developing-topics-in-ai-mode-485884)).

**How to optimize for Google's AI surfaces.**
- **Win classic Google fundamentals first** — indexing, helpful content, snippet eligibility. AI features are built *on top of* the same index; there is no separate door.
- **Optimize for fan-out, not just your head term.** Cover the *sub-questions* a topic implies; entity-rich passages that name specific tools, stats, and steps score better in passage retrieval.
- **Write self-contained passages** (~40–60 words) that answer one sub-query cleanly, with clear headings around them.
- **Don't reach for special AI markup** — Google explicitly says none is needed. Spend that effort on clarity and coverage instead. (Schema still helps *classic* rich results and entity understanding; see [04 · Technical GEO](04-technical.md).)

*Last verified: 2026-08.*

---

## Microsoft Copilot & Bing

> **TL;DR:** Copilot's web answers ride on the **Bing index** (crawled by `Bingbot`) — there's **no separate Copilot web crawler**. Cite prominently and inline. High-leverage lever: **be in Bing** (which also partly feeds ChatGPT Search) and use **IndexNow** for near-instant freshness.

**Retrieval.** Microsoft introduced **Copilot Search in Bing** in April 2025 ([Bing blog](https://blogs.bing.com/search/April-2025/Introducing-Copilot-Search-in-Bing)). Copilot uses Retrieval-Augmented Generation over the Bing index, separating the steps of *retrieving* search results and *summarizing* them into a cohesive, grounded answer ([Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/generative-ai-public-websites)). Copilot "pulls from the Bing index, crawled by `Bingbot`, with no separate Copilot-specific crawler for web content" ([industry summary](https://llmpulse.ai/ai-crawler-index/bingbot)).

**Citation behavior.** Copilot Search "cites its sources prominently"; sentences and passages are inline-linked so users can navigate to the source, and cited sources plus relevant web results are surfaced alongside the answer ([Bing blog](https://blogs.bing.com/search/April-2025/Introducing-Copilot-Search-in-Bing)). Microsoft's stated citation logic prioritizes **freshness, structural clarity, and demonstrated expertise**, then favors "the cleanest, most trustworthy, most liftable answer."

**Crawlers / user-agents.** `Bingbot` (the same crawler that builds the Bing search index). Bing respects `robots.txt` and the `Crawl-delay` directive.

**Publisher controls & measurement.**
- **Be in the Bing index:** allow `Bingbot`, submit a sitemap, verify in **Bing Webmaster Tools**.
- **IndexNow** (Microsoft's open push protocol) notifies Bing the moment content changes, collapsing indexing lag from days to minutes — meaning Copilot can cite something published *today* ([subscribe PR overview](https://subscribepr.com/blog/how-to-get-indexed-on-bing/), industry source).
- **AI Performance report** (Bing Webmaster Tools, public preview since Feb 2026): shows total citations, cited pages, and "**grounding queries**" — the phrases the AI used to retrieve your content — across Copilot, Bing AI summaries, and select partner integrations ([Bing Webmaster blog](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)). Microsoft frames this explicitly as a step toward **GEO** tooling for publishers. This is one of the few *first-party* AI-citation dashboards available — use it.

**How to optimize for Copilot.**
- **Prioritize Bing indexing and IndexNow** — the highest-leverage, lowest-effort move, and it double-dips into ChatGPT Search.
- **Structure for liftability:** clear headings, definitions, tables; put the answer near the top.
- **Lean into Microsoft-adjacent authority** where relevant (Microsoft Learn, LinkedIn, well-structured docs) — Copilot draws heavily on these.

*Last verified: 2026-08.*

---

## Claude (Anthropic)

> **TL;DR:** Claude can search the web and returns **structured citations with clickable source URLs**. Anthropic separates **training** (`ClaudeBot`), **user fetches** (`Claude-User`), and **search indexing** (`Claude-SearchBot`) into distinct bots — to appear in Claude's answers, **allow `Claude-User` and `Claude-SearchBot`** even if you block training.

**Retrieval.** Claude performs web search on demand and grounds answers in retrieved pages. `Claude-SearchBot` "navigates the web to improve search result quality… It analyzes online content specifically to enhance the relevance and accuracy of search responses," while `Claude-User` fetches specific pages when a user's question requires it ([Anthropic support](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)).

**Citation behavior.** When Claude cites, it returns **structured citations with clickable source URLs**, creating a direct referral path to the source ([ALM Corp](https://almcorp.com/blog/anthropic-claude-bots-robots-txt-strategy/), industry source). Anthropic's move to *three granular bots* (announced 2025) is significant because it lets publishers **opt out of training while staying visible in search** — a distinction not every vendor makes as cleanly ([Search Engine Journal](https://www.searchenginejournal.com/anthropics-claude-bots-make-robots-txt-decisions-more-granular/568253/)).

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

*Last verified: 2026-08.*

---

## Emerging & other engines

The long tail is growing and worth tracking; treat this section as a watchlist rather than settled fact.

- **Grok (xAI)** — built into X, with privileged real-time access to the X timeline plus open-web search. Reporting suggests Grok's WebSearch leans on a **pre-built index** rather than always crawling live at query time ([tryProfound guide](https://www.tryprofound.com/blog/understanding-grok-a-comprehensive-guide-to-grok-websearch-grok-deepsearch), industry source). Strong on real-time social/trending queries. *Crawler user-agent specifics — verify against xAI's current docs.*
- **Meta AI** — deployed across WhatsApp, Instagram, and Facebook (3B+ users), powered by Llama, retrieving from the open web plus Meta's own platform signals. *Meta operates crawlers such as `meta-externalagent`/`meta-externalfetcher` per Meta's docs — confirm exact tokens and behavior before relying on them.* ⚠️ needs verification.
- **DeepSeek** — a reasoning-focused model that integrated web search; popular as a free, uncapped option. Citation/crawler behavior is less documented in English-language sources — ⚠️ needs verification.
- **You.com, Brave (Leo/Answer), Arc/others** — smaller answer engines that, like Perplexity, tend to place **numbered inline citations on nearly every answer** ([aitoolkitpro comparison](https://aitoolkitpro.blog/best-ai-search-engines-2026/), industry source). Lower reach, but often higher citation density and sometimes their own crawlers/controls.

> ⚠️ **needs verification:** the emerging-engine details above lean on secondary sources and move quickly. Before optimizing for any of them, confirm the current crawler tokens, index source, and citation behavior against first-party documentation, and log material changes in [`updates/`](../updates/README.md).

---

## Cross-engine comparison

As of **2026-08**. "Index source" = where answer candidates primarily come from. Verify each cell before betting on it.

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

**Primary / official**

- OpenAI — *Crawlers & bots* (GPTBot, OAI-SearchBot, ChatGPT-User, OAI-AdsBot; user-agent strings, IP ranges, opt-out effects). [developers.openai.com/api/docs/bots](https://developers.openai.com/api/docs/bots)
- Perplexity — *Bots* (PerplexityBot, Perplexity-User; strings, IP ranges, robots.txt behavior). [docs.perplexity.ai/guides/bots](https://docs.perplexity.ai/guides/bots)
- Google Search Central — *AI features and your website* (eligibility, "no special markup", Google-Extended, query fan-out, Search Console). [developers.google.com/search/docs/appearance/ai-features](https://developers.google.com/search/docs/appearance/ai-features)
- Anthropic / Claude — *Does Anthropic crawl data from the web…* (ClaudeBot, Claude-User, Claude-SearchBot; strings, IP ranges, robots.txt). [support.claude.com](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
- Microsoft Bing — *Introducing Copilot Search in Bing* (April 2025). [blogs.bing.com](https://blogs.bing.com/search/April-2025/Introducing-Copilot-Search-in-Bing)
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
- Subscribe PR — *How to get indexed on Bing (IndexNow).* [subscribepr.com](https://subscribepr.com/blog/how-to-get-indexed-on-bing/)
- ALM Corp — *ClaudeBot, Claude-User & Claude-SearchBot: robots.txt strategy.* [almcorp.com](https://almcorp.com/blog/anthropic-claude-bots-robots-txt-strategy/)
- tryProfound — *Understanding Grok: WebSearch & DeepSearch.* [tryprofound.com](https://www.tryprofound.com/blog/understanding-grok-a-comprehensive-guide-to-grok-websearch-grok-deepsearch)
- AI Toolkit Pro — *Best AI Search Engines in 2026.* [aitoolkitpro.blog](https://aitoolkitpro.blog/best-ai-search-engines-2026/)

---

> **Contribute:** an engine changed how it cites, exposed a new control, or you measured its behavior? Open a PR ([CONTRIBUTING.md](../CONTRIBUTING.md)) with a dated, sourced update — and add a line to the current [`updates/`](../updates/README.md) week. Correction of any claim here, especially the `needs verification` ones, is exactly the kind of contribution this handbook needs.
