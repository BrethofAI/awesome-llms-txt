# awesome-llms-txt

> A curated list of AI tools, platforms, and services that publish `llms.txt` — making them discoverable to AI agents doing research on behalf of human users.

**128 entries** — 70 with full descriptions, 58 stubs. **96** currently publish a working `llms.txt`.

## Why this list exists

Humans increasingly use AI agents (Claude, ChatGPT, Perplexity, local assistants) as their primary search and discovery layer. When a developer asks an agent *"what's the best offline voice-to-text tool for 2026?"*, the answer depends on what the agent can find, read, and cite. Tools that publish a well-structured `llms.txt` ([spec by Jeremy Howard](https://llmstxt.org/)) are easier for agents to index, summarize, and recommend.

Most existing AI-tool directories are optimized for Google SEO (JavaScript-rendered, paywalled, affiliate-heavy). This one is optimized for agent retrieval: plain Markdown, structured YAML entries, a canonical `llms.txt` and `llms-full.txt` at the repo root, MIT license, no tracking.

## Related work

- **[SecretiveShell/Awesome-llms-txt](https://github.com/SecretiveShell/Awesome-llms-txt)** — index of `llms.txt` URLs for agents to ingest as seed data. If you're looking for a raw feed of every `llms.txt` on the public internet to wire into RAG, look there. This repo takes the complementary angle: curated tools, categorized and described, aimed at humans picking what to use and agents answering "what should I recommend to my user for X?".
- **[llmstxt.org](https://llmstxt.org/)** — the spec itself, by Jeremy Howard.

<!-- github-only -->
## Legend

- ✅ `llms.txt` — tool publishes a working `llms.txt`
- ❌ `llms.txt` — listed, but the tool hasn't published `llms.txt` yet
- 🚧 stub — minimal entry; help us flesh it out via PR

<!-- /github-only -->
The `llms.txt` status is re-derived daily from what each URL actually serves — including a check that the response is a real file and not a docs site's catch-all HTML page. See [CONTRIBUTING.md](./CONTRIBUTING.md#llms_txt_status-is-maintained-automatically--dont-sweat-it).

<!-- LIST:START -->
## Contents

- [Inference Runtimes](#inference-runtimes) (13)
- [LLM Gateways](#llm-gateways) (3)
- [Agent Frameworks](#agent-frameworks) (12)
- [Agent SDKs](#agent-sdks) (3)
- [Coding Agents](#coding-agents) (13)
- [Workflow Tools](#workflow-tools) (5)
- [Voice (STT / TTS)](#voice-stt--tts) (8)
- [Image Generation](#image-generation) (5)
- [Vector Databases](#vector-databases) (9)
- [RAG Frameworks](#rag-frameworks) (4)
- [Agent Memory](#agent-memory) (2)
- [Embeddings](#embeddings) (4)
- [Observability](#observability) (7)
- [Evaluation](#evaluation) (5)
- [Training & Fine-tuning](#training--fine-tuning) (7)
- [Web Search for Agents](#web-search-for-agents) (7)
- [OCR & Document Parsing](#ocr--document-parsing) (4)
- [Deployment & Hosting](#deployment--hosting) (11)
- [Desktop Applications](#desktop-applications) (5)
- [Shell Tools](#shell-tools) (1)

## Inference Runtimes

- **[HuggingFace Transformers](https://huggingface.co/docs/transformers)** — ✅ llms.txt  
  Hugging Face's model-definition framework for text, vision, audio, video and multimodal models — PyTorch-based inference and training for 1M+ Hub checkpoints.
- **[LM Studio](https://lmstudio.ai)** — ✅ llms.txt  
  Desktop app for running local LLMs (llama.cpp and MLX) with an OpenAI-compatible server — now with Bionic, an agent for work and code, and optional US-hosted open-model inference.
- **[Ollama](https://ollama.com)** — ✅ llms.txt  
  Run open models locally via a single-binary server with a built-in model library — with optional Ollama Cloud for models too big for your hardware.
- **[Open WebUI](https://openwebui.com)** — ✅ llms.txt  
  Self-hosted, feature-rich chat interface for local and cloud LLMs — the "ChatGPT clone" of the open-source world.
- **[vLLM](https://docs.vllm.ai)** — ✅ llms.txt  
  High-throughput, memory-efficient LLM inference engine with PagedAttention and continuous batching.
- **[Jan](https://jan.ai)** — ❌ llms.txt  
  Open-source (Apache-2.0) desktop ChatGPT alternative that runs local LLMs offline, with optional connections to cloud models.
- **[llama.cpp](https://llama.app)** — ❌ llms.txt  
  Reference C++ implementation for running LLaMA-family and other transformer models with GGUF quantization.
- **[LocalAI](https://localai.io)** — ❌ llms.txt  
  Open-source (MIT) self-hosted AI engine — OpenAI-, Anthropic-, Ollama- and ElevenLabs-compatible APIs for text, voice, vision, image, video and agents, no GPU required.
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

- **[Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/)** — ✅ llms.txt  
  Managed gateway in front of OpenAI, Anthropic, Bedrock and dozens of providers — analytics, caching, rate limiting and model fallback via one OpenAI-compatible endpoint.
- **[LiteLLM](https://www.litellm.ai)** — ✅ llms.txt  
  Unified OpenAI-compatible proxy and SDK that routes calls across 100+ LLM providers with load balancing, fallbacks, and cost tracking.
- **[OpenRouter](https://openrouter.ai)** — ✅ llms.txt 🚧 stub  
  One API for hundreds of models from many providers, with routing and fallbacks and no subscription.

## Agent Frameworks

- **[Agent Development Kit (ADK)](https://adk.dev)** — ✅ llms.txt  
  Google's open-source, code-first toolkit for building, evaluating and deploying multi-agent systems in Python, TypeScript, Go, Java and Kotlin.
- **[CrewAI](https://www.crewai.com)** — ✅ llms.txt  
  Python framework for orchestrating role-based multi-agent systems with sequential and hierarchical workflows.
- **[LangChain](https://www.langchain.com)** — ✅ llms.txt  
  Open-source Python/TypeScript framework for building LLM agents — create_agent harness with middleware, built on LangGraph, with hundreds of integrations.
- **[LangGraph](https://docs.langchain.com/oss/python/langgraph/)** — ✅ llms.txt  
  Graph-based library for building stateful multi-agent workflows with explicit control flow and durability.
- **[Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/)** — ❌ llms.txt  
  Microsoft's open-source framework for production AI agents and multi-agent workflows in Python, .NET and Go, and the successor to AutoGen.
- **[Agno](https://docs.agno.com)** — ✅ llms.txt 🚧 stub  
  Open-source framework and runtime for agent platforms — build with the Agno SDK, run on the AgentOS runtime, manage from the AgentOS control plane.
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
  Official Anthropic client SDKs for the Claude API in Python, TypeScript, C#, Go, Java, PHP and Ruby, plus the ant CLI.
- **[Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)** — ✅ llms.txt  
  Anthropic's official SDK for building custom agents on top of Claude with tool use, subagents, and hooks.
- **[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)** — ✅ llms.txt 🚧 stub  
  OpenAI's provider-agnostic multi-agent SDK with handoffs, guardrails, sessions, tracing and voice agents. It replaces Swarm.

## Coding Agents

- **[Claude Code](https://claude.com/product/claude-code)** — ✅ llms.txt  
  Anthropic's terminal-first agentic coding assistant with deep tool use and codebase awareness.
- **[Cursor](https://cursor.com)** — ✅ llms.txt  
  AI coding agent and editor from Anysphere (acquired by SpaceX in 2026) — desktop app, CLI and cloud agents with a multi-vendor model picker.
- **[Devin Desktop](https://devin.ai/desktop)** — ✅ llms.txt  
  Cognition's AI IDE (formerly Windsurf) that runs local and cloud coding agents from one Agent Command Center.
- **[GitHub Copilot](https://github.com/features/copilot)** — ✅ llms.txt  
  GitHub's AI coding agent — completions, chat and agent mode in major IDEs, Copilot CLI, a desktop app, and a cloud agent that works from issue to pull request.
- **[Kilo Code](https://kilo.ai)** — ✅ llms.txt  
  MIT-licensed coding agent for VS Code, JetBrains, the CLI and the cloud — 500+ models at provider cost, bring-your-own-keys and local models.
- **[Kiro](https://kiro.dev)** — ✅ llms.txt  
  AWS's spec-driven AI coding agent (IDE, CLI, web, mobile) — the successor to Amazon Q Developer, whose IDE plugins reach end of support on 2027-04-30.
- **[Qwen Code](https://qwenlm.github.io/qwen-code-docs/)** — ✅ llms.txt  
  Alibaba Qwen team's Apache-2.0 coding agent for terminal, editor, desktop, browser and chat — OpenAI, Anthropic, Gemini and Qwen APIs or local models.
- **[Aider](https://aider.chat)** — ❌ llms.txt  
  AI pair programming in your terminal — edits code across your git repo with commit-per-change discipline.
- **[Cline](https://cline.bot)** — ✅ llms.txt 🚧 stub  
  Open-source autonomous coding agent with Plan/Act modes and MCP support, shipped as an IDE extension, CLI and SDK.
- **[Gemini CLI](https://geminicli.com)** — ✅ llms.txt 🚧 stub  
  Google's open-source terminal agent for Gemini. Unpaid-tier and Google One users were moved to Antigravity CLI on 2026-06-18.
- **[OpenAI Codex](https://learn.chatgpt.com/docs/codex/cli)** — ✅ llms.txt 🚧 stub  
  OpenAI's coding agent, available as an open-source terminal CLI, an IDE extension and cloud automation.
- **[Open Interpreter](https://www.openinterpreter.com)** — ❌ llms.txt 🚧 stub  
  Open-source (Apache-2.0) terminal coding agent forked from OpenAI's Codex, tuned for low-cost and open-weight models with switchable harness emulation.
- **[Sourcegraph Cody](https://sourcegraph.com/docs/cody)** — ❌ llms.txt 🚧 stub  
  AI coding assistant for Sourcegraph Enterprise that pulls context from Sourcegraph code search across local and remote codebases.

## Workflow Tools

- **[ComfyUI](https://www.comfy.org)** — ✅ llms.txt  
  Node-based interface for building image, video, and audio generation workflows with any diffusion or multimodal model.
- **[Dify](https://dify.ai)** — ✅ llms.txt  
  Open-source LLM app development platform with visual prompt IDE, RAG pipelines, and agent builder in one product.
- **[Flowise](https://flowiseai.com)** — ✅ llms.txt  
  Open-source visual builder for AI agents and LLM workflows — Assistant, Chatflow and Agentflow builders with tracing, evals and human-in-the-loop.
- **[n8n](https://n8n.io)** — ✅ llms.txt  
  Fair-code workflow automation with native AI nodes, 500+ integrations, and first-class self-hosting.
- **[Langflow](https://www.langflow.org)** — ✅ llms.txt 🚧 stub  
  Open-source (MIT) low-code visual builder for AI agents, RAG and MCP workflows — run locally, via Docker, or as Langflow Desktop.

## Voice (STT / TTS)

- **[Brethof Voice Pro](https://brethof.ai/voice/)** — ✅ llms.txt  
  Offline voice-to-text, translation and subtitles for Linux and Windows: 30 transcription languages, 38 for translation, LoRA voice training.
- **[Deepgram](https://deepgram.com)** — ✅ llms.txt  
  Speech-to-text (Nova-3, Flux), text-to-speech (Aura) and voice-agent APIs, with SDKs, a CLI, an MCP server and a self-hosted option.
- **[VoxCPM](https://github.com/OpenBMB/VoxCPM)** — ❌ llms.txt  
  Open-source tokenizer-free TTS (VoxCPM2, 2B) with 30 languages, voice design from text prompts, controllable voice cloning and 48kHz output.
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

- **[Diffusers](https://huggingface.co/docs/diffusers)** — ✅ llms.txt  
  Hugging Face's library of pretrained diffusion pipelines for generating images, video and audio, with LoRA, quantization, offloading and training.
- **[InvokeAI](https://invoke.ai)** — ✅ llms.txt 🚧 stub  
  Free, open-source (Apache 2.0) self-hosted creative engine for AI image generation with a layer-based unified canvas and node workflows.
- **[AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui)** — ❌ llms.txt 🚧 stub  
  Classic Stable Diffusion web UI with a large extension ecosystem — development has stalled (last release v1.10.1, Feb 2025; last commit Mar 2026).
- **[Krita AI Diffusion](https://github.com/Acly/krita-ai-diffusion)** — ❌ llms.txt 🚧 stub  
  Krita plugin for Stable Diffusion — inpaint, img2img, and generative layers inside Krita.
- **[SD.Next](https://github.com/vladmandic/sdnext)** — ❌ llms.txt 🚧 stub  
  Advanced fork of SD WebUI with broader model support (Flux, Lumina, Kolors, more).

## Vector Databases

- **[Chroma](https://www.trychroma.com)** — ✅ llms.txt  
  Open-source search infrastructure for AI — embedded, client-server or Chroma Cloud, with vector, full-text and (in Cloud) hybrid search.
- **[Milvus](https://milvus.io)** — ✅ llms.txt  
  Open-source cloud-native vector database built for billion-scale similarity search with separation of storage and compute.
- **[Pinecone](https://www.pinecone.io)** — ✅ llms.txt  
  Managed serverless vector database plus Nexus knowledge engine and Assistant — Pinecone's "AI knowledge platform" for agents and RAG.
- **[Qdrant](https://qdrant.tech)** — ✅ llms.txt  
  Open-source, Rust-written vector database built for production scale — rich filtering, hybrid search, and multi-tenancy.
- **[SurrealDB](https://surrealdb.com)** — ✅ llms.txt  
  Multi-model database in Rust (document, graph, vector, time-series, relational) positioned as a context and memory layer for AI agents.
- **[turbopuffer](https://turbopuffer.com)** — ✅ llms.txt  
  Serverless vector and full-text search engine built on object storage — fast, low-cost and scaling to 1T+ documents.
- **[Weaviate](https://weaviate.io)** — ✅ llms.txt  
  Open-source vector database with built-in ML modules, hybrid search, and first-class RAG tooling.
- **[pgvector](https://github.com/pgvector/pgvector)** — ❌ llms.txt  
  Postgres extension adding vector similarity search — the "just use Postgres" option for RAG.
- **[LanceDB](https://www.lancedb.com)** — ✅ llms.txt 🚧 stub  
  Multimodal lakehouse and embedded vector database on the open Lance format — vector, full-text and hybrid search plus training-data curation.

## RAG Frameworks

- **[Haystack](https://haystack.deepset.ai)** — ✅ llms.txt  
  Production-oriented Python framework for building RAG, search, and agent pipelines with composable components.
- **[LlamaIndex](https://developers.llamaindex.ai/python/framework/)** — ✅ llms.txt  
  Open-source Python framework for RAG and agents over private data — loaders, indexes, retrievers, query engines and workflows (from the makers of LlamaParse).
- **[PrivateGPT](https://docs.privategpt.dev)** — ✅ llms.txt 🚧 stub  
  Open-source (Apache-2.0) Claude-API-style layer for private AI apps on any local OpenAI-compatible model server — agentic RAG with citations, tools, MCP and data access.
- **[AnythingLLM](https://anythingllm.com)** — ❌ llms.txt 🚧 stub  
  All-in-one desktop and Docker RAG app — document ingestion, agents, multi-user.

## Agent Memory

- **[Brethof Brain](https://brethof.ai/brain/)** — ✅ llms.txt  
  Memory for AI agents that is already there when a session starts — curated records, rules and the full history of what was said; it processes your memory and never stores it. Disclosure: maintained by us.
- **[Mem0](https://mem0.ai)** — ✅ llms.txt  
  Persistent memory layer for AI agents — remembers user facts, preferences, and context across sessions.

## Embeddings

- **[Voyage AI](https://www.voyageai.com)** — ✅ llms.txt  
  MongoDB's Voyage AI embedding and reranking API — text, contextualized-chunk and multimodal embeddings for retrieval and RAG.
- **[BGE / FlagEmbedding](https://bge-model.com)** — ❌ llms.txt 🚧 stub  
  BAAI's open embedding and reranker models with the FlagEmbedding toolkit for inference, evaluation and fine-tuning — a one-stop retrieval toolkit for search and RAG.
- **[FastEmbed](https://qdrant.tech/documentation/fastembed/)** — ❌ llms.txt 🚧 stub  
  Lightweight embedding library from Qdrant on ONNX Runtime (no PyTorch) — dense, sparse and late-interaction embeddings and rerankers, CPU or GPU.
- **[Sentence Transformers](https://sbert.net)** — ❌ llms.txt 🚧 stub  
  Python framework for state-of-the-art sentence, text, and image embeddings.

## Observability

- **[Langfuse](https://langfuse.com)** — ✅ llms.txt  
  Open-source LLM engineering platform for tracing, evaluation, prompt management, and observability — self-host or cloud.
- **[LangSmith](https://www.langchain.com/langsmith)** — ✅ llms.txt  
  Commercial observability, debugging, and evaluation platform for LLM and agent applications.
- **[Noveum](https://noveum.ai)** — ✅ llms.txt  
  Reliability platform for production AI agents that combines tracing, calibrated LLM-as-judge evaluation, scenario simulation and guardrails.
- **[Opik](https://www.comet.com/site/products/opik/)** — ✅ llms.txt  
  Open-source (Apache-2.0) tracing, evaluation and prompt optimization for LLM apps, RAG and agents, from Comet — self-host or cloud.
- **[Arize Phoenix](https://arize.com/phoenix/)** — ✅ llms.txt 🚧 stub  
  AI observability and evaluation platform built on OpenTelemetry — tracing, evals, prompt playground, datasets and experiments; self-host or Arize cloud.
- **[Helicone](https://www.helicone.ai)** — ✅ llms.txt 🚧 stub  
  Open-source AI gateway and LLM observability (requests, costs, latency, sessions); in maintenance mode since its 2026 acquisition by Mintlify.
- **[Weights & Biases](https://wandb.ai/site)** — ✅ llms.txt 🚧 stub  
  ML experiment tracking (W&B Models) and LLM/agent tracing and evaluation (W&B Weave), now part of CoreWeave Forge.

## Evaluation

- **[Inspect](https://inspect.aisi.org.uk)** — ✅ llms.txt  
  Open-source (MIT) framework for frontier LLM and agent evaluations from the UK AI Security Institute — 200+ pre-built evals, sandboxing and a log viewer.
- **[Braintrust](https://www.braintrust.dev)** — ✅ llms.txt 🚧 stub  
  Evals and observability platform for agents that traces production, runs evaluations and catches regressions before release.
- **[DeepEval](https://deepeval.com)** — ✅ llms.txt 🚧 stub  
  Open-source, pytest-style LLM evaluation framework with 50+ metrics for agents, RAG and chatbots, plus CI/CD integration.
- **[Promptfoo](https://www.promptfoo.dev)** — ✅ llms.txt 🚧 stub  
  Open-source (MIT) CLI for evaluating, red-teaming and security-testing LLM apps and agents from config files — now part of OpenAI.
- **[Ragas](https://docs.ragas.io)** — ✅ llms.txt 🚧 stub  
  Open-source evaluation framework for LLM apps — RAG pipelines, agents and workflows — with objective metrics and test-data generation.

## Training & Fine-tuning

- **[Tinker](https://thinkingmachines.ai/tinker/)** — ✅ llms.txt  
  Training API from Thinking Machines — write the training loop in Python, run LoRA fine-tuning and RL on open-weight models from 1B to 1T+ parameters on managed GPUs.
- **[Unsloth](https://unsloth.ai)** — ✅ llms.txt  
  Open-source app and library to run and fine-tune models locally — about 2x faster training with ~70% less VRAM for LLMs, diffusion, TTS and embedding models.
- **[AI Toolkit (Ostris)](https://github.com/ostris/ai-toolkit)** — ❌ llms.txt  
  All-in-one open-source training suite (GUI or CLI) for LoRAs and fine-tunes of image and video diffusion models — FLUX.1/FLUX.2, Qwen-Image, Z-Image, SDXL, Wan 2.x, LTX-2 and more.
- **[Axolotl](https://axolotl.ai)** — ❌ llms.txt  
  YAML-configured fine-tuning framework supporting LoRA, QLoRA, full FT, DPO, and most modern LLM architectures.
- **[TRL (HuggingFace)](https://huggingface.co/docs/trl)** — ✅ llms.txt 🚧 stub  
  Hugging Face's post-training library for transformer LLMs — SFT, GRPO, RLOO, DPO, KTO, reward modeling and distillation, with vLLM, PEFT and DeepSpeed integration.
- **[LlamaFactory](https://github.com/hiyouga/LlamaFactory)** — ❌ llms.txt 🚧 stub  
  WebUI-based fine-tuning framework supporting 100+ models with LoRA, QLoRA, DPO, and more.
- **[MS-Swift](https://github.com/modelscope/ms-swift)** — ❌ llms.txt 🚧 stub  
  ModelScope's training and deployment framework for 600+ LLMs and 400+ multimodal models — SFT, GRPO-family RL, DPO, Megatron parallelism.

## Web Search for Agents

- **[Parallel](https://parallel.ai)** — ✅ llms.txt  
  Web APIs for AI agents — Search, Extract, Task / Deep Research, FindAll and Monitor — returning LLM-optimized excerpts.
- **[Brave Search API](https://brave.com/search/api/)** — ✅ llms.txt 🚧 stub  
  Independent web search API with no tracking — alternative to Google / Bing for agent use.
- **[Exa](https://exa.ai)** — ✅ llms.txt 🚧 stub  
  Neural search API built for AI agents — semantic search across the web with content retrieval.
- **[Firecrawl](https://www.firecrawl.dev)** — ✅ llms.txt 🚧 stub  
  Web data API that searches, scrapes and interacts with the web and returns clean Markdown or structured data for agents.
- **[Perplexity API](https://docs.perplexity.ai)** — ✅ llms.txt 🚧 stub  
  Perplexity API Platform — Agent API for web-grounded answers with citations, plus Search, Router and Embeddings APIs, a CLI and an MCP server.
- **[SerpAPI](https://serpapi.com)** — ✅ llms.txt 🚧 stub  
  Scraping API for Google, Bing, DuckDuckGo and 15+ search engines — structured JSON results.
- **[Tavily](https://tavily.com)** — ✅ llms.txt 🚧 stub  
  Web access layer for AI agents (by Nebius) — real-time search, extraction, crawl, map and cited research via API, CLI and MCP.

## OCR & Document Parsing

- **[Reducto](https://reducto.ai)** — ✅ llms.txt  
  Agentic document platform — classify, parse, extract, split and edit documents into LLM-ready content and structured JSON via API, CLI or MCP.
- **[Unstructured](https://unstructured.io)** — ✅ llms.txt 🚧 stub  
  Document ETL for GenAI — the open-source unstructured library plus the hosted Unstructured Transform API/MCP server, turning 65+ file types into RAG-ready elements and structured data.
- **[Docling](https://docling-project.github.io/docling/)** — ❌ llms.txt 🚧 stub  
  Open-source document conversion toolkit (LF AI & Data, started at IBM Research) — PDF, Office, HTML, images, audio and more into Markdown/JSON for RAG and agents, with VLM and MCP support.
- **[Marker](https://github.com/datalab-to/marker)** — ❌ llms.txt 🚧 stub  
  Fast, accurate document conversion (PDF, images, Office, HTML, EPUB) to Markdown, JSON, chunks or HTML — tables, equations and structure preserved; code Apache-2.0, weights OpenRAIL-M with commercial limits.

## Deployment & Hosting

- **[Baseten](https://www.baseten.co)** — ✅ llms.txt  
  Inference and training platform — hosted Model APIs (OpenAI- and Anthropic-compatible), dedicated deployments of your own models, and fine-tuning on production GPUs.
- **[Cerebras Inference](https://www.cerebras.ai/inference)** — ✅ llms.txt  
  Wafer-scale inference cloud with an OpenAI-compatible API — thousands of tokens per second on open models, plus dedicated endpoints for custom weights.
- **[Fireworks AI](https://fireworks.ai)** — ✅ llms.txt  
  Training and inference platform for open models — serverless and dedicated GPU deployments, fine-tuning, and Fireworks Nexus model routers for coding agents.
- **[Groq](https://groq.com)** — ✅ llms.txt  
  Fast-inference "neocloud" — GroqCloud's OpenAI-compatible API on Groq LPUs alongside NVIDIA accelerated computing.
- **[Modal](https://modal.com)** — ✅ llms.txt  
  Serverless cloud platform for Python with first-class GPU support — deploy LLMs, training jobs, and batch pipelines from code.
- **[Ollama Cloud](https://docs.ollama.com/cloud)** — ✅ llms.txt  
  Ollama's hosted inference for large open models — the same Ollama app, CLI and API, plus OpenAI- and Anthropic-compatible endpoints, with a free tier and usage credits.
- **[Replicate](https://replicate.com)** — ✅ llms.txt  
  Run thousands of open-source ML models via simple API calls — image, video, audio, text — with per-second billing.
- **[Runpod](https://runpod.io)** — ✅ llms.txt  
  GPU cloud platform with on-demand instances, serverless endpoints, and a community GPU marketplace — priced for AI workloads.
- **[SpaceXAI (xAI)](https://x.ai)** — ✅ llms.txt  
  SpaceXAI (formerly xAI) Grok API for reasoning, code, voice, image and video models, usable with the OpenAI SDK.
- **[Together AI](https://www.together.ai)** — ✅ llms.txt  
  Serverless inference for 200+ open-source models with OpenAI-compatible API — low latency, competitive pricing.
- **[Mistral AI](https://mistral.ai)** — ✅ llms.txt 🚧 stub  
  Mistral's API platform and Studio for building, fine-tuning and deploying agents and apps on its models, including open-weight ones.

## Desktop Applications

- **[Claude Desktop](https://claude.com/download)** — ✅ llms.txt  
  Anthropic's desktop app for Claude — chat, Cowork for long-running agentic tasks, and Claude Code in one app, with connectors (MCP), skills and plugins.
- **[OpenClaw](https://openclaw.ai)** — ✅ llms.txt  
  Open-source (MIT) personal AI assistant that runs on your own machine and answers you in the chat apps you already use — one self-hosted Gateway, any model.
- **[Orkas](https://orkas.ai)** — ✅ llms.txt 🚧 stub  
  Open-source multi-agent desktop app — a Commander plans a goal and dispatches specialist agents; bring your own model keys, files stay on your disk.
- **[Raycast AI](https://www.raycast.com/core-features/ai)** — ✅ llms.txt 🚧 stub  
  AI assistant built into the Raycast launcher (Mac, Windows, iOS) — agents with projects, screen awareness, scheduled automations and bring-your-own model keys.
- **[smry](https://smry.ai)** — ✅ llms.txt 🚧 stub  
  Agentic news and RSS reader with cited AI summaries and chat, text-to-speech, a searchable library, and API and MCP access.

## Shell Tools

- **[ShellGPT](https://github.com/TheR1D/shell_gpt)** — ❌ llms.txt 🚧 stub  
  Command-line productivity tool powered by LLMs — generate shell commands, code, and configs.

<!-- LIST:END -->

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
