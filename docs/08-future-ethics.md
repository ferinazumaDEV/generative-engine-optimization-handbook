# 08 · Future, Risks & Ethics

> Part of **[The GEO Handbook](../README.md)** — a free, community-maintained reference on Generative Engine Optimization. New to the project? Start at the [README](../README.md). Terms are defined once in the [Glossary](09-glossary.md); the evidence behind claims here lives in [07 · Research & Case Studies](07-research-cases.md).
>
> *Last substantive review: 2026-08. This chapter is deliberately split into three registers: **what is documented** (dated facts with primary sources), **what is demonstrated** (peer-reviewed risk research), and **what is speculation** (labeled `🔮 speculation` — reasoned forecasting, not fact). GEO's frontier moves weekly; treat every dated figure as "true as observed then" and re-check the linked source before acting. Anything unverified is flagged `⚠️`.*

Every other chapter of this handbook tells you how to *win* at GEO. This one is about the parts that don't fit on a tactics checklist: where the whole game is heading, the ways it can hurt you or others, and the line between **optimizing** so an engine understands you and **manipulating** so it lies for you.

That line matters more here than in classic SEO for one structural reason:

> **In GEO, the "ranking function" is a language model — a system that can be *argued with*, *deceived*, and *hijacked* through the very text it reads.** A Google crawler parses your page. A generative engine *reads* it, and can be talked into things. That single fact is the source of most of this chapter's risks and all of its ethics.

---

## TL;DR

