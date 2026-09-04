# 05 · Authority & Off-Page

> Part of **[The GEO Handbook](../README.md)** — a free, community-maintained reference on Generative Engine Optimization. New here? Start at the [README](../README.md). Terms are defined once in the [Glossary](09-glossary.md); this chapter builds on the mental model from **[01 · Foundations](01-foundations.md)** and picks up the thread [03 · Content](03-content.md) deliberately left off — the *off-page* half of credibility.
>
> *Last substantive review: 2026-08. Time-sensitive figures are dated inline; verify anything marked `⚠️`. This chapter is the one most polluted by confident, uncited vendor statistics — it is written to separate what is **measured** from what is **folklore**, and it flags aggressively. Treat any single percentage as "as measured then, by that vendor, with that method."*

[Content Strategy](03-content.md) was about the page you control: writing a passage worth quoting. This chapter is about the thing you *don't* directly control — **what the rest of the web says about you, and whether the engine has learned to treat you as a real, trustworthy entity.** It is the harder half, the slower half, and — on the current evidence — the half that matters more.

The organizing idea:

> **On-page work makes a passage *quotable*. Off-page authority makes an engine *willing to quote you at all*.** You can write the perfect chunk, but if the model has never encountered your brand as a real entity, and no source it trusts corroborates you, the perfect chunk loses to a mediocre one from Wikipedia.

---

## TL;DR

