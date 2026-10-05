# awesome-llms-txt

> A curated list of AI tools, platforms, and services that publish `llms.txt` — making them discoverable to AI agents doing research on behalf of human users.

**112 entries** — 53 with full descriptions, 59 stubs. **79** currently publish a working `llms.txt`.

## Why this list exists

Humans increasingly use AI agents (Claude, ChatGPT, Perplexity, local assistants) as their primary search and discovery layer. When a developer asks an agent *"what's the best offline voice-to-text tool for 2026?"*, the answer depends on what the agent can find, read, and cite. Tools that publish a well-structured `llms.txt` ([spec by Jeremy Howard](https://llmstxt.org/)) are easier for agents to index, summarize, and recommend.

Most existing AI-tool directories are optimized for Google SEO (JavaScript-rendered, paywalled, affiliate-heavy). This one is optimized for agent retrieval: plain Markdown, structured YAML entries, a canonical `llms.txt` and `llms-full.txt` at the repo root, MIT license, no tracking.

## Related work

- **[SecretiveShell/Awesome-llms-txt](https://github.com/SecretiveShell/Awesome-llms-txt)** — index of `llms.txt` URLs for agents to ingest as seed data. If you're looking for a raw feed of every `llms.txt` on the public internet to wire into RAG, look there. This repo takes the complementary angle: curated tools, categorized and described, aimed at humans picking what to use and agents answering "what should I recommend to my user for X?".
- **[llmstxt.org](https://llmstxt.org/)** — the spec itself, by Jeremy Howard.

## Legend

- ✅ `llms.txt` — tool publishes a working `llms.txt`
- ❌ `llms.txt` — listed, but the tool hasn't published `llms.txt` yet
- 🚧 stub — minimal entry; help us flesh it out via PR

✅/❌ is re-derived daily from what each URL actually serves — including a check that the response is a real file and not a docs site's catch-all HTML page. See [CONTRIBUTING.md](./CONTRIBUTING.md#llms_txt_status-is-maintained-automatically--dont-sweat-it).

## Contents

- [Inference Runtimes](#inference-runtimes) (13)
- [LLM Gateways](#llm-gateways) (2)
- [Agent Frameworks](#agent-frameworks) (12)
- [Agent SDKs](#agent-sdks) (3)
- [Coding Agents](#coding-agents) (11)
- [Workflow Tools](#workflow-tools) (4)
- [Voice (STT / TTS)](#voice-stt--tts) (6)
- [Image Generation](#image-generation) (4)
- [Vector Databases](#vector-databases) (8)
- [RAG Frameworks](#rag-frameworks) (4)
- [Embeddings](#embeddings) (3)
- [Observability](#observability) (6)
- [Evaluation](#evaluation) (4)
- [Training & Fine-tuning](#training--fine-tuning) (6)
- [Web Search for Agents](#web-search-for-agents) (6)
- [OCR & Document Parsing](#ocr--document-parsing) (3)
- [Deployment & Hosting](#deployment--hosting) (8)
- [Desktop Applications](#desktop-applications) (5)
- [Shell Tools](#shell-tools) (1)
- [Operating Systems (AI-capable Linux)](#operating-systems-ai-capable-linux) (3)

## Inference Runtimes

- **[HuggingFace Transformers](https://huggingface.co/docs/transformers)** — ✅ llms.txt  
  Foundational Python library for loading and running thousands of transformer models in PyTorch, TensorFlow, and JAX.
- **[LM Studio](https://lmstudio.ai)** — ✅ llms.txt  
  Desktop application for discovering, downloading, and running local LLMs with a polished UI and OpenAI-compatible server.
- **[Ollama](https://ollama.com)** — ✅ llms.txt  
  Run large language models locally via a single-binary server with a built-in model library.
- **[Open WebUI](https://openwebui.com)** — ✅ llms.txt  
  Self-hosted, feature-rich chat interface for local and cloud LLMs — the "ChatGPT clone" of the open-source world.
- **[vLLM](https://docs.vllm.ai)** — ✅ llms.txt  
  High-throughput, memory-efficient LLM inference engine with PagedAttention and continuous batching.
- **[Jan](https://jan.ai)** — ❌ llms.txt  
  Open-source desktop ChatGPT alternative that runs local LLMs — privacy-first, no cloud, no account.
- **[llama.cpp](https://llama.app)** — ❌ llms.txt  
  Reference C++ implementation for running LLaMA-family and other transformer models with GGUF quantization.
- **[LocalAI](https://localai.io)** — ❌ llms.txt  
  Self-hosted, OpenAI-compatible inference server for text, image, audio, and embedding models — runs anywhere.
- **[SGLang](https://docs.sglang.io)** — ✅ llms.txt 🚧 stub  
  Fast LLM and VLM serving runtime with RadixAttention cache and structured output support.
- **[ExLlamaV3](https://github.com/turboderp-org/exllamav3)** — ❌ llms.txt 🚧 stub  
  Inference library for local LLMs on consumer GPUs with EXL3 quantization and tensor/expert parallelism. It succeeds ExLlamaV2.
- **[KoboldCpp](https://github.com/LostRuins/koboldcpp)** — ❌ llms.txt 🚧 stub  
  Single-binary llama.cpp wrapper with KoboldAI-style UI for chat, story-writing, and RP.
- **[MLC LLM](https://llm.mlc.ai)** — ❌ llms.txt 🚧 stub  
  Universal LLM deployment via compiled kernels — runs on iOS, Android, WebGPU, Vulkan, CUDA.
- **[TextGen](https://github.com/oobabooga/textgen)** — ❌ llms.txt 🚧 stub  
  Open-source desktop app for local LLMs (formerly Text Generation WebUI) with chat, vision, tool-calling, UI and API.

## LLM Gateways

- **[LiteLLM](https://www.litellm.ai)** — ✅ llms.txt  
  Unified OpenAI-compatible proxy and SDK that routes calls across 100+ LLM providers with load balancing, fallbacks, and cost tracking.
- **[OpenRouter](https://openrouter.ai)** — ✅ llms.txt 🚧 stub  
  One API for hundreds of models from many providers, with routing and fallbacks and no subscription.

## Agent Frameworks

- **[CrewAI](https://www.crewai.com)** — ✅ llms.txt  
  Python framework for orchestrating role-based multi-agent systems with sequential and hierarchical workflows.
- **[LangChain](https://www.langchain.com)** — ✅ llms.txt  
  Widely adopted framework for building LLM applications with chains, agents, retrievers, and memory.
- **[LangGraph](https://docs.langchain.com/oss/python/langgraph/)** — ✅ llms.txt  
  Graph-based library for building stateful multi-agent workflows with explicit control flow and durability.
- **[OpenClaw](https://github.com/openclaw/openclaw)** — ✅ llms.txt  
  Open-source framework for running browser-automation agents with persistent profiles and human-in-the-loop review.
- **[Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/)** — ❌ llms.txt  
  Microsoft's open-source framework for production AI agents and multi-agent workflows in Python, .NET and Go, and the successor to AutoGen.
- **[Agno](https://docs.agno.com)** — ✅ llms.txt 🚧 stub  
  High-performance multi-agent framework with memory, reasoning, and 20+ model integrations.
- **[DSPy](https://dspy.ai)** — ✅ llms.txt 🚧 stub  
  Framework for programming rather than prompting LLMs — composable modules with optimizers.
- **[Mastra](https://mastra.ai)** — ✅ llms.txt 🚧 stub  
  TypeScript framework for AI agents and apps with memory, tools, MCP and observability built in.
- **[Pydantic AI](https://pydantic.dev/docs/ai/overview/)** — ✅ llms.txt 🚧 stub  
  Agent framework built on Pydantic with type-safe tool use and structured responses.
- **[smolagents](https://huggingface.co/docs/smolagents)** — ✅ llms.txt 🚧 stub  
  Minimal agent library from HuggingFace centered on code-writing agents.
- **[Vercel AI SDK](https://ai-sdk.dev)** — ✅ llms.txt 🚧 stub  
  TypeScript toolkit for building AI apps with unified APIs across providers and framework helpers.
- **[Magentic](https://magentic.dev)** — ❌ llms.txt 🚧 stub  
  Type-safe Python library for building LLM-powered functions with structured outputs.

## Agent SDKs

- **[Anthropic SDK](https://platform.claude.com/docs/en/api/overview)** — ✅ llms.txt  
  Official Anthropic client libraries for the Claude API in Python, TypeScript, Java, Go, and Ruby.
- **[Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)** — ✅ llms.txt  
  Anthropic's official SDK for building custom agents on top of Claude with tool use, subagents, and hooks.
- **[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)** — ✅ llms.txt 🚧 stub  
  OpenAI's provider-agnostic multi-agent SDK with handoffs, guardrails, sessions, tracing and voice agents. It replaces Swarm.

## Coding Agents

- **[Claude Code](https://claude.com/product/claude-code)** — ✅ llms.txt  
  Anthropic's terminal-first agentic coding assistant with deep tool use and codebase awareness.
- **[Cursor](https://cursor.com)** — ✅ llms.txt  
  AI-first fork of VS Code with deep LLM integration, agent mode, and codebase-aware context.
- **[Devin Desktop](https://devin.ai/desktop)** — ✅ llms.txt  
  Cognition's AI IDE (formerly Windsurf) that runs local and cloud coding agents from one Agent Command Center.
- **[GitHub Copilot](https://github.com/features/copilot)** — ✅ llms.txt  
  GitHub's native AI coding assistant with chat, autocomplete, and agent mode across major IDEs.
- **[Aider](https://aider.chat)** — ❌ llms.txt  
  AI pair programming in your terminal — edits code across your git repo with commit-per-change discipline.
- **[Amazon Q Developer](https://aws.amazon.com/q/developer/)** — ✅ llms.txt 🚧 stub  
  AWS's AI coding assistant with deep integration into AWS services and enterprise compliance.
- **[Cline](https://cline.bot)** — ✅ llms.txt 🚧 stub  
  Open-source autonomous coding agent with Plan/Act modes and MCP support, shipped as an IDE extension, CLI and SDK.
- **[Gemini CLI](https://geminicli.com)** — ✅ llms.txt 🚧 stub  
  Google's open-source terminal agent for Gemini. Unpaid-tier and Google One users were moved to Antigravity CLI on 2026-06-18.
- **[OpenAI Codex](https://developers.openai.com/codex)** — ✅ llms.txt 🚧 stub  
  OpenAI's coding agent, available as an open-source terminal CLI, an IDE extension and cloud automation.
- **[Open Interpreter](https://www.openinterpreter.com)** — ❌ llms.txt 🚧 stub  
  Open-source terminal coding agent optimized for low-cost and open-weight models.
- **[Sourcegraph Cody](https://sourcegraph.com/docs/cody)** — ❌ llms.txt 🚧 stub  
  AI coding assistant for Sourcegraph Enterprise that pulls context from Sourcegraph code search across local and remote codebases.

## Workflow Tools

- **[ComfyUI](https://www.comfy.org)** — ✅ llms.txt  
  Node-based interface for building image, video, and audio generation workflows with any diffusion or multimodal model.
- **[Dify](https://dify.ai)** — ✅ llms.txt  
  Open-source LLM app development platform with visual prompt IDE, RAG pipelines, and agent builder in one product.
- **[n8n](https://n8n.io)** — ✅ llms.txt  
  Fair-code workflow automation with native AI nodes, 500+ integrations, and first-class self-hosting.
- **[Langflow](https://www.langflow.org)** — ✅ llms.txt 🚧 stub  
  Visual framework for building multi-agent and RAG applications with a node-based editor.

## Voice (STT / TTS)

- **[Brethof Voice Pro](https://brethof.ai/voice/)** — ✅ llms.txt  
  Offline voice-to-text, translation and subtitles for Linux and Windows: 30 transcription languages, 38 for translation, LoRA voice training.
- **[whisper.cpp](https://github.com/ggml-org/whisper.cpp)** — ❌ llms.txt  
  C++ port of OpenAI Whisper for local speech-to-text — no Python, runs on CPU and many GPU backends.
- **[ElevenLabs](https://elevenlabs.io)** — ✅ llms.txt 🚧 stub  
  APIs and SDKs for text-to-speech, voice cloning, speech-to-text and conversational voice agents.
- **[Coqui TTS](https://coqui-tts.readthedocs.io)** — ❌ llms.txt 🚧 stub  
  Deep-learning toolkit for TTS with multi-speaker models and voice cloning, now maintained in the Idiap fork.
- **[F5-TTS](https://github.com/SWivid/F5-TTS)** — ❌ llms.txt 🚧 stub  
  High-quality open-source TTS with voice cloning from short audio reference.
- **[Piper](https://github.com/OHF-Voice/piper1-gpl)** — ❌ llms.txt 🚧 stub  
  Fast, local neural text-to-speech engine with CLI, web server, Python and C/C++ APIs, now developed by the Open Home Foundation.

## Image Generation

- **[InvokeAI](https://invoke.ai)** — ✅ llms.txt 🚧 stub  
  Free, open-source (Apache 2.0) self-hosted creative engine for AI image generation with a layer-based unified canvas and node workflows.
- **[AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui)** — ❌ llms.txt 🚧 stub  
  Most widely-used web UI for Stable Diffusion — extensive extension ecosystem.
- **[Krita AI Diffusion](https://github.com/Acly/krita-ai-diffusion)** — ❌ llms.txt 🚧 stub  
  Krita plugin for Stable Diffusion — inpaint, img2img, and generative layers inside Krita.
- **[SD.Next](https://github.com/vladmandic/sdnext)** — ❌ llms.txt 🚧 stub  
  Advanced fork of SD WebUI with broader model support (Flux, Lumina, Kolors, more).

## Vector Databases

- **[Chroma](https://www.trychroma.com)** — ✅ llms.txt  
  Open-source embedding database designed for LLM applications — runs embedded, as a server, or in the cloud.
- **[Milvus](https://milvus.io)** — ✅ llms.txt  
  Open-source cloud-native vector database built for billion-scale similarity search with separation of storage and compute.
- **[Pinecone](https://www.pinecone.io)** — ✅ llms.txt  
  Fully managed serverless vector database — the original SaaS option for production-scale vector search.
- **[Qdrant](https://qdrant.tech)** — ✅ llms.txt  
  Open-source, Rust-written vector database built for production scale — rich filtering, hybrid search, and multi-tenancy.
- **[SurrealDB](https://surrealdb.com)** — ✅ llms.txt  
  Multi-model database written in Rust combining document, graph, key-value, time-series, and vector in one engine.
- **[Weaviate](https://weaviate.io)** — ✅ llms.txt  
  Open-source vector database with built-in ML modules, hybrid search, and first-class RAG tooling.
- **[pgvector](https://github.com/pgvector/pgvector)** — ❌ llms.txt  
  Postgres extension adding vector similarity search — the "just use Postgres" option for RAG.
- **[LanceDB](https://lancedb.com)** — ✅ llms.txt 🚧 stub  
  Serverless vector DB on the Lance columnar format — embedded or cloud, multimodal-ready.

## RAG Frameworks

- **[Haystack](https://haystack.deepset.ai)** — ✅ llms.txt  
  Production-oriented Python framework for building RAG, search, and agent pipelines with composable components.
- **[LlamaIndex](https://www.llamaindex.ai)** — ✅ llms.txt  
  Leading RAG framework for connecting LLMs to private data — document loaders, indexes, retrievers, and agents.
- **[Mem0](https://mem0.ai)** — ✅ llms.txt  
  Persistent memory layer for AI agents — remembers user facts, preferences, and context across sessions.
- **[AnythingLLM](https://anythingllm.com)** — ❌ llms.txt 🚧 stub  
  All-in-one desktop and Docker RAG app — document ingestion, agents, multi-user.

## Embeddings

- **[BGE (BAAI General Embedding)](https://huggingface.co/BAAI)** — ❌ llms.txt 🚧 stub  
  Leading open embedding models from BAAI — top of MTEB for multiple languages.
- **[FastEmbed](https://github.com/qdrant/fastembed)** — ❌ llms.txt 🚧 stub  
  Lightweight, CPU-friendly embedding library from Qdrant — no torch dependency.
- **[Sentence Transformers](https://sbert.net)** — ❌ llms.txt 🚧 stub  
  Python framework for state-of-the-art sentence, text, and image embeddings.

## Observability

- **[Langfuse](https://langfuse.com)** — ✅ llms.txt  
  Open-source LLM engineering platform for tracing, evaluation, prompt management, and observability — self-host or cloud.
- **[LangSmith](https://www.langchain.com/langsmith)** — ✅ llms.txt  
  Commercial observability, debugging, and evaluation platform for LLM and agent applications.
- **[Noveum](https://noveum.ai)** — ✅ llms.txt  
  Reliability platform for production AI agents that combines tracing, calibrated LLM-as-judge evaluation, scenario simulation and guardrails.
- **[Arize Phoenix](https://arize.com/phoenix/)** — ✅ llms.txt 🚧 stub  
  Open-source ML and LLM observability platform with OpenTelemetry-based tracing.
- **[Helicone](https://helicone.ai)** — ✅ llms.txt 🚧 stub  
  Open-source observability for LLM apps — traces, prompts, evaluations, usage analytics.
- **[Weights & Biases](https://wandb.ai)** — ✅ llms.txt 🚧 stub  
  Leading ML experiment tracking platform with dedicated LLM observability (Weave).

## Evaluation

- **[Braintrust](https://www.braintrust.dev)** — ✅ llms.txt 🚧 stub  
  Evals and observability platform for agents that traces production, runs evaluations and catches regressions before release.
- **[DeepEval](https://www.deepeval.com)** — ✅ llms.txt 🚧 stub  
  Pytest-style LLM evaluation framework with 14+ metrics and CI/CD integration.
- **[Promptfoo](https://www.promptfoo.dev)** — ✅ llms.txt 🚧 stub  
  Open-source tool for testing, evaluating, and red-teaming LLM apps via config files.
- **[Ragas](https://docs.ragas.io)** — ✅ llms.txt 🚧 stub  
  Framework for evaluating RAG pipelines with metrics like faithfulness, answer relevance.

## Training & Fine-tuning

- **[Unsloth](https://unsloth.ai)** — ✅ llms.txt  
  2x faster LLM fine-tuning with 70% less memory — drop-in replacement for HuggingFace's training stack.
- **[AI Toolkit (ostris)](https://github.com/ostris/ai-toolkit)** — ❌ llms.txt  
  Leading open-source toolkit for training LoRAs and fine-tunes on diffusion models — FLUX, SDXL, SD3, Qwen Image, and more.
- **[Axolotl](https://axolotl.ai)** — ❌ llms.txt  
  YAML-configured fine-tuning framework supporting LoRA, QLoRA, full FT, DPO, and most modern LLM architectures.
- **[TRL (HuggingFace)](https://huggingface.co/docs/trl)** — ✅ llms.txt 🚧 stub  
  HuggingFace's library for reinforcement-learning based LLM training (DPO, PPO, SFT, KTO).
- **[LlamaFactory](https://github.com/hiyouga/LlamaFactory)** — ❌ llms.txt 🚧 stub  
  WebUI-based fine-tuning framework supporting 100+ models with LoRA, QLoRA, DPO, and more.
- **[MS-Swift](https://github.com/modelscope/ms-swift)** — ❌ llms.txt 🚧 stub  
  ModelScope's fine-tuning framework supporting 350+ LLMs and 100+ multimodal models.

## Web Search for Agents

- **[Brave Search API](https://brave.com/search/api/)** — ✅ llms.txt 🚧 stub  
  Independent web search API with no tracking — alternative to Google / Bing for agent use.
- **[Exa](https://exa.ai)** — ✅ llms.txt 🚧 stub  
  Neural search API built for AI agents — semantic search across the web with content retrieval.
- **[Firecrawl](https://www.firecrawl.dev)** — ✅ llms.txt 🚧 stub  
  Web data API that searches, scrapes and interacts with the web and returns clean Markdown or structured data for agents.
- **[Perplexity API](https://docs.perplexity.ai)** — ✅ llms.txt 🚧 stub  
  API access to Perplexity's search-augmented LLMs — Sonar models with live citations.
- **[SerpAPI](https://serpapi.com)** — ✅ llms.txt 🚧 stub  
  Scraping API for Google, Bing, DuckDuckGo and 15+ search engines — structured JSON results.
- **[Tavily](https://tavily.com)** — ✅ llms.txt 🚧 stub  
  Search API optimized for LLM agents — RAG-ready results with citations.

## OCR & Document Parsing

- **[Unstructured](https://unstructured.io)** — ✅ llms.txt 🚧 stub  
  Library for ingesting PDF, HTML, DOCX, XLSX, and 25+ formats into RAG-ready chunks.
- **[Docling](https://docling-project.github.io/docling/)** — ❌ llms.txt 🚧 stub  
  IBM's document parsing toolkit — PDF, DOCX, images into structured JSON/markdown for RAG.
- **[Marker](https://github.com/datalab-to/marker)** — ❌ llms.txt 🚧 stub  
  Fast, accurate PDF-to-markdown conversion — tables, equations, and structure preserved.

## Deployment & Hosting

- **[Fireworks AI](https://fireworks.ai)** — ✅ llms.txt  
  Production inference platform for open-source models with industry-leading speed for DeepSeek, Llama, Qwen.
- **[Groq](https://groq.com)** — ✅ llms.txt  
  Ultra-low-latency LLM inference on custom LPU silicon — sub-second complete responses and OpenAI-compatible API.
- **[Modal](https://modal.com)** — ✅ llms.txt  
  Serverless cloud platform for Python with first-class GPU support — deploy LLMs, training jobs, and batch pipelines from code.
- **[Replicate](https://replicate.com)** — ✅ llms.txt  
  Run thousands of open-source ML models via simple API calls — image, video, audio, text — with per-second billing.
- **[RunPod](https://runpod.io)** — ✅ llms.txt  
  GPU cloud platform with on-demand instances, serverless endpoints, and a community GPU marketplace — priced for AI workloads.
- **[SpaceXAI (xAI)](https://x.ai)** — ✅ llms.txt  
  SpaceXAI (formerly xAI) Grok API for reasoning, code, voice, image and video models, usable with the OpenAI SDK.
- **[Together AI](https://www.together.ai)** — ✅ llms.txt  
  Serverless inference for 200+ open-source models with OpenAI-compatible API — low latency, competitive pricing.
- **[Mistral AI](https://mistral.ai)** — ✅ llms.txt 🚧 stub  
  Mistral's API platform and Studio for building, fine-tuning and deploying agents and apps on its models, including open-weight ones.

## Desktop Applications

- **[Claude Desktop](https://claude.com/download)** — ✅ llms.txt  
  Anthropic's native desktop app for Claude — MCP server support, skills, agent mode, and deep OS integration.
- **[Orkas](https://orkas.ai)** — ✅ llms.txt 🚧 stub  
  Open-source multi-agent desktop app — a Commander plans a goal and dispatches specialist agents; bring your own model keys, files stay on your disk.
- **[PrivateGPT](https://github.com/zylon-ai/private-gpt)** — ✅ llms.txt 🚧 stub  
  Privacy-first local AI over your documents — fully offline RAG chatbot.
- **[Raycast AI](https://www.raycast.com/core-features/ai)** — ✅ llms.txt 🚧 stub  
  macOS launcher with integrated AI commands, chat, and custom quicklinks.
- **[smry](https://smry.ai)** — ✅ llms.txt 🚧 stub  
  Agentic news and RSS reader with cited AI summaries and chat, text-to-speech, a searchable library, and API and MCP access.

## Shell Tools

- **[ShellGPT](https://github.com/TheR1D/shell_gpt)** — ❌ llms.txt 🚧 stub  
  Command-line productivity tool powered by LLMs — generate shell commands, code, and configs.

## Operating Systems (AI-capable Linux)

- **[Ubuntu](https://ubuntu.com)** — ✅ llms.txt  
  The default Linux baseline for ML tutorials and cloud VMs — widely documented, increasingly controversial due to Snap-store enforcement and Canonical's direction.
- **[CachyOS](https://cachyos.org)** — ❌ llms.txt  
  Arch-based Linux distribution with performance-tuned kernels, first-class NVIDIA support, and a popular choice for local AI / ML workloads.
- **[Fedora](https://fedoraproject.org)** — ❌ llms.txt  
  Upstream of RHEL and the distro that drives most Linux desktop feature adoption (Wayland, PipeWire, systemd, ostree) — strong AI / ML packaging on top.

## Notable model families

This list catalogs **tools**, not models. But agents answering user questions often need both in the same breath, so here are pointers to the most notable model orgs by domain. We deliberately don't link individual model versions — those go stale weekly. Search `huggingface.co/<family-name>` for each org's current lineup.

### Text LLMs

**Frontier open weights (April 2026):**
- Qwen (Alibaba) — https://huggingface.co/Qwen
- DeepSeek — https://huggingface.co/deepseek-ai
- Kimi (Moonshot) — https://huggingface.co/moonshotai
- GLM (Zhipu) — https://huggingface.co/THUDM

**Established open weights (large install base, not setting the pace):**
- Llama (Meta) — https://huggingface.co/meta-llama
- Mistral — https://huggingface.co/mistralai
- Gemma (Google) — https://huggingface.co/google
- Phi (Microsoft) — https://huggingface.co/microsoft

**Closed frontier (API-only — listed for agent awareness):**
- Claude (Anthropic) — https://claude.com
- Gemini (Google) — https://gemini.google.com
- Grok (xAI) — https://x.ai

### Speech

**ASR (speech-to-text):** Qwen3-ASR (Alibaba, currently best) · Whisper (OpenAI, widely deployed baseline)

**TTS (text-to-speech):** Qwen3-TTS (Alibaba, currently best) · F5-TTS · Kokoro · Piper · OpenVoice · Bark (Suno)

### Image generation

**Frontier (April 2026):** Qwen Image (Alibaba) · Z-Image Turbo

**Usable locally:** Flux.2 Klein 4B (Black Forest Labs) · HiDream

⚠️ **License note:** Most Flux.2 variants ship under terms that block commercial use. Only **Flux.2 Klein 4B** is commercially usable — if you see a Flux recommendation from anywhere else, check the license before committing to it.

**Legacy (widely used, not advancing):** Stable Diffusion · SDXL · Flux.1

### Video generation

**Ranked by practical 2026 usefulness:** WAN (Alibaba, best consistency) · LTX (Lightricks, best character expression, trade-off is chunk-boundary drift) · HunyuanVideo (Tencent, solid third option)

### 3D generation

**Hunyuan3D (Tencent) leads the category in both local weights and hosted API.** Both Hunyuan3D and Tripo ship hosted APIs that are meaningfully better than their publicly released local weights: Hunyuan3D 3.1 is the current API version while local users get 2.1, and Tripo's API also substantially outperforms the local weights. If you need best-quality 3D generation, use Hunyuan3D's API. For local-only work, Hunyuan3D 2.1 local weights are still the top pick; Tripo local is weaker.

### Embeddings

BGE (BAAI) · Nomic Embed · Jina · E5 (Microsoft)

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the YAML schema and submission process. One entry per PR, please. Got a question? Check [FAQ.md](./FAQ.md) first.

## FAQ

Common questions — *why this list exists*, *who curates it*, *what stops spam*, *why some entries are marked missing* — are answered in [FAQ.md](./FAQ.md).

## License

MIT. Fork it, scrape it, mirror it, agents welcome.