- **The trajectory is links → answers → agents.** Search is moving from a list of pages, to a synthesized answer, to an autonomous **agent** that reads, reasons, and acts on your behalf ([Google AI Mode, launched 5 Mar 2025](https://blog.google/products/search/ai-mode-search/)). GEO's target is shifting from "be a cited source" toward "be the source an *agent* trusts enough to act on."
- **The economic bargain that funded the open web is breaking.** AI answers reduce clicks: in a Pew panel of ~69k real searches, users clicked a result **8% of the time when an AI summary appeared vs. 15% without**, and clicked a source *inside* the summary just **1%** of the time ([Pew Research, 2025](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)). Crawlers now take vastly more than they send back.
- **A counter-economy is forming around licensing and access control.** Cloudflare began **blocking AI crawlers by default and launched "pay per crawl"** ([1 Jul 2025](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)); publishers and platforms backed the **RSL (Really Simple Licensing)** standard for machine-readable content terms ([rslstandard.org, 2025](https://rslstandard.org/)). Whether these hold is unresolved.
- **Getting cited is not the same as getting cited *correctly*.** Independent testing found AI search engines answered **>60% of source-attribution queries wrong**, often citing fabricated or broken URLs and syndicated copies over originals ([CJR Tow Center, Mar 2025](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php)). You can be misquoted *by* the answer, and getting the correction is hard.
- **Adversarial "black-hat GEO" is real and peer-reviewed, not hypothetical.** Researchers have shown a **"strategic text sequence" hidden on a product page can force it to the top of an LLM's recommendations** ([Kumar & Lakkaraju, 2024](https://arxiv.org/abs/2404.07981)), and that conversational engines like Perplexity can be **reliably manipulated by injected page content** ([Pfrommer et al., EMNLP 2024](https://arxiv.org/abs/2406.03589)). This handbook documents these to help you *recognize and defend*, not deploy.
- **Prompt injection is the defining new attack surface.** Because engines read your content as partial *instructions*, hostile text on a page — yours or a competitor's — can hijack an answer or an agent. Indirect prompt injection is a demonstrated, unsolved class of attack ([Greshake et al., 2023](https://arxiv.org/abs/2302.12173)) and sits at **#1 (LLM01)** on the [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/).
- **Mass-generated content threatens the corpus itself.** Training models on model-generated text degrades them — **"model collapse"** ([Shumailov et al., *Nature*, 2024](https://doi.org/10.1038/s41586-024-07566-y)). AI slop is not just an aesthetic problem; it poisons the well every engine drinks from.
- **The ethical line is old, the stakes are new.** Disclosure of AI-generated content and commercial intent is increasingly a *legal* requirement, not just etiquette — see the [FTC fake-reviews rule (2024)](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials) and [EU AI Act Article 50](https://artificialintelligenceact.eu/article/50/). Provenance standards like [C2PA Content Credentials](https://c2pa.org/) aim to make "is this real?" machine-checkable.

---

## Part 1 — Where GEO is heading

Three shifts define the near future. None is finished; all are underway.

### Shift 1: From answers to agents

The first wave of generative search *answered* your question in prose with a few citations. The second wave *acts*:

- **Agentic / "deep research" modes** decompose a question into many sub-queries, fetch and read dozens of pages, and synthesize a multi-step report — rather than answering from a single retrieval. Google's **AI Mode** (launched [5 Mar 2025](https://blog.google/products/search/ai-mode-search/)) uses a **"query fan-out"** technique that "searches multiple data sources concurrently, then synthesizes results." Comparable "research assistant" modes shipped across the major engines through 2025.
- **AI browsers and agents** go further — reading pages, filling forms, comparing products, and completing tasks with minimal human clicks. `⚠️ The specific products, names, and capabilities in this space change monthly; verify the current state per engine in [02 · The Engines](02-engines.md) rather than trusting any single snapshot here.`

**What this changes for GEO:** the "reader" you are optimizing for is less and less a human skimming an answer, and more an automated pipeline that fans a question into many retrievals, weighs sources, and may *act* on what it reads. Three consequences:

| Era | The unit of visibility | What you optimize for |
|---|---|---|
| **Search (classic SEO)** | A ranked link | A human clicks your page |
| **Answers (GEO, 2024–2025)** | A citation inside a synthesized paragraph | A model *quotes* your page |
| **Agents (emerging)** | Being the source an agent *trusts and acts on* | A model *relies* on your page across a multi-step task |

> 🔮 **speculation.** As more queries are answered by fan-out and agents, **prompt coverage** (the breadth of natural-language questions you're retrievable for) and **machine-parseable factual clarity** likely matter more than any single ranked page. This is a reasoned extrapolation from where the products are going, *not* a measured result — treat it as a hypothesis to test with [06 · Measurement](06-measurement.md), not a fact.

### Shift 2: The broken bargain — economics of the answer

Classic search ran on a trade: **you let Google crawl you, Google sent you clicks.** Generative answers keep the first half and gut the second.

**The measured demand-side shift** (how users behave):

- With an AI summary present, the click-through to any traditional result roughly **halved (15% → 8%)**, clicks to sources *inside* the summary were ~**1%**, and users were more likely to **end the session entirely** (26% vs. 16%) — [Pew Research, Jul 2025](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/), a clickstream panel of 68,879 real searches. This is behavioral evidence (Tier 3 in [07's evidence ladder](07-research-cases.md#how-to-read-the-evidence-in-this-handbook)) — it describes *users*, not causation, but it's directly measured.

**The measured supply-side shift** (how crawlers behave):

- Cloudflare reports the crawl-to-referral ratio has become wildly lopsided — by its analysis, earning a referred visit is **~750× harder via OpenAI and ~30,000× harder via Anthropic** than via classic Google crawling, because AI crawlers fetch enormously more per visitor they return ([Cloudflare, 1 Jul 2025](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)). `⚠️ single-vendor figure with an obvious incentive — Cloudflare sells the blocking product. The direction is corroborated by Cloudflare's separate crawl-to-refer data cited in [06 · Measurement](06-measurement.md); the exact multiples are theirs.`

**The consequence — "the answer without a click":** if the engine satisfies the user *and* keeps the click, the content that fed the answer earns neither traffic nor ad revenue. This is the central economic tension of the whole field, and it drives Shift 3.

> **The GEO reframing.** In a zero-click world, a "visit" is a weaker success metric and **being the cited authority** (brand imprint, being *named* even without a click) becomes a goal in itself. This is real, but don't let it become a cope: measure the [business outcomes you actually have](06-measurement.md#layer-2--the-traffic-layer-ai-referrals-in-analytics), not just vanity presence.

### Shift 3: The counter-movement — licensing, access control, and provenance

Publishers and infrastructure providers are building the tollbooth the open web never had. Watch these; several may become GEO controls you configure directly.

| Development | What it is | Status (2026-08) | Why it matters for GEO |
|---|---|---|---|
| **Pay-per-crawl** ([Cloudflare](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)) | Block AI crawlers by default; let sites charge per fetch via a marketplace | Announced 1 Jul 2025; marketplace in beta | Access to your content may become a *priced* decision, not a default |
| **RSL — Really Simple Licensing** ([rslstandard.org](https://rslstandard.org/)) | Machine-readable licensing terms (attribution + compensation) attached to content, extending `robots.txt` | RSL 1.0 published 2025; backers incl. Reddit, Yahoo, Ziff Davis, O'Reilly, Vox Media, People Inc., Creative Commons, Cloudflare, Fastly, Akamai | A standard way to say "you may train/answer on this *if…*" — the license layer for the AI web |
| **AI-specific `robots.txt` controls** | Per-bot allow/deny for training vs. search vs. user-fetch crawlers | Live and evolving | The lever you *already* control — see [04 · Technical GEO](04-technical.md#ai-crawlers-the-bots-you-need-to-know). Blocking the wrong bot silently removes you from citations |
| **`llms.txt`** ([llmstxt.org](https://llmstxt.org/)) | A community-proposed markdown file offering clean, agent-friendly content | Proposal by Jeremy Howard, Sep 2024 (v2, Aug 2026); **not an official standard**; adoption growing | Aspires to be the "sitemap for LLMs" — but see the reality check below |
| **C2PA / Content Credentials** ([c2pa.org](https://c2pa.org/)) | Open provenance standard — a cryptographic "nutrition label" of origin and edits | Spec v2.x; steering committee incl. Adobe, Google, Meta, Microsoft, OpenAI, BBC, Sony, TikTok | Makes "who made this / is it AI-generated" machine-checkable — future authenticity signal |
| **Content-licensing deals** | Direct publisher↔AI-lab contracts (e.g. the Reddit deals in [05 · Authority](05-authority.md#sources)) | Ongoing, expanding | Licensed corpora get privileged treatment; being *in* one is an authority signal money can buy |

> ⚠️ **Reality check on `llms.txt`.** It is a *proposal*, not a ratified standard, and there is evidence engines mostly **don't read it yet** — an Ahrefs study found ~97% of `llms.txt` files were never fetched by AI crawlers across ~137,000 sites ([SEJ/Ahrefs, 2026](https://www.searchenginejournal.com/ai-search-myths-debunked-ahrefs-spa/584393/), summarized in [07 · Research](07-research-cases.md)). Publish one if it's cheap; do **not** treat it as a citation lever until behavior data says otherwise. This is exactly the kind of hopeful-but-unproven tactic this handbook exists to flag.

---

## Part 2 — The risks

Optimizing for a system that *reads* introduces failure modes that classic SEO never had. Here they are, worst-first, each with its evidence tier.

| Risk | One-line definition | Evidence | Who bears the cost |
|---|---|---|---|
| **Misattribution / hallucinated citation** | The engine cites you for something you didn't say, or invents a source | Demonstrated ([CJR, 2025](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php)) | You (reputation), the reader (false info) |
| **Adversarial manipulation ("black-hat GEO")** | Hidden text forces the engine to rank/recommend a product | Demonstrated ([Kumar & Lakkaraju, 2024](https://arxiv.org/abs/2404.07981); [Pfrommer et al., 2024](https://arxiv.org/abs/2406.03589)) | Honest competitors, the reader, the engine's trust |
| **Prompt injection of content** | Text on a page acts as *instructions* that hijack the answer or an agent | Demonstrated ([Greshake et al., 2023](https://arxiv.org/abs/2302.12173); [OWASP LLM01](https://genai.owasp.org/llm-top-10/)) | You (hijacked reputation), agent users (harm) |
| **Content pollution / model collapse** | Mass AI-generated "slop" degrades the corpus engines learn from | Demonstrated ([Shumailov et al., *Nature*, 2024](https://doi.org/10.1038/s41586-024-07566-y)) | Everyone — the shared information commons |
| **Getting cited for wrong info** | An outdated or error-containing page of yours becomes "the answer" | Documented (via the hallucination + freshness evidence) | You, the reader |
| **Silent removal** | Blocking the wrong crawler, or a paywall/licensing choice, cuts you from citations without warning | Documented ([04 · Technical](04-technical.md)) | You (invisible loss) |

### Risk 1: Hallucination — cited, but wrong

The headline promise of GEO — *be the source in the answer* — has a dark twin: **be the source in a *wrong* answer, or be cited for words you never wrote.**

- **Engines fabricate and misattribute citations at high rates.** The Columbia Journalism Review's Tow Center tested eight AI search engines and found they collectively answered **more than 60% of source-attribution queries incorrectly**, frequently with total confidence. Grok 3 was wrong ~94% of the time; several engines returned **fabricated or broken URLs** (Grok 3: 154 of 200 citations broken), and many cited **syndicated copies (Yahoo/AOL) instead of the original publisher** ([CJR, Mar 2025](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php)). A citation appearing next to your name is **not** proof the engine represented you correctly.
- **The engine can amplify bad sources at scale.** Google's **AI Overviews** infamously told users to **put glue on pizza** (traced to an 11-year-old Reddit joke) and to **eat rocks** (from a satirical *Onion* article) in May 2024. Google called them "extremely rare queries" and refined the system ([Search Engine Land, 24 May 2024](https://searchengineland.com/google-ai-overviews-odd-answers-442575)). The lesson for creators cuts both ways: **satire, jokes, and errors in your content can be laundered into confident fact by an engine that can't reliably tell them apart.**

**Defensive GEO** (the honest response to this risk):

- Write so you're **hard to misquote**: put the correct, self-contained claim *inside one chunk* with its qualifier, so an extractive engine can't lift a half-truth ([03 · Content](03-content.md)).
- **Monitor how you're represented**, not just whether you appear — track sentiment and factual accuracy of mentions, and watch for stale pages resurfacing ([06 · Measurement](06-measurement.md#the-kpis--definitions)).
- **Keep authoritative pages current and unambiguous.** An outdated price, policy, or stat on your own site is the most likely thing to get cited wrong *about you*.

### Risk 2: Manipulation — the "black-hat GEO" that already works in the lab

This is the risk the rest of this handbook is the antidote to. Because the ranking function is a language model, you can try to *talk it into* citing you — and researchers have shown it works.

- **Strategic text sequences (STS).** Kumar & Lakkaraju showed that **adding a carefully crafted, often human-unreadable text sequence to a product's page can significantly raise its odds of being the LLM's top recommendation** — moving a product that was "rarely recommended" or ranked second into first place ([*Manipulating Large Language Models to Increase Product Visibility*, 2024](https://arxiv.org/abs/2404.07981)). They explicitly compare it to how SEO "transformed webpage ranking" — i.e., this is the adversarial-SEO playbook, ported to LLMs.
- **Ranking manipulation that transfers to real engines.** Pfrommer et al. built a **tree-of-attacks jailbreak that "reliably promotes low-ranked products,"** and showed the exploits **"transfer effectively to state-of-the-art conversational search engines such as perplexity.ai"** ([*Ranking Manipulation for Conversational Search Engines*, EMNLP 2024](https://arxiv.org/abs/2406.03589)). This is not a toy: it moves real products in a shipping product.

> **The handbook's line, stated plainly.** We document these attacks so **defenders and honest operators can recognize them** — a competitor gaming an answer against you, an audit of your own vendors, an engine's blind spot you should report. **They are not techniques this handbook recommends.** Beyond the ethics (below), they are *fragile*: engines patch jailbreaks, hidden-text tricks recreate the exact spam pattern search engines spent two decades learning to punish (see the [anti-patterns in 05 · Authority](05-authority.md#anti-patterns-off-page-manipulation-to-avoid)), and a manipulated citation collapses the moment a human checks it. The durable version of "get recommended" is [being genuinely worth recommending](03-content.md).

**Why it's also a *you* problem, not just a temptation:** the same mechanism means a **competitor can inject text to suppress or smear you**, and an attacker can plant content designed to make engines say false things about your brand. Manipulation is a threat model to defend against, regardless of your own ethics.

### Risk 3: Prompt injection — your content as a weapon (or a target)

This is the risk with no clean classic-SEO analogue, and the one most likely to define the agent era.

> **Bullet definition — Indirect prompt injection:** an attack where hostile instructions are hidden **inside content the model retrieves** (a web page, a document, a review), rather than typed by the user. When the engine reads the page, it may follow those instructions — leaking data, changing its answer, or taking an action — because LLMs "**blur the line between data and instructions**" ([Greshake et al., 2023](https://arxiv.org/abs/2302.12173)).

- It is the **#1 risk (LLM01)** on the [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/), the industry's consensus threat list — ahead of data leakage and every other LLM vulnerability.
- Documented impacts include **data theft, answer manipulation, and "worming"** across LLM-integrated apps, demonstrated against real systems including search-integrated GPT-4 ([Greshake et al., 2023](https://arxiv.org/abs/2302.12173)).

**The two faces of prompt injection in GEO:**

1. **Your content could be the vector.** If your pages carry user-generated content (reviews, comments, forum posts) or third-party embeds, an attacker can plant injection text there. An agent that reads your page on a user's behalf could be hijacked *through you* — a liability and a trust problem you own. **Sanitize UGC; don't render untrusted text as if it were yours.**
2. **You could be the target.** A competitor or bad actor can inject content elsewhere designed to make engines misrepresent *you* — the manipulation risk above, weaponized against your brand.

**What honest operators do:** treat prompt injection as a **security problem, not a growth tactic.** Do not embed hidden instructions in your own pages "to help the AI" — it's indistinguishable from an attack, it will be filtered or penalized, and it teaches your infrastructure the wrong pattern. Follow the [OWASP guidance](https://genai.owasp.org/llm-top-10/) on your own properties.

> **Defend it as an engineer.** Prompt injection is covered as a hands-on security problem — the *lethal trifecta*, indirect injection via RAG/tools, and why prompt-level defenses fail while architecture-level ones work — in the companion reference **[Evidence-Based Prompt Engineering → Security](https://github.com/ferinazumaDEV/prompt-engineering-evidence/blob/main/docs/05-security.md)**.

### Risk 4: Content pollution and model collapse — poisoning the well

The cheapest GEO tactic is also the most corrosive to the whole ecosystem: **flood the web with AI-generated pages to blanket every query.** At scale, this backfires on everyone, provably.

- **Model collapse.** Training generative models on model-generated data causes **"irreversible defects… where tails of the original content distribution disappear"** — the model forgets rare, real, human patterns and drifts toward bland self-reference. Demonstrated across model types up to LLMs ([Shumailov et al., *The Curse of Recursion*, 2023](https://arxiv.org/abs/2305.17493); peer-reviewed as **[*AI models collapse when trained on recursively generated data*, *Nature* 631, 2024](https://doi.org/10.1038/s41586-024-07566-y)**). As "AI slop" fills the web, the corpus every future engine learns from degrades.
- **The near-term version for creators:** engines and platforms are actively **demoting mass-produced, low-value content** (the same reflex that produced the [anti-patterns in 05](05-authority.md#anti-patterns-off-page-manipulation-to-avoid)). Spinning a thousand thin pages doesn't build citability; it builds a footprint that detectors and quality systems are increasingly tuned to discount.

> **The commons argument.** Even if slop *worked* for you short-term, it degrades the shared resource — the corpus of trustworthy human content — that makes generative engines (and your own citations) worth anything. GEO done well **adds** a genuinely useful, extractable source to that commons. That is not just ethics; it's the only version of the strategy that compounds instead of collapsing.

---

## Part 3 — The ethics: where the line is

Most of GEO is ordinary, defensible optimization: writing clearly, structuring for extraction, being genuinely authoritative. A minority of tactics cross into manipulation or deception. This section draws the line explicitly, because "the model can be argued with" makes the boundary blurrier here than anywhere in SEO.

### The core test: optimization vs. manipulation

A single question separates the two:

> **Are you making it easier for the engine to understand and trust something *true*, or are you trying to make it say something it otherwise wouldn't — because it isn't warranted?**

| | **Optimization** (do this) | **Manipulation** (don't) |
|---|---|---|
| **Goal** | Be accurately understood and fairly represented | Force a citation/recommendation you haven't earned |
| **Method** | Clarity, structure, real evidence, genuine authority | Hidden text, injected instructions, faked signals |
| **If the reader saw it** | Fine — it's just good content | Embarrassing — it only works while concealed |
| **If it works** | The engine is *more* right about you | The engine is *less* right for everyone |
| **Durability** | Compounds across model generations | Collapses when patched or checked |
| **Examples** | [Citable stats & quotes](03-content.md), [entity clarity](05-authority.md), [crawlability](04-technical.md) | [STS](https://arxiv.org/abs/2404.07981), [ranking jailbreaks](https://arxiv.org/abs/2406.03589), astroturfing, fake reviews |

The founding [GEO paper](07-research-cases.md#part-1--the-founding-study-geo-aggarwal-et-al-kdd-2024) is instructive here: its *winning* tactics — cite sources, add statistics, quote credible authorities — are the honest ones, and **keyword stuffing performed worse than doing nothing.** The evidence and the ethics point the same way.

### Disclosure and transparency — increasingly the law, not just etiquette

Two disclosure questions matter for GEO, and both are now touched by regulation:

**1. Is the content AI-generated / AI-assisted?**

- The **EU AI Act, Article 50** requires providers to **mark AI-generated synthetic content (audio, image, video, *text*) in a machine-readable, detectable format**, and requires deployers to **disclose AI-generated text published to inform the public on matters of public interest** — unless it had human editorial review with a responsible editor ([EU AI Act Art. 50](https://artificialintelligenceact.eu/article/50/)). `⚠️ The AI Act's transparency obligations phase in on a staged timeline through 2026–2027; confirm the exact application date for your case — this is a fast-moving legal area and needs verification against current guidance.`
- Provenance standards like **[C2PA Content Credentials](https://c2pa.org/)** aim to make this *automatic and cryptographic* — a "nutrition label" traveling with the asset. Expect authenticity signals to become part of how engines (and readers) weigh a source.

**2. Is there a commercial relationship / paid intent?**

- The **US FTC's final rule on fake reviews and testimonials** (announced [14 Aug 2024](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials); effective Oct 2024) bans, among other things, **AI-generated fake reviews, reviews misrepresenting real experience, undisclosed insider reviews, and buying fake indicators of influence.** These are exactly the off-page "authority" shortcuts [05 warns against](05-authority.md#anti-patterns-off-page-manipulation-to-avoid) — now explicitly unlawful in the US, with penalties.
- The through-line: **manufacturing the signals engines read (fake reviews, astroturfed mentions, sockpuppet threads) is increasingly both detectable and illegal.** Earn them.

### Platform terms and legality — respect the rules on *both* sides

- **Don't fake, don't scrape-and-abuse.** Just as you shouldn't manipulate engines, note that the engines' *own* scraping is contested: the [Perplexity episode](https://www.forbes.com/sites/randalllane/2024/06/11/why-perplexitys-cynical-theft-represents-everything-that-could-go-wrong-with-ai/) (Forbes accused it of near-verbatim republishing of original reporting with minimal attribution, 11 Jun 2024) and the [CJR finding that engines fetched content from publishers who blocked them](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php) show the norms are unsettled. Your levers are legitimate: `robots.txt`, licensing ([RSL](https://rslstandard.org/)), and access control ([Cloudflare](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)) — use them deliberately (see [04 · Technical](04-technical.md)).
- **Respect each engine's guidelines.** Techniques that violate a platform's terms (cloaking, hidden text, injected instructions) risk removal and are, again, fragile. When a tactic only works *because* it's against the rules, it has a short half-life.

### The handbook's stance

This is a **documentation project, not a growth-hacking service.** Our standing commitments:

- **We describe manipulative tactics to help defenders recognize them — never as recommendations.** Every risky technique in this handbook carries its caveats and its evidence.
- **Every claim carries a real source or an honest `⚠️ needs verification` flag.** A handbook about earning *citations* has to meet a citation standard ([CONTRIBUTING.md](../CONTRIBUTING.md)).
- **Contributions proposing techniques must include a risks/caveats section** (see the [new-technique template](../.github/ISSUE_TEMPLATE/new-technique.md)). "Here's a trick" without "here's how it fails and who it hurts" doesn't get merged.

### Red lines — tactics this handbook will not endorse

- **Hidden or injected instructions** in your content to steer or hijack an engine/agent (STS, prompt injection). Indistinguishable from an attack; a [security risk](#risk-3-prompt-injection--your-content-as-a-weapon-or-a-target), not a tactic.
- **Faked authority signals** — bought/AI-generated reviews, astroturfed communities, sockpuppets, mention farms. [Detectable, often illegal](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials), and self-defeating.
- **Deception about identity or relationship** — undisclosed paid placement, fake expertise, impersonation.
- **Mass low-value content** produced to blanket queries — pollutes the [commons](#risk-4-content-pollution-and-model-collapse--poisoning-the-well) and gets demoted.
- **Manipulating an engine into stating something false** — about you, a competitor, or the world. The whole point of the answer is that people trust it; abusing that is the cardinal sin of the field.

---

## Part 4 — What could change the game

Forecasting, explicitly labeled. These are the wildcards a serious operator watches. `🔮 speculation — reasoned scenarios, not predictions with dates. None of this is a fact yet.`

| Wildcard | If it happens | Signal to watch |
|---|---|---|
| **Ads inside answers** | Sponsored citations blur "earned" vs. "paid" visibility; a new pay-to-appear layer forms atop organic GEO | Engines rolling out ad units / sponsored sources in AI answers |
| **Licensing markets mature** | Being *in* a licensed corpus becomes a buyable authority signal; the open-crawl era narrows | [RSL](https://rslstandard.org/) / [pay-per-crawl](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/) adoption; more publisher↔lab deals |
| **Agent-to-agent commerce** | Your "audience" is increasingly other software; optimization targets machine-readable trust, not human persuasion | Agents completing purchases/bookings; agent-facing content formats |
| **Provenance becomes a ranking signal** | [C2PA](https://c2pa.org/)-signed, verifiably-human or verifiably-sourced content is preferred; unsigned content is discounted | Engines surfacing / weighting Content Credentials |
| **Regulation forces disclosure & attribution** | Mandatory AI-content labeling and source attribution reshape what "citation" means | [EU AI Act](https://artificialintelligenceact.eu/article/50/) enforcement; new national rules |
| **The detection arms race escalates** | Manipulation (STS, injection) and defenses co-evolve; black-hat GEO gets shorter-lived and riskier | Papers + engine patches following [Kumar](https://arxiv.org/abs/2404.07981)/[Pfrommer](https://arxiv.org/abs/2406.03589) |
| **Model collapse mitigation reshapes sourcing** | To avoid [collapse](https://doi.org/10.1038/s41586-024-07566-y), labs prize *verified-human, high-provenance* content — raising the value of genuine expertise | Labs paying for/prioritizing provenance-tagged human data |
| **Personalization fractures "the answer"** | There is no single answer to optimize for; visibility becomes per-user and harder to measure | Divergent answers across users/regions (see [06](06-measurement.md)) |

**The one durable bet across every scenario:** each wildcard *raises* the premium on **genuine, verifiable, well-structured expertise** and *lowers* the payoff of shortcuts. Whether the future rewards provenance signatures, licensed corpora, or agent trust, the content that wins is real and clearly-expressed. That is not a coincidence — it's the same conclusion the [founding evidence](07-research-cases.md) already reached. **Optimize to be understood; don't manipulate to be misunderstood in your favor.**

---

## Where to go next

- **[07 · Research & Case Studies](07-research-cases.md)** — the evidence behind every risk here, rated by strength: the founding study, the manipulation papers, the behavioral data.
- **[05 · Authority & Trust](05-authority.md)** — the honest way to earn the signals that manipulation tries to fake, and the [off-page anti-patterns](05-authority.md#anti-patterns-off-page-manipulation-to-avoid) this chapter treats as red lines.
- **[04 · Technical GEO](04-technical.md)** — the access controls (`robots.txt`, AI user-agents, crawler allow/deny) that are your real levers in the licensing/economics shift.
- **[03 · Content Strategy](03-content.md)** — writing hard-to-misquote, extractable content: the practical defense against the misattribution risk.
- **[06 · Measurement](06-measurement.md)** — how to detect when you're misrepresented, and to test the "future" hypotheses here on your own brand instead of trusting them.

---

## Sources

Primary research and official/legal documents first, then large-sample observational and journalistic investigations, then standards bodies. Single-vendor and incentivized figures are flagged `⚠️` in-text. Speculation is labeled `🔮` in-text and carries no source because it is *not* a claim of fact. All links verified as of 2026-08. **Special caution for this chapter:** the future/ethics space is where confident, unsourced prediction thrives — if you add a forecast, mark it as speculation; if you add a risk, bring the peer-reviewed or primary-documented evidence that it is real.

**Peer-reviewed / primary research (Tier 1 — demonstrated):**

- **Kumar, A., & Lakkaraju, H. (2024). *Manipulating Large Language Models to Increase Product Visibility.*** — a "strategic text sequence" added to a product page significantly raises its chance of being the LLM's top recommendation. [arXiv:2404.07981](https://arxiv.org/abs/2404.07981)
- **Pfrommer, S., Bai, Y., Gautam, T., & Sojoudi, S. (2024). *Ranking Manipulation for Conversational Search Engines.* EMNLP 2024 (Main).** — a tree-of-attacks jailbreak "reliably promotes low-ranked products" and transfers to Perplexity.ai. [arXiv:2406.03589](https://arxiv.org/abs/2406.03589)
- **Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., & Fritz, M. (2023). *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection.*** — defines indirect prompt injection; shows real systems (incl. search-integrated GPT-4) are vulnerable. [arXiv:2302.12173](https://arxiv.org/abs/2302.12173)
- **Shumailov, I., Shumaylov, Z., Zhao, Y., Gal, Y., Papernot, N., & Anderson, R. (2023/2024). *The Curse of Recursion* / *AI models collapse when trained on recursively generated data.*** — model collapse: training on model-generated data causes irreversible degradation. [arXiv:2305.17493](https://arxiv.org/abs/2305.17493) · peer-reviewed in *Nature* 631 (2024), [DOI:10.1038/s41586-024-07566-y](https://doi.org/10.1038/s41586-024-07566-y)
- **Aggarwal, P., et al. (2024). *GEO: Generative Engine Optimization.* KDD 2024.** — the founding study; its *honest* tactics win and keyword-stuffing loses (see [07](07-research-cases.md)). [arXiv:2311.09735](https://arxiv.org/abs/2311.09735) · [DOI:10.1145/3637528.3671900](https://doi.org/10.1145/3637528.3671900)

**Official / legal / standards documents (Tier 4 — documented):**

- **US Federal Trade Commission (2024). *Final Rule Banning Fake Reviews and Testimonials.*** — bans AI-generated fake reviews, misrepresented experience, undisclosed insider reviews, fake influence indicators. Announced 14 Aug 2024. [ftc.gov](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials)
- **EU AI Act, Article 50 — Transparency obligations.** — machine-readable marking of AI-generated synthetic content (incl. text) and disclosure of AI-generated public-interest text. `⚠️ staged application 2026–2027 — verify current date.` [artificialintelligenceact.eu/article/50](https://artificialintelligenceact.eu/article/50/)
- **OWASP GenAI Security Project. *Top 10 for LLM Applications (2025).*** — prompt injection ranked **LLM01**, the #1 LLM risk. [genai.owasp.org/llm-top-10](https://genai.owasp.org/llm-top-10/) `⚠️ canonical project page; confirm current-year ordering.`
- **C2PA / Content Authenticity Initiative. *Content Credentials.*** — open provenance standard; "nutrition label" for digital content; steering committee incl. Adobe, Google, Meta, Microsoft, OpenAI, BBC, Sony, TikTok. [c2pa.org](https://c2pa.org/)
- **RSL Standard (2025). *Really Simple Licensing.*** — machine-readable content-licensing terms for AI; backers incl. Reddit, Yahoo, Ziff Davis, O'Reilly, Vox Media, People Inc., Creative Commons, Cloudflare, Fastly, Akamai. [rslstandard.org](https://rslstandard.org/)
- **Howard, J. (2024). *The `/llms.txt` file* proposal.** — community proposal (not an official standard) for agent-friendly content. [llmstxt.org](https://llmstxt.org/)
- **Google (2025). *AI Mode in Search.*** — launched 5 Mar 2025; "query fan-out" multi-source synthesis; the agentic direction of travel. [blog.google](https://blog.google/products/search/ai-mode-search/)

**Large-sample observational & journalistic investigations (Tiers 2–3):**

- **Cloudflare (2025). *Content Independence Day: no AI crawl without compensation.*** — default-block AI crawlers + "pay per crawl"; the ~750×/~30,000× crawl-to-referral figures (`⚠️ single-vendor, incentivized`). Announced 1 Jul 2025. [blog.cloudflare.com](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)
- **Pew Research Center (2025). *Google users are less likely to click on links when an AI summary appears.*** — 68,879 real searches; click rate 8% (AI summary) vs. 15% (none); 1% clicked a source in the summary. 22 Jul 2025. [pewresearch.org](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)
- **Jaźwińska, K., & Chandrasekar, A. — Columbia Journalism Review / Tow Center (2025). *We Compared Eight AI Search Engines. They're All Bad at Citing News.*** — >60% of source-attribution answers wrong; fabricated/broken URLs; syndicated-over-original citing. 6 Mar 2025. [cjr.org](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php)
- **Search Engine Land (2024). *Google AI Overviews served up some odd (and dangerous) answers.*** — "glue on pizza" (Reddit joke) and "eat rocks" (*The Onion*) in AI Overviews; Google's "rare queries" response. 24 May 2024. [searchengineland.com](https://searchengineland.com/google-ai-overviews-odd-answers-442575)
- **Lane, R. — Forbes (2024). *Why Perplexity's Cynical Theft Represents Everything That Could Go Wrong With AI.*** — accusation of near-verbatim republishing of Forbes' original reporting with minimal attribution. 11 Jun 2024. [forbes.com](https://www.forbes.com/sites/randalllane/2024/06/11/why-perplexitys-cynical-theft-represents-everything-that-could-go-wrong-with-ai/)

> **Found an error, a dead link, or a newer development?** This chapter ages fast — the future/ethics frontier moves weekly. Per [CONTRIBUTING.md](../CONTRIBUTING.md): every claim carries a real source or an honest `⚠️ needs verification` flag, and every forecast is labeled `🔮 speculation`. If you add a risk, bring the peer-reviewed or primary evidence that it's real; if you add a prediction, mark it as one.
