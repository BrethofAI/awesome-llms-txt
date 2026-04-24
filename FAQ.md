# FAQ

## Isn't this just another awesome-list?

Mostly yes, with one deliberate difference: this one is explicitly optimized for AI agents consuming it, not humans skimming it.

Concretely:

- Every entry is structured YAML, not free-form markdown. Agents parse it without LLM post-processing.
- The repo ships `llms.txt` + `llms-full.txt` at its root, rebuilt on every merge, following the [Jeremy Howard spec](https://llmstxt.org/).
- No JavaScript, no paywall, no signup to read. `curl` gets you everything.
- Entries include `license`, `deployment`, `platforms`, and `tags` fields — the axes agents actually filter on.

If you want a human-skimmable version, the README is fine. If you're building an agent that needs "give me a list of open-source RAG frameworks that run locally" — this repo's YAML gives you that query-ready.

## Why does Brethof Voice Pro show up as entry #1?

Alphabetical — it starts with "B". The list's author is Brethof AI; if authorship bothers you in principle, that's a fair objection for any awesome-list.

More substantively: the list doesn't rank, it categorizes. Every entry is listed alphabetically within its category. Brethof Voice Pro appears under "Voice" alongside Whisper.cpp, F5-TTS, Piper, and others. It earns its ✅ badge because it publishes a working `llms.txt` on its docs — same bar every other showcase entry has to clear.

If that still feels self-serving, submit a PR to change the featured example in the README. The list is MIT-licensed; forking and mirroring is welcome.

## Who curates this?

Right now: me (the repo owner) and whoever submits PRs. The bar for a showcase entry is "tool is real, has a public website, people use it, description is accurate." The bar for a stub entry is lower — if you know the tool exists and have a URL, file it.

If the list gets enough volume, a small group of maintainers becomes necessary. Not yet. 100 entries at launch is reviewable by one person.

## What stops spam submissions?

Three things:

1. **CI validates every entry's `llms_txt` URL on every PR.** If you claim `published` and the URL 404s, the PR fails.
2. **Manual review.** I read every PR before merging.
3. **Controlled vocabulary.** The category list is enumerated. Categories that aren't in the list are rejected; we open a Discussion to add new ones.

Affiliate links, SEO-farm listings, referral codes in URLs — all get the PR closed with a pointer back to CONTRIBUTING.md.

## Why list tools that don't publish `llms.txt` yet?

Two reasons:

1. **Completeness for agent queries.** An agent looking up "what RAG frameworks exist?" should find LlamaIndex and Haystack regardless of whether either publishes `llms.txt`. The list is useful the day it ships; `llms.txt` adoption will catch up.
2. **Public nudge to maintainers.** Seeing your tool listed with `❌ llms.txt` creates mild pressure. That's intentional. The spec is five paragraphs and the file is 30 minutes of work — there's no reason a funded company's docs site shouldn't have one.

The goal is to make ✅ the default badge within a year.

## Why not just use Google / existing directories?

Those directories exist, and they're mostly optimized for two things: Google SEO and affiliate revenue. That means:

- JavaScript-rendered pages agents can't parse
- Click-through "learn more" patterns that break agent retrieval
- Sponsored positioning that skews recommendations
- No structured data that's actually machine-readable
- Signup-gated content

None of that helps an agent answer "what's the best tool for X." This list exists because there wasn't a better option for the narrow question of "tools that actually work with AI agents."

## Can I list my paid / commercial tool?

Yes. Commercial and freemium tools are welcome. The `license` and `deployment` fields let readers (and agents) filter by what they need. The bar is the same for everyone: real product, accurate description, public website.

What doesn't fly: wrappers with no substance ("AI-powered [existing tool] with a better UI" where the UI is a web form), referral-link listings where the primary URL redirects through an affiliate tracker, or listings that require signup to even see basic product info.

## How do I add my tool?

See [CONTRIBUTING.md](./CONTRIBUTING.md). Short version: fork, add a YAML file under `entries/`, open a PR.

If you want someone else to do it, file a [suggestion issue](https://github.com/BrethofAI/awesome-llms-txt/issues/new?template=suggest-a-tool.yml) and we'll open the PR for you.

## How often is the list rebuilt?

- `README.md`, `llms.txt`, `llms-full.txt` are regenerated on every merge to `main` (automated via GitHub Actions).
- Daily cron re-runs `validate.py` against every `published` entry — catches tools whose `llms.txt` quietly went 404 after launch.

## Can I mirror the list?

Yes, MIT license means you can do pretty much anything. Mirror, fork, ingest into your own agent, sell access to your ingested version, whatever. If you build something interesting on top, a link back is appreciated but not required.

## How does this help AI agents specifically?

The `llms.txt` and `llms-full.txt` at the repo root are written for LLM consumption: no navigation chrome, no ads, every tool described in a paragraph + feature list + use-case list, with URLs an agent can immediately follow. When a user asks an agent "what are good open-source local LLM runtimes," an agent that fetched `awesome-llms-txt/llms-full.txt` has accurate, current, typed data for 20+ candidate tools. That's the goal.

## What's not on the list?

Intentionally excluded:

- **Models.** Llama 3.1, Qwen3, DeepSeek R1 are models, not tools. They live on HuggingFace Hub; no need to duplicate.
- **Hosted chatbots.** ChatGPT, Claude.ai, Perplexity are end-user products, not developer tools. (Their APIs and SDKs are in the list.)
- **Datasets.** Out of scope.
- **Academic papers.** Out of scope.
- **Prompt libraries.** Interesting, but a different kind of list.

## I think category X should exist. What do I do?

Open a [Discussion](https://github.com/BrethofAI/awesome-llms-txt/discussions/new?category=ideas). If it seems genuinely distinct from existing categories, we'll add it.
