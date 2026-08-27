# 07 · Research & Case Studies

> Part of **[The GEO Handbook](../README.md)** — a free, community-maintained reference on Generative Engine Optimization. New to the project? Start at the [README](../README.md). Terms are defined once in the [Glossary](09-glossary.md); this chapter is the *evidence base* the rest of the handbook points back to for proof.
>
> *Last substantive review: 2026-08. Time-sensitive figures are dated inline; verify anything marked `⚠️`. This is the chapter where numbers live, so it is written to be paranoid about them: every figure names its **study, sample size, method, and metric definition**, and rates how much weight it actually carries. Two studies that both say "citations" often mean different things — read the metric, not just the percentage.*

Every other chapter makes claims. This one shows the receipts. It collects the **primary literature** (peer-reviewed research), the **large-scale observational studies** (mostly industry, mostly correlational), the **behavioral evidence** (how people actually use AI answers), and the **before/after examples** — and, for each, tells you how strong the evidence really is.

The organizing principle:

> **A number is only as good as its method.** The single most valuable skill in GEO is telling *demonstrated* (measured in a controlled test) from *observed at scale* (a big correlation, cause unknown) from *anecdotal* (one agency's blog post). This chapter labels every entry so you can weight it correctly — and so guidance elsewhere in the handbook can cite *here* instead of repeating an unsourced stat.

---

## TL;DR

- **The field has exactly one founding controlled study, and it is strong.** *GEO: Generative Engine Optimization* (Aggarwal et al., **KDD 2024**) built a 10,000-query benchmark and showed that specific content edits raise a source's visibility in AI answers by **up to ~40%** — with **adding citations, quotations, and statistics** as the clear winners and **keyword stuffing** as a clear loser ([arXiv:2311.09735](https://arxiv.org/abs/2311.09735)).
- **The winning tactics are counter-intuitive.** The paper's top three methods — **Cite Sources, Quotation Addition, Statistics Addition** — lifted the position-adjusted word-count metric **30–40%**. Making writing *more persuasive/authoritative* did **not** help significantly, and **keyword stuffing performed worse than doing nothing**.
- **GEO helps the underdog most.** For a source ranked **#5** in the underlying search results, adding citations raised its visibility in the synthesized answer by **+115.1%**, while the #1 source's visibility *fell* ~30% — evidence that answer engines re-shuffle who gets seen ([Aggarwal et al., 2024, Table 2](https://arxiv.org/abs/2311.09735)).
- **It replicated on a real engine.** Re-run on **Perplexity.ai** (200-sample subset), the same methods held: **Quotation Addition +22%**, **Statistics Addition +37%** on the two metrics; **keyword stuffing came in ~10% *below* baseline**.
- **The academic literature beyond that is thin and young** — the most-cited follow-up is an *adversarial* paper showing conversational search engines can be **manipulated by injected content** ([Pfrommer et al., EMNLP 2024](https://arxiv.org/abs/2406.03589)). Most 2025–2026 "GEO research" is **industry**, not peer-reviewed: bigger samples, weaker methods.
- **The big industry studies agree on the shape, disagree on the digits.** Across **680M citations**, engines lean on a small set of familiar domains — ChatGPT ↔ **Wikipedia (7.8%)**, Perplexity ↔ **Reddit (6.6%)** ([Profound, 2025](https://www.tryprofound.com/blog/ai-platform-citation-patterns)). Across **75,000 brands**, **off-site brand mentions out-correlate backlinks** with AI visibility by a wide margin — *but the authors themselves flag correlation ≠ causation* ([Ahrefs, Dec 2025](https://ahrefs.com/blog/ai-brand-visibility-correlations/)).
- **Some popular tactics don't survive testing.** Ahrefs found **JSON-LD schema markup had no meaningful effect** on AI citations (1,885 test pages), and **97% of `llms.txt` files were never read** (137,000 sites) ([SEJ / Ahrefs, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/)).
- **The behavioral shift is measured, not hype.** In a Pew panel of **68,879 real searches**, users clicked a result **8% of the time when an AI summary appeared vs. 15% without**, and clicked a link *inside* the summary just **1%** of the time ([Pew Research, 2025](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)).
- **Rigorous, independent before/after brand case studies barely exist.** Most "we 5×'d our citations" posts are vendor self-reports with no control. This chapter treats the founding paper's controlled experiment as the gold-standard before/after and holds agency case studies to a stated bar — see [what a credible case study needs](#what-a-credible-case-study-must-include).

---

## How to read the evidence in this handbook

GEO advice online is a firehose of confident percentages with undisclosed methods. This handbook rates every empirical claim on a fixed ladder. When two chapters disagree, the one citing the higher tier wins.

| Tier | Label | What it means | Trust it for |
|---|---|---|---|
| 1 | **Demonstrated** | Measured in a controlled experiment with a stated method (ideally reproducible / peer-reviewed) | Cause-and-effect claims |
| 2 | **Observed at scale** | A large dataset shows a strong pattern, but cause is unproven (correlational) | Direction and priority, *not* causation |
| 3 | **Behavioral** | Directly measured human behavior (panels, clickstream) — real, but describes *users*, not *ranking mechanics* | "Why GEO matters" / landscape |
| 4 | **Documented** | Written down in a primary source (a model paper, a licensing filing, official docs) | Facts about how systems were built |
| 5 | **Anecdotal** | One practitioner/agency/vendor result, no control, often incentivized | Hypotheses to test yourself — never as proof |
| — | **`⚠️ Needs verification`** | Repeated online but the primary evidence isn't there | Nothing, until sourced |

> **Rule of thumb:** *do* the things at Tiers 1 and 4 (they're demonstrated or documented), *prioritize* by Tier 2 (correlations point you in the right direction), and *test Tier 5 on your own brand* before believing it. Measurement method for that self-test lives in **[06 · Measurement](06-measurement.md)**.

---

## Part 1 — The founding study: *GEO* (Aggarwal et al., KDD 2024)

This is the paper that named the field and remains its single strongest piece of evidence. If you read one primary source, read this one. **Tier 1 — Demonstrated** (controlled, peer-reviewed, code + data released).

### The paper at a glance

| Field | Detail |
|---|---|
| **Title** | *GEO: Generative Engine Optimization* |
| **Authors** | Pranjal Aggarwal, Vishvak Murahari (equal contribution), Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, Ameet Deshpande |
| **Affiliations** | **IIT Delhi** (Aggarwal); **Princeton University** (Murahari, Narasimhan, Deshpande); independent (Rajpurohit, Kalyan) |
| **Venue** | **KDD 2024** — 30th ACM SIGKDD Conference, Barcelona, 25–29 Aug 2024 |
| **Posted** | arXiv v1 16 Nov 2023 · v3 28 Jun 2024 |
| **Model used** | **GPT-3.5-turbo** for all experiments |
| **Headline** | Content edits can boost a source's visibility in AI answers **by up to ~40%** |
| **Links** | [arXiv:2311.09735](https://arxiv.org/abs/2311.09735) · [PDF](https://arxiv.org/pdf/2311.09735) · [DOI:10.1145/3637528.3671900](https://doi.org/10.1145/3637528.3671900) · [project page + data](https://generative-engines.com/GEO/) · [code (GitHub)](https://github.com/GEO-optim/GEO) |

### What they built: GEO-bench and two ways to measure "visibility"

You can't optimize what you can't measure, and "impressions" from classic SEO don't map onto a paragraph-length AI answer. The paper's lasting contribution is arguably its *measurement apparatus*.

- **GEO-bench** — a benchmark of **~10,000 queries** drawn from **nine sources** and tagged across **25 domains** (Arts, Health, Games, Law & Government, Science, Business, and more), plus difficulty and query-intent labels. Sources include real search queries (**MS MARCO, ORCAS-1, Natural Questions**), harder synthesis/reasoning sets (**AllSouls** Oxford essay questions, **LIMA**, **Davinci-Debate**, **ELI5**), and live **Perplexity.ai Discover** queries. This mix is why the results claim to generalize beyond simple factual lookups.
- **Position-Adjusted Word Count** — an *objective* visibility metric: how many words of the answer come from your source, **discounted by how far down** the citation appears (a quote up top counts more than one buried at the bottom).
- **Subjective Impression** — a *subjective* metric scored by an LLM across **seven dimensions**: **relevance, influence, uniqueness, diversity, follow-up likelihood, subjective position, and subjective count**. It captures the intuition that a citation can be prominent and persuasive even when it isn't word-heavy.

> **Why two metrics matter for you:** they measure different things. A method can win on word-count share but not on subjective prominence, or vice-versa. When a vendor says a tactic "improved citations by X%," your first question should be *"which metric?"* — this paper is the reason that question exists.

### The nine methods they tested

Each method is a small, automated rewrite of a source page. Note that only three of them (**Keyword Stuffing, Cite Sources, Quotation Addition**) meaningfully change *what information* is present — the rest change *presentation*.

| # | Method | What it does | Verdict |
|---|---|---|---|
| 1 | **Cite Sources** | Adds citations to credible sources | ✅ **Top performer** |
| 2 | **Quotation Addition** | Adds relevant quotes from credible sources | ✅ **Top performer** |
| 3 | **Statistics Addition** | Adds relevant statistics/numbers | ✅ **Top performer** |
| 4 | **Fluency Optimization** | Improves the fluency of the text | ✅ Solid (+15–30%) |
| 5 | **Easy-to-Understand** | Simplifies the language | ✅ Solid (+15–30%) |
| 6 | **Authoritative** | Rewrites in a more persuasive/authoritative tone | ➖ No significant gain |
| 7 | **Technical Terms** | Adds technical terminology | ➖ Marginal |
| 8 | **Unique Words** | Adds uncommon words | ➖ Marginal |
| 9 | **Keyword Stuffing** | Adds more query keywords (classic SEO) | ❌ **No gain / worse than baseline** |

### The headline results

Across GEO-bench, **the best method beat the unoptimized baseline by 41% on Position-Adjusted Word Count and 28% on Subjective Impression** ([Table 1](https://arxiv.org/abs/2311.09735)). Breaking it down:

| Method group | Position-Adjusted Word Count | Subjective Impression | Reading |
|---|---|---|---|
| **Cite Sources / Quotation / Statistics** (top 3) | **+30–40%** | **+15–30%** | Adding *verifiable substance* — a source, a quote, a number — is the strongest lever, and it's cheap. |
| **Fluency / Easy-to-Understand** | **+15–30%** | +15–30% | *Presentation* matters on its own: engines reward clarity even with no new facts. |
| **Authoritative** | ~no significant gain | ~no significant gain | Just *sounding* confident doesn't move a grounded engine. |
| **Keyword Stuffing** | little/none | little/none | The classic SEO reflex **fails** here — sometimes worse than doing nothing. |

> **The one sentence to remember:** the tactics that win in AI answers are the ones that make a passage **more verifiable and more readable** — cite a source, quote an authority, add a statistic, write clearly. The tactics that won the last era of SEO (keyword density, persuasive puffery) do little. This is the empirical heart of the whole handbook; **[03 · Content Strategy](03-content.md)** turns it into a writing method.

### GEO is a democratizing force: it helps low-ranked sources most

The paper's most striking table looks at *which* sources benefit. When methods are applied to sources at different search-result ranks, the payoff is inverted relative to classic SEO:

| Source's rank in underlying search | Effect of **Cite Sources** on answer visibility |
|---|---|
| **#5** (bottom of the pack) | **+115.1%** |
| **#4** | +15.5% |
| **#3** | +20.4% |
| **#1** (already on top) | **−30.3%** (on average, top source *loses* share) |

> **Why this matters:** an answer engine synthesizes from several sources, so it can pull a well-optimized #5 into the spotlight and leave a lazy #1 on the sidelines. For a small creator, that's the opportunity in one number: **you don't have to rank first to be quoted.** ([Aggarwal et al., 2024, Table 2](https://arxiv.org/abs/2311.09735)) `⚠️ Note:` this is measured against 2023-era GPT-3.5 retrieval; treat the *direction* as robust and the exact magnitude as era-specific.

### The effect is domain-specific

No single tactic wins everywhere. The paper reports the top-performing domains for each method — useful if you know your niche:

| Method | Works best in… |
|---|---|
| **Cite Sources** | Statement-type, Factual, Law & Government |
| **Statistics Addition** | Law & Government, Debate, Opinion |
| **Quotation Addition** | People & Society, Explanation, History |
| **Authoritative** | Debate, History, Science |
| **Fluency Optimization** | Business, Science, Health |

The practical takeaway the authors draw: **match the tactic to the query type.** A statistics-heavy rewrite pays off for a policy/finance page; quotes pay off for narrative/historical content.

### Methods stack

Content owners will use several tactics at once, so the paper tested combinations of the top four. The best pair — **Fluency Optimization + Statistics Addition** — beat any single method by **>5.5%** (on a 200-sample subset), and **Fluency Optimization was the best "team player,"** averaging **~31%** improvement when combined with others despite being weaker alone. Lesson: **write clearly *and* add substance; the combination compounds.**

### It replicated on a live engine (Perplexity.ai)

To rule out "this only works on our toy engine," the authors re-ran the methods against **Perplexity.ai** — a commercially deployed generative engine — on a 200-example subset (**Tier 1, but smaller n**). The pattern held:

| Method | Position-Adjusted Word Count | Subjective Impression |
|---|---|---|
| **Quotation Addition** | **+22%** (best on this metric) | +~30% |
| **Statistics Addition** | +~9% | **+37%** (best on this metric) |
| **Cite Sources** | up to +9% | up to +37% |
| **Keyword Stuffing** | **−10%** (worse than baseline) | — |

> The replication is the reason to trust the founding study more than any single vendor blog: the same intervention, tested on an engine the authors didn't build, moved the needle the same way — and the classic-SEO tactic *backfired* the same way.

### How to read this paper's limits (so you cite it honestly)

The founding study is strong, but it is not the last word — and pretending otherwise is exactly the kind of over-claiming this handbook exists to avoid:

- **It's from the GPT-3.5 era (2023).** Engines, retrieval stacks, and citation UIs have changed a lot by 2026. The *mechanisms* (verifiable substance wins) are durable; the *exact percentages* are a snapshot.
- **The metrics are proxies.** Position-Adjusted Word Count and LLM-scored Subjective Impression are reasonable stand-ins for "visibility," but they are not click-throughs or conversions. Business impact is a further inference.
- **The generative engine in the main experiments was one the authors built** (GPT-3.5 over a retrieval set), with Perplexity as a secondary check. Real engines are more complex and more varied — see **[02 · The Engines](02-engines.md)**.
- **"Up to 40%" is a ceiling, not an average.** It's the best method on the best metric. Quoting it as a typical result overstates it.

---

## Part 2 — Research building on GEO (the wider literature)

Beyond the founding paper, the *peer-reviewed* literature specifically on GEO is still small in 2026 — which is itself worth knowing, because it means most numbers you'll see online come from industry, not from replicated science.

### The adversarial angle: conversational search engines can be manipulated

**Tier 1 — Demonstrated (adversarial).** *Ranking Manipulation for Conversational Search Engines* (Pfrommer, Bai, Gautam, Sojoudi — **EMNLP 2024**, [arXiv:2406.03589](https://arxiv.org/abs/2406.03589)) is the most-cited academic follow-up, and it approaches GEO from the security side. The authors show that an attacker can **inject adversarial text into a website** to reliably promote a **low-ranked product** in a conversational search engine's answer, using a *tree-of-attacks* jailbreaking technique — and that the attacks **transfer to production engines like Perplexity**. Two findings matter for legitimate practitioners:

1. **Source order, product name, and document content all shift which sources an engine favors** — confirming, from the attacker's side, that on-page signals causally change AI visibility.
2. **The same mechanism that GEO uses for good can be abused.** This is why **[08 · Future & Ethics](08-future-ethics.md)** treats prompt/answer manipulation as a real risk, not a growth hack — and why engines are actively hardening against injected content.

### Why some sources dominate: the training-corpus papers

**Tier 4 — Documented.** GEO doesn't only happen at retrieval time; part of "authority" is baked in when a model is *trained*. Three primary sources explain why Wikipedia and Reddit punch above their weight (the full argument lives in **[05 · Authority & Trust](05-authority.md)**):

- **GPT-3 up-weighted Wikipedia.** Brown et al. (2020) sampled Wikipedia **3.4 epochs** vs. **0.44** for Common Crawl — high-quality text was deliberately over-represented ([arXiv:2005.14165, Table 2.2](https://arxiv.org/abs/2005.14165)).
- **GPT-2's training set was a Reddit quality filter.** Radford et al. (2019) built WebText from pages **linked on Reddit with ≥3 karma**, using human curation as a proxy for quality ([OpenAI PDF](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)).
- **A few big domains dominate common corpora.** Dodge et al. (2021), documenting the C4 corpus, found a small set of large sites (patents, Wikipedia, news) make up a disproportionate share ([EMNLP 2021](https://aclanthology.org/2021.emnlp-main.98/) · [arXiv:2104.08758](https://arxiv.org/abs/2104.08758)).

### An honest note on the state of the literature

> The academic GEO canon in 2026 is roughly: **one founding optimization paper, one adversarial-manipulation paper, and a supporting cast of training-corpus and retrieval papers.** Everything else claiming to be "GEO research" — the studies in Part 3 — is **industry work**: valuable for scale, weaker for method, and usually run by a company selling a related product. Weight accordingly. If you know of a peer-reviewed GEO study not listed here, it is exactly the kind of contribution this chapter needs ([CONTRIBUTING.md](../CONTRIBUTING.md)).

---

## Part 3 — Industry studies with data

These are the large-sample observational studies practitioners cite daily. They are **bigger than any academic study** (millions of citations, tens of thousands of brands) but almost all are **Tier 2 — Observed at scale (correlational)** or **Tier 3 — Behavioral**, and most are run by vendors. Read the method, not the headline.

### What AI engines actually cite

**Profound — AI Platform Citation Patterns.** **Tier 2.** Analyzed **~680 million citations** (Aug 2024 – Jun 2025) across ChatGPT, Google AI Overviews, and Perplexity (not Copilot). The takeaway: **each engine has a different favorite source**, so there is no single "get cited" playbook.

| Engine | Most-cited domain | Share of all its citations | Share of its top-10 sources |
|---|---|---|---|
| **ChatGPT** | **Wikipedia** | 7.8% | 47.9% |
| **Perplexity** | **Reddit** | 6.6% | 46.7% |
| **Google AI Overviews** | Reddit / YouTube / Quora (mixed) | 2.2% / 1.9% / 1.5% | 21.0% / 18.8% / 14.3% |

Across all platforms, **`.com` = 80.4%** and **`.org` = 11.3%** of cited domains. ([Profound, 2025](https://www.tryprofound.com/blog/ai-platform-citation-patterns)) `⚠️` Different vendors report different exact shares for the same engines — treat the *ranking* of domains as robust and the *precise percentages* as method-dependent. Per-engine detail: **[02 · The Engines](02-engines.md)**.

### What correlates with AI visibility

**Ahrefs — Top Brand Visibility Factors (75,000 brands, Dec 2025).** **Tier 2.** Correlated dozens of SEO/brand metrics against whether a brand appears in ChatGPT, Google AI Mode, and AI Overviews (Spearman correlation; filtered to Domain Rating > 40 and keywords ≥ 800 monthly searches). The result reshaped a lot of GEO thinking:

| Factor | Correlation with AI visibility | Strength |
|---|---|---|
| **YouTube brand mentions** | **~0.74** (0.735–0.740) | Strongest |
| YouTube mention impressions | ~0.72 | Very strong |
| **Branded web mentions** | **0.66–0.71** | Strong |
| Branded anchors | 0.51–0.63 | Moderate |
| Branded search volume | 0.35–0.47 | Moderate |
| **Domain Rating** | **0.27–0.33** | Weak |
| Number of site pages | ~0.19 | Weak |
| **Number of backlinks** | **0.19–0.24** | Weak |

> **The finding in one line:** **off-site brand *mentions* out-correlate on-site *backlinks* with AI visibility — by roughly 3×.** This flips the classic SEO priority order. **But the authors state the caveat plainly:** *"correlation isn't causation… that doesn't mean improving these metrics will automatically boost your AI visibility."* Read the mechanism in **[05 · Authority & Trust](05-authority.md)** before acting; measure it on your own brand via **[06 · Measurement](06-measurement.md)**. ([Ahrefs, Dec 2025](https://ahrefs.com/blog/ai-brand-visibility-correlations/))

### What content *types* get cited

**Ahrefs — Do "Best" Lists Boost ChatGPT Visibility? (750 prompts).** **Tier 2 / small-n.** Categorized what ChatGPT cites for **750 top-of-funnel prompts** (software, products, agency recommendations):

- **"Best X" blog listicles were 43.8% of all cited page types** — the single most-cited format for commercial queries.
- **35% of cited lists came from low-authority domains (DR < 20)** — you don't need a huge site to be in the mix.
- **79.1% of cited lists were updated in 2025** — freshness correlates with citation (see the recency study below).
- **Self-promotion can backfire:** publishing your own "best" list that ranks you #1 doesn't guarantee the engine recommends *you*. In one documented example, a brand's self-ranking list *"may have inadvertently helped [a competitor] place higher."* ([Ahrefs, Dec 2025](https://ahrefs.com/blog/best-lists-research/); myth-study detail in [SEJ, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/))

**Seer Interactive — AI Brand Visibility & Content Recency (5,000+ URLs, Jun 2025).** **Tier 2.** Found that content cited by ChatGPT, Perplexity, and AI Overviews skews **recent**, and that AI bots re-crawl fresh pages fast — corroborating the freshness signal above. ([Seer Interactive, 2025](https://www.seerinteractive.com/insights/study-ai-brand-visibility-and-content-recency))

### Research that debunks popular tactics

Some of the most useful industry research is the myth-busting kind. Ahrefs' **"9 AI Search Myths, Debunked"** compiled controlled-ish tests across **~15 million data points** ([SEJ, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/)). **Tier 2** (large-scale, single vendor):

| Popular belief | What the data showed | Sample |
|---|---|---|
| "Schema markup gets you cited" | **No meaningful effect.** After 30 days: ChatGPT +2.2%, AI Mode +2.4%, AI Overviews **−4.6%** | 1,885 test pages vs. 4,000 controls |
| "`llms.txt` boosts AI visibility" | **97% of `llms.txt` files were never read**; only 3% of sites that published one got any request, and 77% of those came from SEO tools, not AI crawlers | 137,000 sites |
| "AI citations are unrelated to Google ranking" | **~38% of AI-Overview-cited URLs also ranked in the organic top 10**; **88.5% of ChatGPT citations came from the general search index** | 1.4M ChatGPT prompts; 863k SERPs; 4M citations |
| "Backlinks/DR drive AI visibility" | Weak correlates (DR 0.27–0.33; backlinks 0.19–0.24), far below brand mentions | 75,000 brands |

> **Why these are gold:** they kill three tactics people spend real time on (schema-as-a-shortcut, `llms.txt`-as-a-boost, backlink-chasing for AI) and confirm one uncomfortable truth — **classic ranking still feeds a large share of AI citations**, so SEO and GEO overlap more than the "SEO is dead" crowd admits. Technical detail and the nuance on schema (still useful for *understanding*, just not a citation lever) live in **[04 · Technical GEO](04-technical.md)**.

### How people actually behave (the "why it matters" evidence)

**Tier 3 — Behavioral.** The clearest, least-conflicted numbers in the whole field come from behavioral panels, not vendors:

- **Pew Research (2025)** watched **68,879 real Google searches** from **900 U.S. adults** in March 2025. When an **AI summary** appeared, users clicked a traditional result in just **8%** of visits — **vs. 15%** without a summary (nearly half as often). They clicked a link *inside* the AI summary only **1%** of the time, and were more likely to **end the session entirely** (**26%** with a summary vs. **16%** without). About **18%** of searches showed an AI summary at all. ([Pew Research, 2025](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/))
- **SparkToro / Similarweb (2026):** as of 2026, **less than one-third of Google searches still send a click** to the open web (~68% "zero-click"). ([SparkToro, 2026](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/))
- **Similarweb (2025):** AI prompts are **~17× longer** than Google searches — conversational, multi-part questions, not keywords — which changes what "matching" content looks like. ([Similarweb, 2025](https://officechai.com/ai/chatgpt-queries-17x-longer-than-google-searches-6x-longer-than-googles-ai-mode-similarweb-data/))

> These three together *are* the business case for GEO: the click is disappearing, the answer is the destination, and if you're not *in* the answer, the 1% summary-link click-rate is all that's left. This is the empirical basis for the framing in **[01 · Foundations](01-foundations.md)**.

---

## Part 4 — Before/after examples & case studies

Everyone wants a "we did X and citations went up Y%" case study. The honest state of the evidence: **rigorous, independently-verified before/after brand case studies are rare**, because almost nobody runs a control. Here is what actually exists, strongest first.

### The gold-standard before/after: the founding paper's own experiment

The most trustworthy before/after in GEO is still the **controlled** one from Part 1: same source, same query, measured **before** and **after** a single intervention, averaged over thousands of queries and five random seeds. Its qualitative examples (paper, Table 4) show the mechanism plainly — *adding the source of a claim, or a relevant statistic, with no new substantive information, measurably raised the passage's share of the generated answer.* When you need to *prove* a GEO tactic works, cite this, not a testimonial. **Tier 1.**

### The population-level "case study": what changed when AI answers arrived

The clearest real-world before/after isn't one brand — it's the **whole search population**. The Pew and SparkToro numbers above are a natural experiment: *before* AI summaries, ~15% of searches produced a click and zero-click sat lower; *after*, click-through roughly halves on summary pages and zero-click passes ~68%. That's the shift GEO exists to answer. **Tier 3.**

### A documented mini-case: self-promotion backfiring

A concrete, cited before/after at the tactic level: brands that published **their own "best tools" lists ranking themselves #1** did **not** reliably get recommended by ChatGPT — and in at least one traced instance the self-serving list *helped a competitor* place higher, because the engine extracted the *comparison*, not the self-ranking ([Ahrefs, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/)). **Tier 2.** The lesson matches the founding paper: engines reward *verifiable, balanced substance*, and they're unimpressed by self-assertion — the same reason "Authoritative" tone didn't win in the lab.

### Why to distrust the typical agency case study

Most GEO case studies you'll find are **Tier 5 — Anecdotal**, and share the same defects:

- **No control.** Visibility rose, but so did the brand's PR, its publishing cadence, and the engines themselves — you can't attribute the lift to the tactic.
- **Cherry-picked queries.** "We now appear for [query]" — but for how many of the queries that matter, and did others drop?
- **Undefined metric.** "Citations up 300%" from a base of 2 to 8, or measured by a tool with its own sampling quirks.
- **Vendor incentive.** The case study sells the service that produced it.

None of that makes them worthless — they're **hypotheses worth testing** — but they are not proof, and this handbook will not repeat their numbers as fact.

### What a credible case study must include

If you want to contribute one here (please do), it has to clear this bar — the same one in [CONTRIBUTING.md](../CONTRIBUTING.md):

```markdown
### <Title> (<Author/Org>, <Year>)
- **Goal:** the specific visibility outcome you targeted (which engine, which queries)
- **Intervention:** exactly what you changed, and what you held constant
- **Measurement:** the metric + tool, defined; ideally a control or a clear baseline window
- **Before / After:** the numbers, with dates and sample sizes
- **Confounders:** what else changed in the same period (be honest)
- **Evidence strength:** demonstrated / observed / anecdotal
- **Link:** where a reader can verify
```

> A single well-controlled case study — with a real baseline and honest confounders — is worth more than fifty "we 5×'d it" posts. If you run one, the field genuinely needs it.

---

## What we still don't know (open research questions)

Being honest about gaps is part of being a reference. As of 2026, these are unsettled — good targets for the next paper or a rigorous case study:

- **Does the founding paper's ranking still hold on 2026 engines?** The "cite/quote/stat" trio was demonstrated on GPT-3.5. A faithful replication on current ChatGPT Search, Gemini, and Perplexity is missing. `⚠️`
- **How much does off-site *mention* volume *cause* (not just correlate with) citations?** The Ahrefs correlation is strong; no controlled test isolates mentions as the variable. `⚠️`
- **What is the real half-life of a citation?** Freshness correlates with citation, but nobody has cleanly measured how fast a cited page decays out of answers.
- **How do multi-turn / agentic queries change GEO?** Almost all evidence is single-turn; agent workflows that chain many retrievals are unstudied. `⚠️`
- **Training-time vs. retrieval-time attribution.** We can't yet separate "cited because the model *knows* you" from "cited because you were *retrieved* now" — which would tell creators where to spend. `⚠️`

---

## Where to go next

- **[03 · Content Strategy](03-content.md)** — turns Part 1's winning methods (cite, quote, add statistics, write clearly) into an actual writing method.
- **[05 · Authority & Trust](05-authority.md)** — the mechanism behind Part 3's brand-mention correlation, and the training-corpus papers in depth.
- **[06 · Measurement](06-measurement.md)** — how to run your *own* before/after so you can test any Tier-5 claim instead of trusting it.
- **[02 · The Engines](02-engines.md)** — the per-engine citation differences (ChatGPT↔Wikipedia, Perplexity↔Reddit) that Profound's data quantifies.
- **[08 · Future & Ethics](08-future-ethics.md)** — the adversarial-manipulation research from Part 2, and where the line sits between optimization and abuse.

---

## Sources

Ordered by evidence tier: **Demonstrated / peer-reviewed** first, then **Documented** primary sources, then **large-scale observational** (industry) and **behavioral** studies. Single-vendor or non-reproducible figures are flagged `⚠️` in-text. All links verified as of 2026-08.

**Tier 1 — Demonstrated / peer-reviewed**

- **Aggarwal, P., Murahari, V., Rajpurohit, T., Kalyan, A., Narasimhan, K., & Deshpande, A. (2024). *GEO: Generative Engine Optimization.* KDD 2024.** — the founding controlled study: GEO-bench (10k queries, 9 sources, 25 domains), the two impression metrics, the nine methods, the +40% headline, the rank-5 +115% democratization result, domain-specific effects, and the Perplexity.ai replication. [arXiv:2311.09735](https://arxiv.org/abs/2311.09735) · [PDF](https://arxiv.org/pdf/2311.09735) · [DOI:10.1145/3637528.3671900](https://doi.org/10.1145/3637528.3671900) · [project page + data](https://generative-engines.com/GEO/) · [code](https://github.com/GEO-optim/GEO)
- **Pfrommer, S., Bai, Y., Gautam, T., & Sojoudi, S. (2024). *Ranking Manipulation for Conversational Search Engines.* EMNLP 2024.** — demonstrates that injected/adversarial content can promote low-ranked sources in conversational search engines (incl. transfer to Perplexity); the adversarial mirror of GEO. [arXiv:2406.03589](https://arxiv.org/abs/2406.03589)

**Tier 4 — Documented (primary sources on why some domains dominate)**

- **Brown, T. B., et al. (2020). *Language Models are Few-Shot Learners* (GPT-3).** — Wikipedia sampled 3.4 epochs vs. Common Crawl 0.44 (Table 2.2). [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- **Radford, A., et al. (2019). *Language Models are Unsupervised Multitask Learners* (GPT-2).** — WebText = Reddit-linked pages with ≥3 karma. [OpenAI PDF](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- **Dodge, J., et al. (2021). *Documenting the English Colossal Clean Crawled Corpus (C4).* EMNLP 2021.** — a small set of large domains dominates a common training corpus. [ACL Anthology](https://aclanthology.org/2021.emnlp-main.98/) · [arXiv:2104.08758](https://arxiv.org/abs/2104.08758)

**Tier 2 — Observed at scale (large-N, correlational; mostly industry — treat as reported)**

- **Profound (2025). *AI Platform Citation Patterns* (~680M citations, Aug 2024–Jun 2025).** — per-engine most-cited domains: ChatGPT↔Wikipedia (7.8%), Perplexity↔Reddit (6.6%), AI Overviews mixed. [tryprofound.com](https://www.tryprofound.com/blog/ai-platform-citation-patterns)
- **Ahrefs (Dec 12, 2025). *Top Brand Visibility Factors in ChatGPT, AI Mode, and AI Overviews* (75,000 brands).** — off-site mentions (~0.66–0.74) out-correlate backlinks/DR (~0.19–0.33); explicit correlation-≠-causation caveat. [ahrefs.com/blog/ai-brand-visibility-correlations](https://ahrefs.com/blog/ai-brand-visibility-correlations/)
- **Ahrefs (Dec 2025). *Do Self-Promotional "Best" Lists Boost ChatGPT Visibility?* (750 prompts).** — "best X" listicles = 43.8% of cited page types; freshness signal; self-promotion backfire. [ahrefs.com/blog/best-lists-research](https://ahrefs.com/blog/best-lists-research/)
- **Search Engine Journal / Ahrefs (2026). *9 AI Search Myths, Debunked* (~15M data points).** — schema-markup null result (1,885 vs 4,000 pages), `llms.txt` 97%-unread (137k sites), ranking↔citation overlap (~38% / 88.5%), backlink/DR correlations. [searchenginejournal.com](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/)
- **Seer Interactive (Jun 25, 2025). *AI Brand Visibility and Content Recency* (5,000+ URLs).** — cited content skews recent; AI bots re-crawl fresh pages fast. [seerinteractive.com](https://www.seerinteractive.com/insights/study-ai-brand-visibility-and-content-recency)

**Tier 3 — Behavioral (measured human behavior)**

- **Pew Research Center (2025). *Google users are less likely to click on links when an AI summary appears.*** — 68,879 searches / 900 U.S. adults, March 2025; 8% vs 15% click-through, 1% summary-link clicks, 26% vs 16% session-end. [pewresearch.org](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)
- **SparkToro / Similarweb (2026). *In 2026, Less than One Third of Google Searches Still Send a Click.*** — the zero-click landscape (~68%). [sparktoro.com](https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/)
- **Similarweb (2025). *2025 Generative AI Landscape.*** — AI prompts ~17× longer than Google searches. [similarweb.com](https://officechai.com/ai/chatgpt-queries-17x-longer-than-google-searches-6x-longer-than-googles-ai-mode-similarweb-data/)

> **Found an error, a dead link, or — especially — a peer-reviewed GEO study or a properly-controlled case study we're missing?** This is the chapter where sourcing matters most. See [CONTRIBUTING.md](../CONTRIBUTING.md): every claim carries a real source and an evidence tier, or an honest `⚠️ needs verification` flag. If you add a statistic, bring its **sample size, method, and exact metric definition** — half the disagreements in this field are two studies measuring different things and calling them the same word.
