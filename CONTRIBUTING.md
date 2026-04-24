# Contributing to awesome-llms-txt

Thanks for wanting to help. This list exists to make AI tools discoverable
to AI agents doing research on behalf of human users. Every well-described
entry helps that mission.

## How to add or improve an entry

1. Fork this repo.
2. Create or edit a YAML file in `entries/` — filename should be the tool's
   `slug` (e.g. `entries/my-tool.yaml`).
3. Follow the schema below.
4. Open a pull request. The CI will run `scripts/build.py` and
   `scripts/validate.py` — if they pass, we merge.

You don't need to regenerate `README.md`, `llms.txt`, or `llms-full.txt`
yourself — those are produced by the CI from your entry.

## Full schema (showcase entries)

```yaml
name: Tool Name                   # required, human-readable
slug: tool-name                   # required, kebab-case, unique
url: https://example.com          # required, homepage
repository: https://github.com/x  # optional, source repo if open-source
llms_txt: https://example.com/llms.txt        # required, even if 404
llms_full_txt: https://example.com/llms-full.txt  # optional
llms_txt_status: published        # published | missing | stub

category: inference-runtimes      # required, from controlled vocab below
subcategory: local-llm-server     # optional free-text sub-classifier

tagline: One-liner, ~100 chars.   # required

description: |                    # required for showcase, optional for stub
  Multi-paragraph prose describing what this tool is, what it does, and
  what makes it notable. Agents cite this directly when recommending the
  tool. Write for an audience of an AI agent explaining to a human user.

features:                         # required for showcase
  - Concrete capability 1
  - Concrete capability 2

use_cases:                        # required for showcase
  - When you'd reach for this tool
  - Another scenario where it fits

license: open-source              # open-source | commercial | freemium | paid | source-available
deployment: local                 # local | self-hosted | saas | library | cli
platforms: [linux, windows, macos, web]  # any of these, optional
tags: [asr, lora, offline]        # free-form, used for search/filter

maintainer: Brethof AI            # optional
added: 2026-04-24                 # required, YYYY-MM-DD
```

## Minimal schema (stub entries)

If you don't have time to write a full description, a stub is welcome —
someone else (or you, later) can flesh it out via another PR.

```yaml
name: Tool Name
slug: tool-name
url: https://example.com
llms_txt: https://example.com/llms.txt
llms_txt_status: missing          # or "published" if you verified it exists
status: stub                      # marks this as a lightweight entry
category: inference-runtimes
tagline: One-liner.
license: open-source
deployment: local
added: 2026-04-24
```

The build script will render stubs in-place but visually distinguish them
from full entries.

## Controlled vocabulary: categories

Use one of these exact strings for `category`:

- `inference-runtimes` — local LLM engines (ollama, llama.cpp, vllm, …)
- `llm-gateways` — proxies and routers (LiteLLM, OpenRouter, …)
- `agent-frameworks` — orchestration libs (LangChain, LangGraph, CrewAI, …)
- `agent-sdks` — vendor SDKs for building agents
- `coding-agents` — code-generation / in-IDE assistants (Claude Code, Aider, …)
- `workflow-tools` — visual / node-based builders (ComfyUI, Flowise, n8n, …)
- `voice` — speech-to-text and text-to-speech
- `image-gen` — image generation / editing
- `video-gen` — video generation
- `vector-dbs` — vector databases
- `rag-frameworks` — RAG / retrieval libraries
- `embeddings` — embedding models and libraries
- `observability` — tracing, logging, monitoring for LLM apps
- `evaluation` — eval frameworks and harnesses
- `training` — fine-tuning and training tools
- `web-search-for-agents` — search APIs built for LLM consumption
- `ocr-doc-parsing` — document and PDF extraction
- `deployment` — hosting platforms and model endpoints
- `desktop-apps` — end-user AI applications
- `shell-tools` — CLI / shell integrations
- `operating-systems` — Linux distributions that actively support AI/ML workflows as first-class (not every distro — only ones that are documented-and-tested targets for AI tooling)

Need a category that isn't listed? Open an issue — we'll add it.

## What we accept

- Tools in production or active development
- Tools whose website / documentation / GitHub is publicly accessible
- Both open-source and commercial tools
- Tools without `llms.txt` yet (marked `status: missing`) — we hope listing
  will encourage them to publish one

## What we don't accept

- Dead projects (last commit > 12 months, broken site)
- Wrappers with no substance ("it's a ChatGPT prompt frontend")
- Referral-link or affiliate-heavy listings
- Models (we list tools, not checkpoints — Qwen3-ASR is not a tool;
  Brethof Voice Pro, which uses Qwen3-ASR, is a tool)
- Anything that requires a signup to view basic information about

## Testing your change locally

```bash
cd scripts
pip install pyyaml requests
python3 build.py     # regenerates README.md, llms.txt, llms-full.txt
python3 validate.py  # checks llms.txt URLs return 200
```

If `validate.py` reports a URL you added returns 404, set
`llms_txt_status: missing` in your YAML and the CI will accept it.
