# Protocol — inline citation density in the smaller answer engines

**Why this exists.** Chapter `02 · The Engines` used to say that You.com, Brave and Arc *"tend to
place numbered inline citations on nearly every answer"*, on the authority of a comparison blog.
The vendors' own documentation does not support the sentence (checked 2026-09-04: You.com documents
`sources` in its Research API, not the consumer product; Brave's Leo page says nothing about
citations; Arc's page says nothing about attribution). A product behaviour that no primary source
describes has to be observed, not cited. This protocol is the observation, and the chapter now
says what was observed — with its date and its limits — instead of what the blog said.

## What is measured

One binary variable per engine per query: **does the generated answer show at least one inline
citation marker — a numeral, superscript or chip inside the answer text that leads to a source
URL?** Yes or no. Not how many, not whether they are correct. Noted separately, not scored: whether
sources appear only as a list under the answer (a list at the end does not tie a claim to a source
the way an inline marker does).

## Engines

1. **You.com** — default answer mode.
2. **Brave Search** — the AI answer on `search.brave.com` (`summary=1`). Leo, the browser assistant,
   is a Brave-browser feature and is not observable from a plain Chromium.
3. **Arc** — Arc Search / *Browse for me*: a macOS / Windows / iOS client. No Linux client.
4. **Claude with web search** — for the chapter's separate claim that *when* Claude cites, the
   citation is a clickable URL.

An engine that cannot be observed under the rules below is recorded as **not observed** and the
chapter does not describe it.

## Queries

Six, fixed before any result was seen. Three factual, two matters of opinion, one event:

1. `what is the half-life of caesium-137`
2. `who won the 2022 Fields Medal`
3. `how does HTTP/3 differ from HTTP/2`
4. `is intermittent fasting effective for weight loss`
5. `best programming language for data science`
6. `what happened in the Suez Canal blockage`

## Procedure

1. **Clean session:** a new browser context per query — no cookies, no login, no history.
   Personalisation changes the answer.
2. Every engine gets the six queries in the same order, **one pass each**. This describes what
   the product does on one day; repeating it would not make it a population estimate.
3. Per answer: `engine | query | inline marker yes/no | sources only below yes/no | note`, plus
   the timestamp with time zone at the start and end of each engine, and one screenshot per engine
   of the first query.

## Observation of 2026-09-13

Start / end: **21:06 / 21:07 UTC**. Location: Spain (a server, datacenter IP). Chromium 128 driven
through the DevTools protocol; a fresh incognito-style context per query.

| engine | q1 | q2 | q3 | q4 | q5 | q6 | inline / observed |
|---|---|---|---|---|---|---|---|
| Brave Search, AI answer | yes (3) | yes (7) | yes (12) | yes (6) | yes (5) | yes (4) | **6 / 6** |
| You.com | — | — | — | — | — | — | not observed: `/search` redirects to `/signin` in a clean session |
| Arc | — | — | — | — | — | — | not observed: no Linux client |
| Claude with web search | — | — | — | — | — | — | not observed: requires an account, which the clean-session rule excludes |

Numbers in parentheses are inline markers counted in the DOM of the answer block
(`button.inline-citation` inside `.llm-output`). All six Brave answers also carried a **sources
list under the answer** (both forms at once, not one or the other).

![Brave Search AI answer, query 1, with inline citation chips](img/brave-2026-09-13-q1.png)

**Limits of this pass, stated so nobody over-reads it:**

- The Brave marker is a link-icon **button** that opens the source on click; it carries no `href`
  in the page source. Its click-through was recorded by the run script but **not re-verified by
  eye**, because two follow-up requests for query 1, minutes after the pass, returned **no AI
  answer at all** — the same query, the same clean context. Whether that was throttling after eight
  requests from one IP or ordinary variance, it means *"nearly every answer"* is not a stable
  property of the product; it is what one pass saw.
- One pass, one location, one day. These products change without notice; the chapter says so.
- For Claude, the chapter's claim is now sourced to Anthropic's own documentation of the web
  search tool (citations with source URL, title and cited text) rather than to a blog; this
  protocol did not observe the product.

## How to repeat

Open `https://search.brave.com/search?q=<query>&source=web&summary=1` in a fresh context, wait for
`.llm-output.llm-output-complete`, count `button.inline-citation` inside it, and screenshot. For
You.com, first check whether `https://you.com/search?q=<query>&tbm=youchat` still redirects to a
sign-in page; if it no longer does, the six queries apply as above. Record the timestamp, the
location and the browser; keep the query list and order fixed; if a query is changed, restart the
engine.