- **Off-site brand signals out-correlate on-site link signals with AI visibility — by a wide margin.** In Ahrefs' study of **75,000 brands** (Dec 2025), **YouTube brand mentions (~0.74)** and **branded web mentions (~0.66–0.71)** were the strongest correlates of appearing in ChatGPT, AI Mode, and AI Overviews, while **number of backlinks (~0.2)** and **Domain Rating (~0.27–0.33)** were weak by comparison ([Ahrefs, Dec 2025](https://ahrefs.com/blog/ai-brand-visibility-correlations/)). **These are correlations, not proof of cause** — read the caveat before you act on them.
- **A backlink tells a system where to navigate; a mention tells it what to *trust*.** LLMs are trained on **text, not a link graph** — they learn "brand X is associated with topic Y" from *co-occurrence* across documents, so an **unlinked** mention on a trusted page teaches the model much of what a linked one would ([GrowthX, 2026](https://growthx.ai/learn/branded-co-occurrence-ai-search)). This is the single biggest conceptual break from classic SEO.
- **Engines cite a small, familiar set of high-authority domains disproportionately.** Across large-scale citation studies, **Wikipedia, Reddit, and YouTube** recur at the top — but each engine has a *different favorite*: ChatGPT leans on **Wikipedia** (7.8% of its citations, ~48% of its top-10), Perplexity on **Reddit** (~6.6%, ~47% of its top-10), and Google AI Overviews sits in between, riding its own index ([Profound, 2025, 680M citations](https://www.tryprofound.com/blog/ai-platform-citation-patterns)). *Exact percentages vary wildly between vendors — see the caveat.*
- **There are two ways to "be in the corpus," and they're different.** **Training-time presence** (you're in the data the model learned from — Common Crawl, Wikipedia, Reddit, licensed feeds) shapes what the model *believes by default*; **retrieval-time presence** (you're in the live index the answer engine searches) shapes what it *cites right now*. You influence them with different moves — see [Being present in the corpora](#being-present-in-the-corpora-training-vs-retrieval).
- **Why Wikipedia and Reddit specifically?** Both are structurally privileged: heavily **up-weighted in training** (GPT-3 sampled Wikipedia **3.4×** despite it being ~3% of tokens — [Brown et al., 2020](https://arxiv.org/abs/2005.14165)), **dominant in the search index** engines retrieve from (Reddit appears in ~**97.5%** of Google product-review queries — [Search Engine Land, 2024](https://searchengineland.com/reddit-dominates-google-search-discussions-forums-437501)), and **directly licensed** to the AI vendors (Google–Reddit **$60M/yr**, 2024; OpenAI–Reddit, 2024 — [CJR, 2025](https://www.cjr.org/analysis/reddit-winning-ai-licensing-deals-openai-google-gemini-answers-rsl.php)).
- **Become a disambiguated entity.** A clear, consistent identity the engine can pin down — one canonical name, a Wikidata/knowledge-graph presence, `sameAs` links, consistent facts across the web — is the foundation authority is built on. It's mostly *consensus + mechanism*, not a lab result; adopt it for correctness, hold the magnitude claims loosely `⚠️`.
- **Digital PR is the most actionable off-page lever**, because it manufactures the exact signal that correlates: real editorial mentions in sources the engines already read and trust. The ethics line — earning mentions vs. faking them — is covered in [08 · Future & Ethics](08-future-ethics.md).

---

## First, calibrate: measured vs. folklore

Authority is where GEO advice is least honest. Marketing posts routinely assert precise numbers ("author bios lift citations 60%", "Reddit is 40% of all AI citations") with undisclosed or non-reproducible methods. This handbook's job is to tell you **how much weight each claim actually carries.** The table rates the off-page factors in this chapter by evidence strength.

| Factor | Evidence level | Basis |
|---|---|---|
| **Off-site brand mentions** correlate with AI visibility (more than backlinks) | **Observed at scale** (correlational, single large vendor) | [Ahrefs 75k-brand study, Dec 2025](https://ahrefs.com/blog/ai-brand-visibility-correlations/) — mentions ~0.66–0.74 vs. backlinks ~0.2 |
| **Backlinks / Domain Rating** are *weak* correlates of AI citation | **Observed at scale** (same study) | Ahrefs — `#backlinks` and DR in the low-0.2–0.3 range |
| A handful of **high-authority domains** (Wikipedia/Reddit/YouTube) get cited disproportionately | **Observed at scale** (multiple vendors; magnitudes disagree) | [Profound, 2025](https://www.tryprofound.com/blog/ai-platform-citation-patterns); corroborated directionally elsewhere `⚠️` on exact % |
| **Wikipedia is up-weighted in LLM training** | **Documented** (model papers) | [GPT-3 / Brown et al., 2020, Table 2.2](https://arxiv.org/abs/2005.14165) — 3.4 epochs vs. 0.44 for Common Crawl |
| **Reddit was used as a training *quality filter*** | **Documented** (model paper) | [GPT-2 / Radford et al., 2019](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) — WebText = Reddit-linked pages with ≥3 karma |
| AI vendors have **licensed** Reddit/others for privileged corpus access | **Documented** (business fact) | [CJR, 2025](https://www.cjr.org/analysis/reddit-winning-ai-licensing-deals-openai-google-gemini-answers-rsl.php); [Tom's Guide, 2024](https://www.tomsguide.com/ai/google-strikes-dollar60m-deal-with-reddit-for-ai-training-data-what-you-need-to-know) |
| **Unlinked mentions** carry weight because LLMs read text, not links | **Mechanism + consensus** | Follows from how LMs learn co-occurrence; not isolated in a public controlled test `⚠️` |
| Being a **disambiguated entity** (Wikidata, `sameAs`, consistent facts) raises citation odds | **Consensus + mechanism**; some vendor claims | Aligns with retrieval/grounding mechanics; specific timelines/percentages are vendor-claimed `⚠️` |
| **Digital PR** earns mentions that improve AI visibility | **Plausible** (mechanism + the correlation above) | No controlled GEO study isolates PR as the variable; reasoned from the mention correlation `⚠️` |
| Precise vendor stats ("X% lift from bios/EEAT/schema") | **Needs verification** | Single-vendor, non-reproducible; do not repeat as fact `⚠️` |

> **How to read this table.** *Documented* = written down in a primary source (a model paper, a licensing filing). *Observed at scale* = a large study found a strong pattern, but correlation ≠ cause. *Mechanism + consensus* = not isolated in a public experiment, but it falls out of how the systems work and practitioners agree. *Needs verification* = repeated online, but the primary evidence isn't there — treat as unproven. When in doubt, do the *documented* and *mechanism-sound* things, and **measure the rest on your own brand** ([06 · Measurement](06-measurement.md)).

---

## Why engines cite *some* sources over others

The uncomfortable truth of GEO is that generative engines are not neutral. They cite a small, familiar set of sources far more than the open web's diversity would predict. Understanding *why* tells you what authority actually is in this world. There are **four mechanisms**, and they stack.

### Mechanism 1 — The engine inherits its index's authority

Most answer engines don't reason over the whole web; they **retrieve from an underlying search index and then synthesize** ([mechanism in Foundations](01-foundations.md)). Google's AI Overviews and AI Mode are served from the **normal Search index**; ChatGPT search and Perplexity run their own retrieval but lean heavily on web results. So **whatever ranks and gets surfaced in that index is what's *available* to be cited.**

This is why Reddit's takeover of Google search results matters so much for GEO. A 2024 analysis found Reddit appearing in roughly **97.5% of Google product-review queries** and taking about **two-thirds of the slots** in Google's "Discussions and forums" feature; Reddit's search visibility rose an estimated **1,328%** between mid-2023 and early 2024, and by 2025 it was the **second most-visible site in US Google results, behind only Wikipedia** ([Search Engine Land, 2024](https://searchengineland.com/reddit-dominates-google-search-discussions-forums-437501)). A source that saturates the retrieval index saturates the citations built on top of it.

> **Corollary:** classic SEO didn't die — it became **table stakes for retrieval-time visibility.** Ranking in Google/Bing still gets you *into the pool* an engine draws from. It's just no longer sufficient (or the whole game), and the *ranking factors themselves* now favor forums and encyclopedias in ways that reshape who gets cited.

### Mechanism 2 — Training exposure shapes the model's defaults

Before any live retrieval happens, the model already "believes" things from its training data — and that data is **not sampled evenly.** Two documented examples:

- **Wikipedia is deliberately up-weighted.** In GPT-3's training mix, Common Crawl was 60% of the weight but was seen only **0.44 times** (less than once); **Wikipedia was ~3% of the weight but was sampled 3.4 times** — the highest of any source ([Brown et al., 2020, Table 2.2](https://arxiv.org/abs/2005.14165)). Model builders treat Wikipedia as high-quality signal and let the model see it repeatedly. That's a structural reason Wikipedia-shaped facts are the model's "defaults."
- **Reddit was used as a proxy for human quality.** GPT-2's **WebText** corpus was built by scraping outbound links from Reddit posts **with at least 3 karma** — using human upvotes as a filter for "interesting" pages ([Radford et al., 2019, §2.1](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)). Reddit's fingerprint has been baked into foundation models from the start.

Analyses of the raw crawl corpora reinforce the picture: in a documentation study of **C4** (a cleaned Common Crawl snapshot used to train many models), a surprising share of tokens came from **patents.google.com and Wikipedia**, alongside major news outlets ([Dodge et al., EMNLP 2021](https://aclanthology.org/2021.emnlp-main.98/)). The corpus is dominated by a relatively small set of large, "respectable" domains — and models inherit that skew.

> **Why this matters for you:** you can't edit the training data, but you *can* influence what the next crawl sees (be crawlable — see [04 · Technical](04-technical.md)) and *where* your entity co-occurs with your topics. Training exposure is slow, cumulative, and mostly out of your hands; retrieval exposure (Mechanism 1) is faster and more actionable.

### Mechanism 3 — Corroboration and consensus

When a model synthesizes an answer, agreement across independent sources is a trust signal. A claim that appears consistently across many documents — and that the retriever finds echoed in several retrieved passages — is safer to repeat than a claim found in exactly one place. This is *mechanism-level reasoning*, not a published controlled result (`⚠️`), but it explains a lot of observed behavior: the model gravitates to the **consensus** version of a fact, and sources that state the consensus clearly get quoted for it.

The practical implication is uncomfortable for challenger brands: **being *right* in one well-written page is weaker than being *corroborated* across many.** Off-page presence isn't vanity — it's how you become the corroborated version of your own story.

### Mechanism 4 — Privileged access via licensing

Increasingly, the corpus is not just crawled — it's **bought.** Reddit signed a content-licensing deal with **Google for a reported $60M/year in February 2024**, and a separate deal with **OpenAI in May 2024**, giving both real-time API access to Reddit's content for training and answer-generation ([CJR, 2025](https://www.cjr.org/analysis/reddit-winning-ai-licensing-deals-openai-google-gemini-answers-rsl.php); [Tom's Guide, 2024](https://www.tomsguide.com/ai/google-strikes-dollar60m-deal-with-reddit-for-ai-training-data-what-you-need-to-know); [The Register, 2024](https://www.theregister.com/2024/05/17/reddit_signs_ai_deal/)). Licensing deals with news publishers, Stack Overflow, and others follow the same pattern. You can't buy your way into these — but you *can* be present on the platforms that have (a Reddit presence is, indirectly, a presence in ChatGPT and Gemini).

> **The four mechanisms, stacked.** A source like Wikipedia gets cited because it is (1) dominant in the retrieval index, (2) up-weighted in training, (3) the corroborated consensus, and (4) freely and cleanly licensed/open. That's why toppling it is nearly impossible — and why the realistic play is to *be cited alongside it*, and to *be present in the sources it and the engines draw on.*

---

## The source hierarchy: who actually gets cited

Multiple 2025–2026 studies agree on the *shape* of AI citations even when they disagree on the numbers: a **short head of high-authority domains** (Wikipedia, Reddit, YouTube, LinkedIn, major news, and vertical authorities) plus a **very long tail** where no single domain is large. Profound's analysis of **~680 million citations** (Aug 2024–Jun 2025) shows how differently each engine behaves:

| Engine | Its most-cited domains | Reading |
|---|---|---|
| **ChatGPT** | **Wikipedia 7.8%** of citations (**47.9%** of its top-10), Reddit ~1.8%, Forbes ~1.1% | Leans on **authoritative knowledge bases** |
| **Google AI Overviews** | **Reddit 2.2%** (21.0% of top-10), YouTube ~1.9%, Quora ~1.5% | Balances **professional content + social**, riding the Google index |
| **Perplexity** | **Reddit 6.6%** (**46.7%** of its top-10), YouTube ~2.0%, Gartner ~1.0% | Prioritizes **community discussion** |

Source: [Profound, *AI Platform Citation Patterns*, 2025](https://www.tryprofound.com/blog/ai-platform-citation-patterns) (`.com` domains ~80% of citations; `.org` ~11%).

Two things to take from this:

1. **Match the engine to the source it favors.** If you're optimizing for Perplexity, an authentic Reddit presence is disproportionately valuable; for ChatGPT, a well-maintained Wikipedia/knowledge-base footprint is; for AI Overviews, classic Google ranking plus YouTube. There is no single "AI SEO."
2. **The head is smaller than the hype suggests.** Even the top domain rarely exceeds single-digit percentages of *total* citations; **the long tail — thousands of domains — is where most citations actually land.** Dominating your niche's tail is realistic in a way that "beating Wikipedia" is not.

> ⚠️ **The number wars — read this before quoting any figure.** Vendor studies report Reddit's share of AI citations anywhere from **~1.8%** (Profound, share of *all* citations) to **~40%** (other vendors, usually "share of answers where Reddit appears" or a different engine/method). These are **not the same metric** and cannot be reconciled by picking the biggest number. The **robust, directional facts** — *a few high-authority domains are cited far above their share of the web; Wikipedia/Reddit/YouTube lead; each engine has a different favorite; the tail is long* — are well-supported. Any **single precise percentage** is method-specific and dated: treat it as `needs verification` and cite the study, the metric, and the date, or don't cite it at all.

---

## Backlinks vs. brand mentions in the GEO era

This is the section classic SEOs most need to recalibrate on. In the link-graph world, a **backlink** (a hyperlink from another site) was the atomic unit of authority — PageRank ran on links. In the generative world, the atomic unit is a **mention** — your brand name appearing in text a model reads, *whether or not it's linked.*

### The mechanism: models read text, not links

An LLM doesn't traverse a hyperlink graph to compute authority. It learns, from **co-occurrence across billions of documents**, that "Brand X" belongs near "topic Y." A page that says *"For async transcription, teams often use Otter, Fireflies, and **YourBrand**"* teaches the model that association **even with no hyperlink attached** ([GrowthX, 2026](https://growthx.ai/learn/branded-co-occurrence-ai-search)). This is **branded co-occurrence**: repeated proximity of your name and your topic, across many trusted documents, is what makes a model confident enough to name you.

> **The reframing:** *A backlink tells a search crawler where to navigate. A mention tells a language model what to trust.* In AEO/GEO, **unlinked mentions are a first-class asset**, not the consolation prize they were in SEO.

### The evidence: the Ahrefs 75,000-brand correlation study

The most-cited quantitative anchor for this shift is Ahrefs' December 2025 study correlating dozens of signals with brand visibility in ChatGPT, AI Mode, and AI Overviews (Spearman correlation; domains filtered to DR > 40 with a keyword ≥ 800 monthly searches). The pattern is stark — **the top correlates are all off-site brand signals**, and links trail badly:

| Signal | ChatGPT | AI Mode | AI Overviews |
|---|---|---|---|
| **YouTube brand mentions** | **0.737** | 0.712 | **0.740** |
| YouTube mention impressions | 0.717 | 0.714 | 0.724 |
| **Branded web mentions** | **0.664** | 0.709 | 0.656 |
| Branded anchors | 0.511 | 0.628 | 0.527 |
| Branded search volume | 0.352 | 0.466 | 0.392 |
| Branded traffic | 0.235 | 0.357 | 0.274 |
| **Domain Rating (DR)** | 0.266 | 0.285 | 0.326 |
| **Number of backlinks** | **~0.2** | ~0.2 | ~0.2 |
| Number of site pages | ~0.19 | ~0.19 | ~0.19 |

Source: [Ahrefs, *Top Brand Visibility Factors…*, Dec 12 2025](https://ahrefs.com/blog/ai-brand-visibility-correlations/). The headline that traveled — *"branded web mentions (0.664) beat backlinks (0.218) roughly 3-to-1"* — is the AI Overviews cut ([corroborated in reporting](https://www.businesswire.com/news/home/20260526119691/en/Across-75000-Brands-YouTube-Mentions-Are-the-Strongest-Signal-of-AI-Visibility-New-Ahrefs-Report-Reveals)).

> ⚠️ **The caveat Ahrefs states, and you must repeat:** *correlation is not causation.* The authors are explicit that improving a metric won't automatically boost visibility. Brands that earn lots of editorial mentions are usually *also* the brands with better products, bigger PR budgets, and more real-world salience. **Mentions are a proxy for "this is a real, known brand," not a proven lever you can pull in isolation.** The honest takeaway isn't "spam mentions"; it's "the signals that predict AI visibility are the signals of *genuine market presence* — so build that, and measure your own lift ([Ch. 06](06-measurement.md))."

### What this does and doesn't mean for your link-building

- **Don't abandon links.** Backlinks still drive the classic ranking that gets you into the *retrieval index* (Mechanism 1), and high-authority links often *come with* a mention. They're just no longer the top-line GEO signal.
- **Do count unlinked mentions as wins.** A prominent unlinked mention in a trusted publication is now worth chasing on its own merits — the old SEO instinct to "ask them to add the link" matters less.
- **Do prioritize *branded* over *anchored*.** The data favors mentions of your **brand name** near your topics over exact-match anchor text. Write to be *named*, not just linked.

---

## Entities & knowledge graphs: becoming a "thing" the engine recognizes

Underneath all of this is a prerequisite: the engine has to know **who you are** as a distinct, disambiguated **entity** — not a string of characters that might be your company, a common word, or three different things. Entity clarity is the substrate authority attaches to.

**Entity** — a distinct, identifiable thing (a person, company, product, place, concept) that a knowledge system can recognize and tell apart from others of a similar name. *(See [Glossary](09-glossary.md).)*

### Why entities matter for citation

Generative engines and the search indexes behind them increasingly reason over **entities and their relationships** (Google's Knowledge Graph is the canonical example; LLMs build looser internal associations of the same kind). If the engine can confidently resolve *"YourBrand"* to a single, well-described entity with known attributes, it can retrieve about you, corroborate you, and attribute to you. If it can't disambiguate you, you're noise. Entity recognition is, in effect, a **gate before citation.**

### How to build entity clarity (consensus practices)

These are widely recommended and mechanism-sound. Their *direction* is solid; specific timelines and percentages attached to them online are vendor-claimed and should be held loosely `⚠️`.

- **Pick one canonical name and use it everywhere.** Consistent brand, product, and person names across your site, profiles, and the web reduce ambiguity. Inconsistency ("Acme", "Acme Inc.", "ACME Software") splits your entity.
- **Get into the public knowledge graphs.** A **Wikidata** item (with its stable `Q`-identifier) and, where genuinely warranted, a **Wikipedia** article are the strongest entity anchors — they're up-weighted in training *and* used as grounding references. **Do not fabricate notability**: Wikipedia has [notability standards](https://en.wikipedia.org/wiki/Wikipedia:Notability) and conflict-of-interest rules, and a deleted or spammy article is worse than none. Earn it, don't manufacture it (see [anti-patterns](#anti-patterns-off-page-manipulation-to-avoid)).
- **Use `sameAs` to connect your identities.** In your **Organization**/**Person** schema, `sameAs` links your site to your authoritative profiles (Wikidata, Wikipedia, LinkedIn, Crunchbase, official social accounts). This is an explicit "these are all *me*" statement machines can follow. *(Schema mechanics live in [04 · Technical](04-technical.md); note there that schema is weakly evidenced as a **direct** citation lever — treat it as helping the engine *understand and disambiguate*, not as a ranking cheat.)*
- **State your facts consistently and machine-readably.** Founding date, founders, location, category, what you do — stated the same way across your About page, structured data, and third-party profiles — is how an engine builds a stable, corroborated picture of you.
- **Feed real co-occurrence.** Every time your brand appears near its core topics in trusted text (Mechanism 3), the entity ↔ topic association strengthens. This is where entities and digital PR meet.

> **▶ Reproducible example.** The cookbook has a runnable before/after for this exact technique — the *same* article naming five genuinely ambiguous entities (Michael Jordan, Apple, Python, Amazon, Paris) as bare names vs with `sameAs` links to Wikidata and Wikipedia, measured at **0 of 5 entities resolved to a single canonical Wikidata ID vs 5 of 5**. It is an offline resolvability proxy (N = 5 entities; it does not measure citation, and it checks that each anchor is unique, not that the Q-ID is the right item). Clone it and run `reproduce.sh`: [`05-authority/entity-clarity-sameas`](https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook/tree/main/05-authority/entity-clarity-sameas).

> ⚠️ **On the eye-catching entity stats.** You'll see claims like *"knowledge-panel appearance in 60–180 days"*, *"AI-citation lift in 90–120 days"*, or *"76.95% of AI-cited URLs rank outside the organic top-10."* Some are directionally plausible (yes, AI cites plenty of pages that *don't* rank #1), but they come from single-vendor analyses with undisclosed methods. **Use the practice, not the promised timeline.** Cite these only with the vendor named and a `needs verification` flag.

---

## Digital PR: the most actionable off-page lever

If off-site mentions are what correlate with AI visibility, then the discipline that **earns off-site mentions on purpose** — digital PR — is the most direct thing you can *do* about authority. It manufactures exactly the signal Mechanisms 1–3 reward: your entity, named and corroborated, in sources the engines already crawl, trust, and license.

**What "PR for GEO" looks like in practice:**

- **Earn editorial coverage in high-authority, frequently-cited publications.** A mention in a major outlet, an industry authority, or a respected niche publication does triple duty: it's a mention (co-occurrence), it's often corroborated by other outlets picking up the story, and those outlets are themselves in the citation head.
- **Become a source, not just a subject.** Original data, research, surveys, and expert commentary get *quoted and attributed* — journalists name you, and the resulting passages are the citable, statistic-bearing chunks the [founding GEO study](03-content.md#technique-3--add-the-citable-trio-statistics-sources-quotations) showed engines favor. Responding to journalist requests (HARO-style services) and publishing original research are the highest-leverage tactics.
- **Show up where the corpus lives.** Given the source hierarchy above, an *authentic* presence on **Reddit, YouTube, and the Q&A/community sites** each engine favors puts you in the literal documents the engines read and license. YouTube's role is striking — it's the single strongest correlate in the Ahrefs data — so video where your brand is *named and discussed* is off-page work, not just content marketing.
- **Get listed in the places "best-of" lists and reviewers draw from.** Third-party listicles, comparison sites, and review platforms feed both the retrieval index and the "best X" answers engines love. Being *independently* included (not just self-listed — [that doesn't get you named](03-content.md#ranked-best-of-lists--the-format-with-the-hard-data-and-a-big-caveat)) is the goal.
- **Build the person-entities too.** Founders, spokespeople, and expert authors with real, consistent identities (bylines, profiles, `sameAs`) become entities the engine can attribute to — reinforcing the organization. *(On-page author signals are covered in [03 · Content, Technique 7](03-content.md#technique-7--e-e-a-t-signals-a-model-can-actually-read); the off-page half — being a *recognized* expert elsewhere — is the part that lives here.)*

> **The honest line, and where it's drawn.** Digital PR for GEO is *plausible*, not *proven* — no controlled study isolates "did PR" as the cause of citation lift (`⚠️`). What's solid is the chain: mentions correlate with visibility; PR earns mentions; therefore PR is the reasoned bet. What crosses into manipulation — fake mentions, paid-for astroturfed reviews, sockpuppet Reddit threads, spun press releases at scale — is a **different, riskier activity** that the platforms actively fight and that [08 · Future & Ethics](08-future-ethics.md) treats as a risk, not a tactic. **Earn the mention. Don't fake it.**

---

## Being present in the corpora: training vs. retrieval

"Get into the corpus" is common GEO advice, but it hides a crucial distinction. There are **two corpora**, they're influenced differently, and conflating them leads to wasted effort.

| | **Training corpus** | **Retrieval index** |
|---|---|---|
| **What it is** | The (frozen) data the model learned from — Common Crawl, Wikipedia, Reddit, books, **licensed feeds** | The **live** index the answer engine searches *at query time* (its own crawl, or Google/Bing results) |
| **What it shapes** | The model's **default beliefs** and which entities/facts it "knows" unprompted | Which sources get **cited in a specific answer, today** |
| **Update speed** | Slow — changes only at the next training run; today's edit may surface in a model *years* later, if ever | Fast — a newly crawled/updated page can be cited within days |
| **How you influence it** | Be crawlable when the big crawls run; be present & consistent across the open web so you're *in* the next snapshot; get onto licensed platforms (Reddit, etc.) | Be **retrievable now**: crawlable by the search bots, indexed, ranking, fresh — see [04 · Technical](04-technical.md) |
| **What you *can't* do** | Edit what a shipped model already learned; delete yourself from a past crawl | Force a citation — you can only be *eligible* |

The practical upshot:

- **For "right now" visibility, work the retrieval index.** This is where classic SEO, crawlability, freshness ([03, Technique 6](03-content.md#technique-6--keep-it-fresh)), and technical GEO ([Ch. 04](04-technical.md)) pay off fastest. It's also where blocking the wrong bot silently removes you — remember that **blocking a *training* crawler (e.g. `Google-Extended`) does *not* remove you from the *search/retrieval* path that gets you cited** ([Ch. 04's bot table](04-technical.md#ai-crawlers-the-bots-you-need-to-know)).
- **For long-run "the model just knows us," work the training corpus** — patiently. Consistent entity presence, real mentions, and being on the platforms that get licensed compound over training generations. You are, in effect, lobbying the *next* model.
- **Roughly 85% of brand mentions in AI answers reportedly come from third-party pages, not the brand's own domain** ([AirOps, 2026](https://growthx.ai/learn/branded-co-occurrence-ai-search)) `⚠️ vendor figure — verify`. Even if the exact number is soft, the direction is the theme of this whole chapter: **your authority is mostly built on other people's pages.**

---

## The off-page authority checklist

A pass to run at the brand/entity level (not the page level — that's the [content checklist](03-content.md#the-content-optimization-checklist)). None is a magic bullet; together they build the off-page half of citability.

- [ ] **One canonical name**, used consistently across your site, profiles, and the web.
- [ ] **Entity anchors in place:** Wikidata item (earned, accurate), Wikipedia article *only if genuinely notable*, complete authoritative profiles (LinkedIn, Crunchbase, industry directories).
- [ ] **`sameAs` links** in Organization/Person schema tying all your identities together ([mechanics: Ch. 04](04-technical.md)).
- [ ] **Consistent core facts** (founding, location, category, what you do) stated the same way everywhere, machine-readably.
- [ ] **A digital-PR engine** earning real editorial mentions — original data/research, expert commentary, journalist responses.
- [ ] **Presence where the corpus lives:** authentic participation on the community/video platforms each target engine favors (Reddit, YouTube, Q&A sites).
- [ ] **Independent third-party inclusion** in reviews, comparisons, and "best-of" lists (earned, not self-serving).
- [ ] **Named person-entities** (founders/experts) with consistent, verifiable identities on and off your site.
- [ ] **Crawlability confirmed** so the next training crawl and the live retrieval bots can actually see you ([Ch. 04](04-technical.md)) — the right *search/index* bots allowed, not just the training ones.
- [ ] **Measurement in place** — track your mention volume *and* your AI-answer share of voice, and watch them move together ([Ch. 06](06-measurement.md)).
- [ ] **Nothing on this list faked** — every mention, review, and entry earned. (See anti-patterns.)

---

## Anti-patterns: off-page manipulation to avoid

The flip side of "authority is earned off-page" is a strong temptation to *manufacture* it. These backfire, invite detection, and cross into the harms of [08 · Future & Ethics](08-future-ethics.md):

- **Astroturfed community presence.** Sockpuppet Reddit threads, fake "which tool should I use?" posts naming your brand, coordinated upvotes. Platforms fight this hard, users spot it, and a poisoned community reputation is very hard to reverse. Reddit's value to engines is *authenticity*; faking it destroys the thing you're trying to borrow.
- **Bought or fabricated reviews and mentions.** Paid-for "editorial," fake review-site entries, or mass-spun press releases create mentions with no real market behind them. They're increasingly detectable, often illegal (e.g. undisclosed paid endorsement rules), and a fragile foundation.
- **Manufactured Wikipedia/Wikidata entries.** Creating a self-serving article on a non-notable entity violates Wikipedia's [notability](https://en.wikipedia.org/wiki/Wikipedia:Notability) and conflict-of-interest policies; it gets deleted, and the attempt can itself become a negative story. Entity presence has to be *warranted*.
- **Link/mention schemes (the PBN reflex).** Private blog networks and mention farms recreate the exact spam pattern search engines spent two decades learning to discount — now with even weaker payoff, since links aren't the top AI signal anyway.
- **Chasing vanity mentions with no topical co-occurrence.** A mention that doesn't sit near your actual topics teaches the model little. Relevance and context beat raw mention count.
- **Confusing "block training" with "protect brand."** Blocking `GPTBot`/`Google-Extended` doesn't build authority and may cut you out of future models while doing nothing about how you're cited *today* — a self-inflicted wound dressed up as strategy. Decide crawler access deliberately ([Ch. 04](04-technical.md)).

> **The through-line:** every anti-pattern here is an attempt to *simulate* the genuine-market-presence signal that Mechanisms 1–4 reward. The systems are increasingly good at telling simulated from real, and the real version is also just… good business. Build the actual authority.

---

## Where to go next

- **[03 · Content Strategy](03-content.md)** — the on-page half of credibility: extractable chunks, the citable trio, and the author/E-E-A-T signals a model can read on *your* page.
- **[04 · Technical GEO](04-technical.md)** — crawlability, the train-vs-search-vs-user bot distinction, `sameAs`/schema mechanics, and why blocking the wrong crawler removes you from the retrieval path that this chapter's authority feeds into.
- **[06 · Measurement](06-measurement.md)** — how to track your *mention volume* and your *AI-answer share of voice* together, so you can test the correlational claims here on your own brand instead of trusting them.
- **[02 · The Engines](02-engines.md)** — the per-engine differences (ChatGPT ↔ Wikipedia, Perplexity ↔ Reddit, AI Overviews ↔ Google index) that decide *which* off-page presence pays off for *which* engine.
- **[08 · Future & Ethics](08-future-ethics.md)** — where the line sits between earning authority and faking it, and why the manipulation shortcuts are a risk, not a tactic.

---

## Sources

Documented primary sources (model papers, licensing reporting) first, then large-sample observational studies, then mechanism/consensus references. Single-vendor and non-reproducible figures are flagged in-text as `⚠️`. All links verified as of 2026-08. **Special caution for this chapter:** the web is saturated with confident, uncited authority stats — if you add one, bring its primary source and its *metric definition*, because the same word ("citations") means different things in different studies.

- **Brown, T. B., et al. (2020). *Language Models are Few-Shot Learners* (GPT-3).** — training-mix weighting; Wikipedia sampled 3.4 epochs vs. Common Crawl 0.44 (Table 2.2). [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- **Radford, A., et al. (2019). *Language Models are Unsupervised Multitask Learners* (GPT-2).** — WebText built from Reddit-linked pages with ≥3 karma, as a human-quality filter (§2.1). [OpenAI PDF](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- **Dodge, J., Sap, M., et al. (2021). *Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus* (C4). EMNLP 2021.** — composition of a widely-used training corpus; dominance of a small set of large domains (patents, Wikipedia, news). [ACL Anthology](https://aclanthology.org/2021.emnlp-main.98/) · [arXiv:2104.08758](https://arxiv.org/abs/2104.08758)
- **Columbia Journalism Review (2025). *Reddit Is Winning the AI Game.*** — Reddit's licensing deals with Google and OpenAI and their strategic role in AI answers. [cjr.org](https://www.cjr.org/analysis/reddit-winning-ai-licensing-deals-openai-google-gemini-answers-rsl.php)
- **Tom's Guide (2024). *Google strikes $60M deal with Reddit for AI training data.*** — the Feb 2024 Google–Reddit content-licensing deal. [tomsguide.com](https://www.tomsguide.com/ai/google-strikes-dollar60m-deal-with-reddit-for-ai-training-data-what-you-need-to-know) · corroborating: [The Register (OpenAI–Reddit, May 2024)](https://www.theregister.com/2024/05/17/reddit_signs_ai_deal/)
- **Search Engine Land (2024). *Reddit shown excessively in Google product review search results, study finds.*** — Reddit in ~97.5% of product-review queries; ~two-thirds of "Discussions and forums" slots; visibility surge. [searchengineland.com](https://searchengineland.com/reddit-dominates-google-search-discussions-forums-437501)
- **Ahrefs (Dec 12, 2025). *Top Brand Visibility Factors in ChatGPT, AI Mode, and AI Overviews* (75,000 brands).** — the correlation table: off-site brand mentions (~0.66–0.74) vs. backlinks/DR (~0.2–0.33); explicit correlation-≠-causation caveat. [ahrefs.com/blog/ai-brand-visibility-correlations](https://ahrefs.com/blog/ai-brand-visibility-correlations/) · reporting: [BusinessWire](https://www.businesswire.com/news/home/20260526119691/en/Across-75000-Brands-YouTube-Mentions-Are-the-Strongest-Signal-of-AI-Visibility-New-Ahrefs-Report-Reveals)
- **Profound (2025). *AI Platform Citation Patterns* (~680M citations, Aug 2024–Jun 2025).** — per-engine most-cited domains (ChatGPT↔Wikipedia, Perplexity↔Reddit, AI Overviews↔mixed). [tryprofound.com](https://www.tryprofound.com/blog/ai-platform-citation-patterns)
- **GrowthX (2026). *Unlinked Brand Mentions & Branded Co-occurrence in AI Search.*** — mechanism: LLMs read text not links; unlinked mentions and co-occurrence teach entity↔topic association; the AirOps "~85% of mentions from third-party pages" figure (`⚠️ vendor`). [growthx.ai](https://growthx.ai/learn/branded-co-occurrence-ai-search)
- **Google. *Search Quality Rater Guidelines — E-E-A-T* (context for authority/trust framing).** [developers.google.com](https://developers.google.com/search/blog/2022/12/google-raters-guidelines-e-e-a-t)
- **Wikipedia. *Notability* and conflict-of-interest guidelines** (for the "earn, don't manufacture" entity point). [en.wikipedia.org/wiki/Wikipedia:Notability](https://en.wikipedia.org/wiki/Wikipedia:Notability)
- **Aggarwal, P., et al. (2024). *GEO: Generative Engine Optimization.* KDD 2024** (the field's founding controlled study; the "cite sources / statistics / quotations" winners that digital PR manufactures off-page). [arXiv:2311.09735](https://arxiv.org/abs/2311.09735)

> **Found an error, a dead link, or a newer study?** This chapter is meant to be corrected — and authority is the topic most prone to unsourced folklore. See [CONTRIBUTING.md](../CONTRIBUTING.md): every claim carries a real source or an honest `⚠️ needs verification` flag. If you add an authority statistic, bring its **primary source and its exact metric definition** — half the disagreements in this field are two studies measuring different things and calling them the same word.
