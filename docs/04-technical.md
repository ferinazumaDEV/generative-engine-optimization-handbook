# 04 · Technical GEO

> Part of **[The GEO Handbook](../README.md)** — a free, community-maintained reference on Generative Engine Optimization. New to the project? Start at the [README](../README.md). Terms are defined once in the [Glossary](09-glossary.md).
>
> *Last substantive review: 2026-08. Time-sensitive figures are dated inline; verify anything marked `⚠️`. Crawler names, user-agents, and engine behaviors change often — this is the fastest-moving chapter in the handbook, so treat dated claims as "as observed then" and re-check the linked primary docs before you act on them.*

This is the plumbing. [Content Strategy](03-content.md) is about writing a passage worth quoting; **Technical GEO is about making sure an engine can *reach* it, *render* it, *parse* it, and is *allowed* to use it.** None of the content work matters if the crawler gets an empty `<div>`, a 404, or a `Disallow`. This chapter covers the controls you actually have.

---

## TL;DR

- **A generative engine can only cite what it can fetch and parse.** The technical job is to be *retrievable* (crawlers can reach you), *renderable* (your content is in the HTML they receive), and *extractable* (the main content isn't buried in scripts and chrome). This is the price of entry for the [retrieval step](01-foundations.md#how-a-generative-engine-turns-your-page-into-a-cited-answer).
- **AI bots split into three jobs:** **training** crawlers (build model datasets — e.g. `GPTBot`, `ClaudeBot`, `Google-Extended`), **search/index** crawlers (build the retrieval index an answer engine queries — e.g. `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`), and **user-triggered** fetchers (grab a page live when a person asks — e.g. `ChatGPT-User`, `Perplexity-User`). You can allow and block these **independently** in `robots.txt`. Blocking training ≠ blocking the search index that gets you *cited*.
- **`robots.txt` is a voluntary standard** ([RFC 9309](https://www.rfc-editor.org/info/rfc9309/)), not a lock. Well-behaved bots obey it; user-triggered fetchers may bypass it because a human initiated the request; and enforcement disputes are real (see the [Perplexity case](#the-enforcement-gap-robotstxt-is-a-request-not-a-lock)).
- **Most AI crawlers do NOT execute JavaScript.** A Vercel + MERJ analysis of ~1.3 billion AI-crawler fetches found *zero* JavaScript execution from GPTBot, ClaudeBot, or PerplexityBot ([Vercel, 2024](https://vercel.com/blog/the-rise-of-the-ai-crawler)). If your main content is client-side rendered, it is effectively invisible to them. **Server-side rendering (SSR) or static generation (SSG) is the single highest-leverage technical fix.**
- **Structured data (schema.org / JSON-LD)** helps machines disambiguate *entities, authorship, dates, and content type*, and it powers classic Google rich results. But the best available test — Ahrefs tracking 1,885 schema-added pages vs. ~4,000 controls — found **no meaningful AI-citation lift** (ChatGPT +2.2%, AI Mode +2.4%, AI Overviews −4.6%) ([Ahrefs/SEJ, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/)). Use it for correctness and entity clarity, not as a citation lever.
- **`llms.txt`** is a real proposed convention, but **as of 2026-08 no major engine (Google, OpenAI, Anthropic, Perplexity) has confirmed using it** for retrieval or citation. Low cost, low risk, no demonstrated ranking effect.
- **Google-Extended controls Gemini training and grounding — NOT your presence in AI Overviews.** AI Overviews are served from the normal Search index via **Googlebot**. Blocking `Google-Extended` does not remove you from AI Overviews; blocking `Googlebot` (or `nosnippet`) does.

---

## The technical GEO stack: four gates

Before any content signal matters, your page has to pass four gates in order. Think of them as a funnel — a failure at any gate zeroes out everything downstream.

| Gate | Question | Fails when… | Fix lives in |
|---|---|---|---|
| **1. Reach** | Can the bot fetch the URL at all? | `robots.txt` blocks it; server 404s/timeouts; login wall | [robots.txt & access](#robotstxt-and-ai-crawler-control) · [speed](#page-speed-and-crawl-efficiency) |
| **2. Render** | Is the content *in the HTML* the bot receives? | Content is injected client-side by JavaScript the bot never runs | [rendering](#rendering-and-crawlability-the-javascript-problem) |
| **3. Extract** | Can the main content be separated from menus/ads/scripts? | Content buried in deeply nested markup, interstitials, or non-semantic HTML | [rendering](#rendering-and-crawlability-the-javascript-problem) · [structured data](#structured-data-schemaorg-and-json-ld) |
| **4. Understand** | Does the machine grasp *what* this is and *who* stands behind it? | No clear entities, authorship, dates, or type signals | [structured data](#structured-data-schemaorg-and-json-ld) · [Authority](05-authority.md) |

The rest of this chapter walks the gates, plus the discovery aids (sitemaps, feeds) and the emerging conventions (`llms.txt`) that sit alongside them.

---

## AI crawlers: the bots you need to know

Different bots do different jobs, and you control them separately. The most consequential mental model in this chapter:

> **Three purposes, three decisions.** For each vendor, a bot may be crawling to **(a) train** a model, **(b) build a search/retrieval index** the answer engine reads, or **(c) fetch a page live** because a user asked. Blocking one does not block the others — and the one that most affects whether you get *cited today* is usually the **search/index** bot, not the training bot.

### Reference table — major AI crawlers (as of 2026-08)

> Verify the exact, current user-agent and IP list from each vendor's own JSON/doc (linked). Vendors publish IP ranges precisely so you can confirm a bot is genuine before allowing it.

| Bot (user-agent token) | Vendor | Purpose | Obeys `robots.txt`? | Official reference |
|---|---|---|---|---|
| `GPTBot` | OpenAI | **Train** foundation models | Yes | [OpenAI bots](https://developers.openai.com/api/docs/bots) · [gptbot.json](https://openai.com/gptbot.json) |
| `OAI-SearchBot` | OpenAI | **Index** for ChatGPT search results | Yes | [OpenAI bots](https://developers.openai.com/api/docs/bots) |
| `ChatGPT-User` | OpenAI | **User-triggered** live fetch (ChatGPT / custom GPT actions) | "may not apply" — user-initiated | [OpenAI bots](https://developers.openai.com/api/docs/bots) |
| `ClaudeBot` | Anthropic | **Train** models | Yes | [Anthropic crawlers](https://support.claude.com/en/articles/8896518) |
| `Claude-SearchBot` | Anthropic | **Index** for Claude's search results | Yes | [Anthropic crawlers](https://support.claude.com/en/articles/8896518) |
| `Claude-User` | Anthropic | **User-triggered** live fetch | Yes | [Anthropic crawlers](https://support.claude.com/en/articles/8896518) |
| `PerplexityBot` | Perplexity | **Index** to surface/link sites in Perplexity | Yes | [Perplexity bots](https://docs.perplexity.ai/guides/bots) |
| `Perplexity-User` | Perplexity | **User-triggered** live fetch | "generally ignores" — user-initiated | [Perplexity bots](https://docs.perplexity.ai/guides/bots) |
| `Google-Extended` | Google | **Train + ground** Gemini (token only, no separate crawler) | Yes (token) | [Google crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers) |
| `Googlebot` | Google | **Index** for Search — *also feeds AI Overviews / AI Mode* | Yes | [Google crawlers](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers) |
| `Applebot-Extended` | Apple | **Train** Apple Intelligence (token only) | Yes (token) | [Apple](https://support.apple.com/en-us/119829) |
| `Bytespider` | ByteDance | **Train** (TikTok/Doubao) | Disputed — treat as untrusted | ⚠️ verify |
| `Meta-ExternalAgent` | Meta | **Train / index** for Meta AI | Yes (claimed) | ⚠️ verify |
| `Amazonbot` | Amazon | **Index** (Alexa / AI answers) | Yes | [Amazon](https://developer.amazon.com/amazonbot) |
| `CCBot` | Common Crawl | **Crawl** open corpus widely reused for AI training | Yes | [Common Crawl](https://commoncrawl.org/ccbot) |

Notes and caveats:

- **Legacy Anthropic tokens.** Older robots.txt files block `anthropic-ai` and `Claude-Web`. Anthropic has since consolidated to the three named bots above; keeping the legacy tokens does no harm but the current controls are `ClaudeBot` / `Claude-SearchBot` / `Claude-User` ([Anthropic](https://support.claude.com/en/articles/8896518); background: [Search Engine Land, 2025](https://searchengineland.com/anthropic-claude-bots-470171)).
- **Microsoft Copilot** doesn't ship a distinctly named public "AI crawler"; its retrieval leans on the **Bing index** (`bingbot`). Blocking `bingbot` therefore affects Copilot the way blocking `Googlebot` affects AI Overviews. `> ⚠️ verify current Copilot retrieval architecture before asserting.`
- **`OAI-AdsBot`** validates the safety of pages submitted as ads on ChatGPT — not a content-retrieval bot ([OpenAI](https://developers.openai.com/api/docs/bots)).
- The **long tail** (e.g. `cohere-ai`, `Diffbot`, `Timpibot`, `DuckAssistBot`, `Omgilibot`) matters mostly for training-data control, not citation. Keep an eye on aggregated bot directories, but confirm any behavior against the vendor's own docs.

### Why the search/index bot is the one to watch

If your goal is **citation** (being named/linked inside an answer), the bot that matters is the **search/index** crawler, because that is what populates the retrieval layer the engine queries at answer time. A common, costly mistake in 2024–25 was blocking *all* AI bots reflexively (often to protest training) and thereby also blocking `OAI-SearchBot` / `PerplexityBot` — removing the site from the very index that produces citations. Decide **training** and **retrieval** separately.

> **Rule of thumb:** if you want the traffic and attribution that comes from being cited, **allow the search/index and user bots** even if you block the training bots. If you want to withhold your content from models entirely, block all three — and accept the visibility cost.

---

## robots.txt and AI crawler control

### The standard

`robots.txt` is a plain-text file at your site root (`https://example.com/robots.txt`) that tells crawlers which paths they may fetch. It was an informal convention from 1994 until the IETF standardized it as **[RFC 9309, the Robots Exclusion Protocol](https://www.rfc-editor.org/info/rfc9309/)** in 2022. Two things about it are essential to understand:

1. **It is per-user-agent.** You write blocks keyed to a bot's token, so you can allow one bot and block another.
2. **It is voluntary.** RFC 9309 is explicit that compliance is cooperative — the rules are "not a form of access authorization." A crawler *can* ignore it. Reputable vendors honor it; that's a norm, not an enforcement mechanism.

### The syntax you actually need

Block a training bot but keep the search/index and user bots (a common "no training, yes citation" stance):

```
# Withhold from model training
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

# ...but stay retrievable and citable
User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

Block *everything* AI (accepting the visibility cost) — list each token explicitly; a bare `User-agent: *` disallow also blocks classic search engines, which you almost never want:

```
User-agent: GPTBot
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: ClaudeBot
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: PerplexityBot
User-agent: Google-Extended
User-agent: Bytespider
User-agent: CCBot
Disallow: /
```

> ⚠️ **Match the token exactly, and date your file.** User-agent tokens are case-insensitive per RFC 9309 but must otherwise match. New bots appear constantly; a `robots.txt` written in 2024 does not know about bots shipped in 2026. Review it on a cadence and confirm tokens against the vendor docs linked above.

> **▶ Reproducible example.** The cookbook has a runnable before/after for this exact gate — the *same* site with a `robots.txt` that blocks AI crawlers vs one that allows them (plus a published `llms.txt`, see [below](#llmstxt-the-emerging-and-unproven-convention)), measured at **0 of 8 canonical AI user-agents allowed vs 8 of 8, and 0 vs 2,868 curated bytes exposed via `llms.txt`**. It is an offline access proxy — a precondition, not a citation measurement, and `llms.txt` consumption is not proven; the recipe's `after/` opens all 8 tested bots, so adapt the allow-list to your own training-vs-search stance above. Clone it and run `reproduce.sh`: [`04-technical/ai-crawler-access`](https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook/tree/main/04-technical/ai-crawler-access).

### The user-triggered exception

The most misunderstood control: **user-triggered fetchers may not obey `robots.txt`.** When a human explicitly asks ChatGPT or Perplexity to read a specific URL, some vendors treat that like a person's browser fetching the page — a proxy for the user, not autonomous crawling — and document that `robots.txt` "may not apply" (`ChatGPT-User`, OpenAI) or is "generally ignored" (`Perplexity-User`, Perplexity) ([OpenAI](https://developers.openai.com/api/docs/bots) · [Perplexity](https://docs.perplexity.ai/guides/bots)). If you need to keep even user-fetched access out, `robots.txt` alone won't do it — you need server-side auth or WAF rules.

### The enforcement gap: robots.txt is a request, not a lock

In **August 2025**, Cloudflare publicly accused Perplexity of **"stealth crawling"** — using undeclared user-agents (posing as a normal Chrome browser on macOS) and rotating IPs/ASNs to fetch content from sites that had blocked its declared bots, generating an estimated 3–6 million such requests per day. Cloudflare responded by de-listing Perplexity as a *verified* bot and blocking the traffic; Perplexity denied the characterization ([Cloudflare, via Search Engine Journal, 2025](https://www.searchenginejournal.com/cloudflare-delists-and-blocks-perplexity-from-crawling-websites/552899/) · [Daring Fireball summary](https://daringfireball.net/linked/2025/08/05/cloudflare-perplexity)).

The takeaway isn't "Perplexity is evil" — it's that **`robots.txt` expresses a preference, and enforcement requires infrastructure.** If you genuinely need to *prevent* access (not merely request that bots abstain), you need edge controls (WAF, bot management, or an infrastructure provider's AI-bot rules), because a disallow line is only as strong as the crawler's willingness to honor it.

### The infrastructure layer: block-by-default and pay-per-crawl

On **1 July 2025**, Cloudflare — which fronts roughly a fifth of the web — became the first major infrastructure provider to **block AI crawlers by default** for new domains, flipping the model from opt-out to opt-in, and launched a **"Pay Per Crawl"** marketplace letting publishers charge AI companies per fetch ([Cloudflare press release, 2025](https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/) · [Search Engine Land](https://searchengineland.com/cloudflare-to-block-ai-crawlers-by-default-with-new-pay-per-crawl-initiative-457708)). Alongside this, an industry effort promotes **"content signals"** — a way for a crawler (or a site) to declare a crawl's *purpose* (train / inference / search) so publishers can decide per-purpose rather than all-or-nothing.

Why this belongs in a GEO chapter: **your host may already be blocking the bots that would cite you.** If you're on Cloudflare (or any provider with AI-bot defaults), check that your *desired* engines are allow-listed. A default block is a silent, invisible reason to be absent from AI answers.

> **Update — Cloudflare tightens the default again (effective 15 September 2026).** Building on its 2025 opt-in flip, Cloudflare announced that for **newly onboarded domains** it will **block the Training and Agent crawler categories by default on ad-bearing pages** while leaving **Search** crawlers allowed — reasoning that an ad signals a page meant for a human. Crucially, **multi-purpose crawlers (e.g. `Googlebot`) are judged across *all* their behaviors**, so blocking "training" can catch a crawler you also rely on for search. Existing domains keep their current settings ([Cloudflare, 1 Jul 2026](https://blog.cloudflare.com/content-independence-day-ai-options/)). The takeaway is unchanged but sharper: **confirm the *search* crawlers you want are allowed** before this default reaches you.

### Standardizing the signal: IETF AIPREF

The ad-hoc, per-vendor tokens (`GPTBot`, `Google-Extended`, `Applebot-Extended`, …) are being pulled toward a **single machine-readable standard**. The IETF **AI Preferences (AIPREF)** working group is drafting a way to declare *purpose-specific* usage preferences — most importantly the split between **`train-ai`** (using content to modify a model's parameters) and **`search`** (linking/excerpting to direct users to the source). As of **19 August 2026**:

- **[`draft-ietf-aipref-vocab-07`](https://datatracker.ietf.org/doc/draft-ietf-aipref-vocab/)** defines the preference *vocabulary* (`train-ai`, `search`). ⚠️ It carries a prominent note that its contents **do not yet reflect working-group consensus** — expect the terms to move.
- **[`draft-ietf-aipref-attach-05`](https://datatracker.ietf.org/doc/draft-ietf-aipref-attach/)** defines how to *attach* those preferences to content: a **`Content-Usage` HTTP response header** (a structured-field dictionary, e.g. `Content-Usage: train-ai=n`) and a parallel **`Content-Usage` rule inside `robots.txt`** (longest-prefix matching, like `Allow`/`Disallow`).

If AIPREF lands, it becomes the clean way to say *"you may crawl me for search/citation but not for training"* — per path — which today's split of training vs. search tokens only approximates. **It is a set of drafts, not a shipped standard;** check the datatracker pages before relying on it. `> ⚠️ pre-consensus / evolving — track the WG documents, don't hard-code the header yet.`

---

## Google-specific controls (and the AI Overviews trap)

Google is a special case because one crawler feeds several products, and the controls are easy to get wrong.

### Google-Extended ≠ AI Overviews

- **`Google-Extended`** is a **robots.txt token only — it has no separate crawler and makes no HTTP requests.** It controls whether your already-crawled content may be used to **train future Gemini models** and for **grounding** (feeding Search-index content to Gemini at prompt time). Google states plainly: *"Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal"* ([Google](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)).
- **AI Overviews and AI Mode are served from the normal Google Search index, crawled by `Googlebot`.** So **blocking `Google-Extended` does *not* remove you from AI Overviews.** The only ways to affect AI Overview *display* have historically been blunt: block `Googlebot` (you leave Search entirely) or use snippet controls (below).

This is the trap: teams block `Google-Extended` believing they've opted out of Google's AI answers, and are surprised to still appear in AI Overviews. The token they wanted governs *training*, not *the answer box*.

### Snippet directives — and the new opt-out toggle

- **`nosnippet` / `max-snippet` / `data-nosnippet`** meta directives *do* apply to AI Overviews and AI Mode — but they also strip your **regular** Search snippet, with the organic click-through cost that implies. Historically there was **no way to opt out of AI features while keeping a normal snippet** ([Search Engine Journal, 2026](https://www.searchenginejournal.com/what-opting-out-of-googles-ai-search-features-means-now/584321/)).
- **New in 2026:** Google introduced a **Search Console toggle** to remove content from **AI Overviews and AI Mode without affecting normal rankings/snippets**, reported effective **17 June 2026** — but, as of that rollout, **available only to a subset of operators (initially UK)**, tied to regulation ([9to5Google, 2026](https://9to5google.com/2026/06/02/google-ai-mode-overviews-opt-out/) · [Search Engine Land, 2026](https://searchengineland.com/google-ai-opt-out-feature-competitors-480375)). `> ⚠️ verify current availability and geography before advising anyone to rely on this toggle — it was geo-limited at launch.`

> **For most GEO practitioners the advice inverts the usual worry:** you almost always want to *be* in AI Overviews, so keep `Googlebot` allowed, keep snippets on, and don't reflexively block `Google-Extended` unless you specifically object to Gemini *training*.

---

## Rendering and crawlability: the JavaScript problem

This is, for many sites, the single biggest and most fixable technical GEO issue.

### The finding: AI crawlers don't run your JavaScript

A joint analysis by **Vercel and MERJ** (December 2024) instrumented real traffic and found that **the major AI crawlers do not execute JavaScript at all**. Across a month they observed roughly **569 million** GPTBot fetches, **370 million** from Anthropic's Claude, and **24.4 million** from PerplexityBot — about **1.3 billion AI-crawler fetches, ~28% of Googlebot's 4.5 billion** — and **zero JavaScript execution** among them ([Vercel, 2024](https://vercel.com/blog/the-rise-of-the-ai-crawler)).

They *do* download JavaScript files (ChatGPT ~11.5% of requests, Claude ~23.8%) — but they read them as text and never run them. The practical consequence:

> **If your main content is injected client-side (a typical single-page app that ships an empty `<div id="root">` and hydrates via JS), most AI crawlers see an empty shell.** The content that would get you cited never enters their pipeline. A page can rank #1 on Google (whose renderer *does* run JS) and be completely invisible to ChatGPT and Claude.

Google is the exception: **`Googlebot` renders JavaScript** using a headless-Chrome, two-phase indexing process, and because `Google-Extended`/Gemini grounding piggybacks on the Search index, Gemini inherits that rendering. **No other major AI engine does** ([Vercel, 2024](https://vercel.com/blog/the-rise-of-the-ai-crawler)).

> ⚠️ This reflects crawler behavior observed in **late 2024 through mid-2026**. Vendors could add rendering later; re-check before assuming a client-rendered site is invisible.

### The fix: server-side rendering or static generation

Make sure the content you want cited is present in the **raw HTML response**, before any JavaScript runs. In order of robustness:

- **Static generation (SSG)** — pre-render pages to HTML at build time. Best for content that doesn't change per-request (docs, articles, marketing pages).
- **Server-side rendering (SSR)** — render HTML on the server per request. Good for dynamic/personalized content.
- **Dynamic rendering / prerendering** — serve a pre-rendered HTML snapshot to bots. A workable stopgap, but a maintenance liability and historically discouraged as a long-term pattern.

**Quick self-test:** fetch your page the way a dumb crawler does and see if the words are there.

```
# If your headline/body text is missing from this output,
# JS-only AI crawlers can't see it either.
curl -sL https://example.com/your-page | grep -i "a distinctive phrase from your content"
```

Or in the browser: **View Source** (not "Inspect" — Inspect shows the *rendered* DOM, which hides the problem). If the content isn't in View Source, it isn't in what most AI crawlers receive.

> **▶ Reproducible example.** The cookbook has a runnable before/after for this exact fix — a client-rendered page vs a server-rendered one with the *same* article, measured at **6 words visible to a no-JS crawler vs 152 (~25×)**. Clone it and run `reproduce.sh`: [`04-technical/ssr-vs-csr-rendering`](https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook/tree/main/04-technical/ssr-vs-csr-rendering).

### Extractability: the main content must be liftable

Even with server-rendered HTML, help the extractor separate signal from chrome:

- Use **semantic HTML** — `<main>`, `<article>`, `<h1>`–`<h3>`, real `<p>`, `<table>`, `<ul>` — not a soup of `<div>`s. Semantics are a strong hint about what the *main content* is.
- Keep the important content **in the initial HTML**, not behind tabs/accordions that only populate on click, lazy-load-on-scroll, or "read more" fetches.
- Don't gate content behind **interstitials, consent walls, or modals** that a non-interactive fetch can't dismiss.
- This dovetails with the chunk-level extractability argument in [Content Strategy](03-content.md) — clean structure serves both the human reader and the machine that lifts a passage.

---

## Structured data: schema.org and JSON-LD

### What it is

**Structured data** is machine-readable metadata you add to a page describing what it *is* — an article, a product, a person, an organization, an event — using the shared vocabulary at **[schema.org](https://schema.org/)**. The recommended encoding is **JSON-LD** (JSON for Linked Data): a `<script type="application/ld+json">` block that states facts (title, author, `datePublished`, price, ratings, entity identifiers) separately from your visible markup. It's Google's preferred format and the easiest for machines to parse deterministically ([Google structured data intro](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)).

Minimal `Article` example:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How generative engines pick sources",
  "author": { "@type": "Person", "name": "Jane Doe", "url": "https://example.com/authors/jane" },
  "datePublished": "2026-08-01",
  "dateModified": "2026-08-20",
  "publisher": { "@type": "Organization", "name": "Example", "url": "https://example.com" }
}
</script>
```

### What it demonstrably does — and what it plausibly does

Two very different levels of evidence, and the handbook keeps them separate:

- **Demonstrated (classic Search):** structured data drives Google **rich results** and helps Google *understand* entities, authorship, and relationships. This is well documented and stable.
- **Plausible (machine understanding for AI):** clean, correct schema gives any machine reader unambiguous facts — *who* wrote this, *when*, *what type* of thing it is, *how* it relates to a known entity. That disambiguation is exactly the kind of signal that helps an engine attribute and trust a passage, and it strengthens the **entity/authority** signals covered in [Authority & Trust](05-authority.md).
- **Tested — no direct citation lift found:** the strongest data point to date cuts *against* the "schema boosts AI citations" hype. An **Ahrefs** analysis tracked **1,885 pages that added JSON-LD schema against ~4,000 control pages over 30 days** and found **no meaningful correlation** with AI visibility: **ChatGPT +2.2%, Google AI Mode +2.4%, and Google AI Overviews −4.6%** (a small decline they *couldn't* attribute to schema) ([Ahrefs, via Search Engine Journal, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/)). Treat any confident *"schema → +20–30% AI citations"* claim (common in vendor posts) as unproven — LLMs read the *rendered text* far more than the JSON-LD block.

> **Honest framing:** implement structured data because it makes your facts *unambiguous and correct for any parser*, powers real Google rich results, and reinforces entity/authorship signals — **not** because it will measurably raise AI citations, which the best available test did not find. See the evidence table in [Content Strategy](03-content.md#first-calibrate-whats-proven-vs-plausible-vs-consensus) for how this ranks against on-page tactics.

> **▶ Reproducible example.** The cookbook has a runnable before/after for this exact technique — the *same* visible article with and without a JSON-LD `@graph`, measured at **0 typed entities / 0 typed facts extractable by a schema.org parser vs 17 / 37**. It is an offline machine-readability proxy (one page, two variants; it does not measure citation — consistent with the Ahrefs finding above). Clone it and run `reproduce.sh`: [`04-technical/structured-data-jsonld`](https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook/tree/main/04-technical/structured-data-jsonld).

### The FAQ / HowTo cautionary tale — date everything

Structured-data *features* get deprecated. Two that GEO guides still over-recommend:

- **`HowTo` rich results** were **removed** by Google in 2023 ([Google, Aug 2023](https://developers.google.com/search/blog/2023/08/howto-faq-changes)).
- **`FAQ` rich results** were narrowed to authoritative government/health sites in 2023, then **fully deprecated on 7 May 2026** — they no longer appear in Google Search at all. Search Console reporting and the Rich Results Test dropped FAQ support in **June 2026**; the Search Console API in **August 2026** ([Search Engine Journal, 2026](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/) · [Google FAQPage docs](https://developers.google.com/search/docs/appearance/structured-data/faqpage)).

The `FAQPage` and `HowTo` *schema types remain valid* — Google says the markup can stay and won't cause problems — but they **no longer produce a Google search feature.** Keeping FAQ markup for machine-readability of a genuine Q&A is fine; adding it *expecting a rich result* is cargo-culting a feature that's gone.

**Structured-data types Google still supports for rich results (as of 2026-08):** Article, Breadcrumb, Carousel, Course, Dataset, Discussion forum, Education Q&A, Event, Image metadata, Job posting, Local business, Math solver, Movie, Organization, Product, Profile page, Q&A (`QAPage`), Recipe, Review snippet, Software app, Speakable, Subscription/paywalled content, Vacation rental, Video ([Google search gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery)). Note FAQ and HowTo are **absent**. `Organization`, `Article`, and `Person`/`ProfilePage` are the most GEO-relevant for establishing *who* and *what*.

---

## llms.txt: the emerging (and unproven) convention

### What it is

**[`llms.txt`](https://llmstxt.org/)** is a proposed convention — introduced by **Jeremy Howard of Answer.AI in September 2024** (v2 published August 2026) — for a Markdown file at your site root that gives LLMs a **curated, token-efficient map of your best content.** The rationale: *"An HTML page wraps its information in navigation, ads, and JavaScript, and converting it back into clean text is difficult and imprecise,"* while LLM context windows are finite and *"every wasted token costs time and money."* The file uses a simple structure — an H1 title, an optional blockquote summary, and H2 sections listing Markdown links to key pages (often with `.md` versions alongside).

It is explicitly **not** `sitemap.xml` (which lists *every* URL for crawlers) and **not** `robots.txt` (which controls *access*). It's a hand-curated "here's the good stuff, cleanly" pointer for LLMs.

### Adoption status — read this before you promise anyone results

> ⚠️ **As of 2026-08, no major AI engine has publicly confirmed that it reads or acts on `llms.txt` for retrieval, ranking, or citation.** Google's Search team (via public comments from **Gary Illyes / John Mueller**) has said it does **not** use or support it. OpenAI, Anthropic, and Perplexity do **not** document it as a visibility or citation signal.

The evidence:

- **It's published but barely read.** An **Ahrefs** study of **137,000 sites** found **28% had published an `llms.txt` file, but 97% of those files were never read** by the bots they're meant for ([Ahrefs, via Search Engine Journal, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/)). Independent monitoring of hundreds of millions of AI-bot visits similarly found only a *negligible* number targeting `llms.txt`. `> ⚠️ adoption-rate figures vary by study/sample; cite the specific study before repeating a number.`
- The clearest **real** value today is **developer documentation**: companies like Stripe, Vercel, Cloudflare, and Anthropic ship `llms.txt`/`llms-full.txt` so that AI *coding assistants* pull correct API details — a genuine, working use case that is *not* the same as "get cited by ChatGPT."

### Verdict

`llms.txt` is **low cost and low risk** — if you already publish clean Markdown docs, adding one is trivial and can help AI coding tools consume your docs. But **do not present it as a proven route to AI-answer citations.** It is a convention hoping for adoption, not an honored standard. Ship it if it's cheap; measure honestly; don't oversell it.

---

## Sitemaps, feeds, and freshness

Discovery still matters: an engine can only index what it finds, and it re-uses the same web-plumbing classic search built.

- **XML sitemaps** (`sitemap.xml`) enumerate your canonical URLs and are a documented discovery channel that AI/search crawlers — `GPTBot`, `OAI-SearchBot`, `ClaudeBot`, `PerplexityBot`, `bingbot` — are reported to use. Keep it complete, canonical, and referenced from `robots.txt` (`Sitemap: https://example.com/sitemap.xml`). Use accurate **`<lastmod>`** dates — they signal freshness, which engines weigh, so don't fake them.
- **RSS / Atom feeds** are the freshness complement: a sitemap gives *coverage* (all URLs), a feed narrows attention to your *newest* items. For frequently-updated sites, run both.
- **Canonicalization.** Use `rel="canonical"` and consistent internal linking so engines don't split signals across duplicate URLs (trailing slashes, tracking params, `http`/`https`, `www`/non-`www`). Ambiguous canonicals dilute which URL gets cited.
- **[IndexNow](https://www.indexnow.org/)** is a push protocol — you ping supporting engines the moment a page changes instead of waiting for a crawl. **Bing, Yandex, Naver, and Seznam support it; Google does not.** Because Microsoft **Copilot** retrieves via the Bing index, IndexNow is a plausible freshness lever for Copilot visibility. The common 2026 setup: XML sitemap for Google, IndexNow for the Bing-family engines, both in parallel. `> ⚠️ "AI engines prioritize sitemaps/IndexNow for citation" is reasoned from how discovery works, not from a controlled study — treat the discovery benefit as established and any citation-lift claim as plausible-not-proven.`

---

## Page speed and crawl efficiency

Speed matters for GEO less as a beauty contest and more as a **delivery guarantee**: a bot that times out, or that wastes its budget on junk URLs, simply gets less of your content.

- **Crawl budget is real and AI crawlers waste a lot of it.** In the Vercel/MERJ data, **~34.8% of ChatGPT fetches and ~34.2% of Claude fetches hit 404s**, with more spent on redirects ([Vercel, 2024](https://vercel.com/blog/the-rise-of-the-ai-crawler)). Every 404/redirect/slow response is budget *not* spent fetching content you want cited. Fix broken links, minimize redirect chains, and return fast `200`s on the pages that matter.
- **Server responsiveness > cosmetic performance.** Since most AI crawlers **don't render**, browser-centric **Core Web Vitals** (LCP/INP/CLS) are largely *irrelevant to what an AI crawler receives* — those measure the rendered client experience the bot never has. What matters to the bot is **TTFB and reliable HTML delivery**: does the server return the full content quickly and without timing out? `> ⚠️ There is no established evidence that Core Web Vitals are an AI-citation ranking factor. Optimize them for humans and classic SEO; for AI crawlers, prioritize fast, complete server responses.`
- **Don't rate-limit the bots you want.** Overly aggressive bot-throttling or WAF rules can starve `OAI-SearchBot`/`PerplexityBot` of your content. If you cap crawl rate, cap it for training bots, not the search/index bots that get you cited.

---

## The technical GEO checklist

A pragmatic, ordered pass. Do the top items first — they have the highest leverage.

1. **Serve content in raw HTML (SSR/SSG).** View Source (or `curl`) must show your main content. This is the #1 fix. → [rendering](#rendering-and-crawlability-the-javascript-problem)
2. **Audit `robots.txt` per-purpose.** Decide training vs. retrieval separately; make sure you are **not** accidentally blocking `OAI-SearchBot` / `Claude-SearchBot` / `PerplexityBot`. → [robots.txt](#robotstxt-and-ai-crawler-control)
3. **Check your infrastructure defaults.** On Cloudflare or similar, confirm your desired AI bots aren't blocked by a platform default or Pay-Per-Crawl setting. → [infrastructure](#the-infrastructure-layer-block-by-default-and-pay-per-crawl)
4. **Don't confuse `Google-Extended` with AI Overviews.** Keep `Googlebot` allowed and snippets on if you want to appear in AI Overviews. → [Google controls](#google-specific-controls-and-the-ai-overviews-trap)
5. **Use semantic HTML and clean main-content structure.** `<main>`/`<article>`/headings; important content not hidden behind clicks. → [extractability](#extractability-the-main-content-must-be-liftable)
6. **Add correct structured data (JSON-LD)** — `Organization`, `Article`, `Person`/`ProfilePage` first. For *correctness and entity clarity*, not as a citation cheat code. → [structured data](#structured-data-schemaorg-and-json-ld)
7. **Keep a complete sitemap with honest `lastmod`**, referenced in `robots.txt`; add a feed for freshness; consider IndexNow for Bing/Copilot. → [sitemaps & feeds](#sitemaps-feeds-and-freshness)
8. **Fix crawl waste.** Kill 404s and redirect chains; ensure fast, reliable server responses (TTFB), especially on your most-citable pages. → [speed](#page-speed-and-crawl-efficiency)
9. **(Optional) Ship `llms.txt`** if you have clean docs — cheap and possibly useful for AI dev tools, but do not expect a citation lift. → [llms.txt](#llmstxt-the-emerging-and-unproven-convention)
10. **Date your work and re-audit.** Crawler tokens and engine behaviors change; put a review on the calendar.

---

## Sources

Primary / official:

- OpenAI — [Bots & crawlers documentation](https://developers.openai.com/api/docs/bots) (`GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `OAI-AdsBot`)
- Anthropic — [How do I block Anthropic's crawlers?](https://support.claude.com/en/articles/8896518) (`ClaudeBot`, `Claude-SearchBot`, `Claude-User`)
- Perplexity — [PerplexityBot / Perplexity-User docs](https://docs.perplexity.ai/guides/bots)
- Google Search Central — [Google crawlers overview & `Google-Extended`](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers)
- Google Search Central — [Changes to HowTo and FAQ rich results (Aug 2023)](https://developers.google.com/search/blog/2023/08/howto-faq-changes)
- Google Search Central — [FAQPage structured data](https://developers.google.com/search/docs/appearance/structured-data/faqpage) · [Structured data search gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) · [Intro to structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- IETF — [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/info/rfc9309/)
- [schema.org](https://schema.org/) · [llmstxt.org](https://llmstxt.org/) · [indexnow.org](https://www.indexnow.org/)
- Cloudflare — [Cloudflare blocks AI crawlers by default / Pay Per Crawl (press release, July 2025)](https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/)

Studies / reporting:

- Vercel + MERJ — [The rise of the AI crawler](https://vercel.com/blog/the-rise-of-the-ai-crawler) (Dec 2024; ~1.3B AI-crawler fetches, zero JS execution, 404/redirect rates)
- Ahrefs, via Search Engine Journal — [AI search myths debunked](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/) (2026; schema-markup test on 1,885+4,000 pages found no meaningful AI-citation effect; llms.txt read-rate; ranking/citation overlap)
- Search Engine Journal — [Cloudflare delists and blocks Perplexity from crawling websites](https://www.searchenginejournal.com/cloudflare-delists-and-blocks-perplexity-from-crawling-websites/552899/) (Aug 2025) · [Google drops FAQ rich results from Search](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/) (2026) · [What opting out of Google's AI search features means now](https://www.searchenginejournal.com/what-opting-out-of-googles-ai-search-features-means-now/584321/)
- Search Engine Land — [Anthropic clarifies how Claude bots crawl sites](https://searchengineland.com/anthropic-claude-bots-470171) · [Cloudflare to block AI crawlers by default / Pay Per Crawl](https://searchengineland.com/cloudflare-to-block-ai-crawlers-by-default-with-new-pay-per-crawl-initiative-457708) · [Google AI opt-out feature](https://searchengineland.com/google-ai-opt-out-feature-competitors-480375)
- 9to5Google — [Google will let websites opt out of AI Mode & Overviews](https://9to5google.com/2026/06/02/google-ai-mode-overviews-opt-out/)
- Daring Fireball — [Cloudflare: Perplexity is using stealth, undeclared crawlers](https://daringfireball.net/linked/2025/08/05/cloudflare-perplexity)

Cross-references within this handbook: [01 · Foundations](01-foundations.md) (the retrieval pipeline) · [02 · The Engines](02-engines.md) (per-engine retrieval & citation) · [03 · Content Strategy](03-content.md) (extractable chunks) · [05 · Authority & Trust](05-authority.md) (entities & E-E-A-T) · [07 · Research & Case Studies](07-research-cases.md).

---

> **Found a token, behavior, or figure that's changed?** This chapter ages fast by design. Open a PR with a dated, linked correction — see [CONTRIBUTING](../CONTRIBUTING.md). The one rule: every claim carries a real source, or it's marked `⚠️ needs verification`.
