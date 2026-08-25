# Weekly updates log

GEO changes almost weekly — engines ship new features, cite differently, expose new controls, and fresh research lands. This folder is the handbook's **running record** so readers can see *when* guidance changed and *why*.

## How it works

- **One file per ISO week**, named `YYYY-Www.md` — for example `2026-W35.md` (ISO week 35 of 2026). See <https://en.wikipedia.org/wiki/ISO_week_date> if you're unsure which week a date falls in.
- Each file captures two things:
  1. **What's new in GEO** — notable changes in the wider landscape (engine/vendor announcements, new research, measured shifts in how AI answers cite sources). **Cited**, like everything else here.
  2. **What changed in this repo** — chapters edited, techniques added/revised, links fixed. Cross-reference the relevant PRs/issues.
- Weeks with nothing material still get a one-line "no material change this week" entry, so the timeline is continuous and gaps are intentional, not forgotten.

## Template for a weekly file

Copy this into a new `YYYY-Www.md`:

```markdown
# YYYY-Www (Mon DD – Sun DD, YYYY)

## What's new in GEO
- **[Area] Headline.** One or two sentences, present tense. ([Source](https://…))
  - Why it matters for GEO practitioners.

## What changed in this repo
- Short bullet per notable merge. (#PR)

## Watching / needs verification
- Things we've seen but haven't confirmed yet — flagged so next week's pass can chase them.
```

## Relationship to the changelog

- **`updates/`** is the granular, weekly, landscape-plus-repo journal.
- **[`CHANGELOG.md`](../CHANGELOG.md)** is the higher-level milestone summary in [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.

When a weekly change is significant enough to matter months from now, promote a line from the weekly file into `CHANGELOG.md`.
