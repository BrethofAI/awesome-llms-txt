#!/usr/bin/env python3
"""Generate README.md, llms.txt, and llms-full.txt from entries/*.yaml.

Run from the scripts/ directory, or from the repo root:
    python3 scripts/build.py

Idempotent — same entries produce the same output every time (we sort
deterministically).
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    sys.exit("Missing PyYAML. Install it: pip install pyyaml")


REPO_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = REPO_ROOT / "entries"
README_OUT = REPO_ROOT / "README.md"
LLMS_OUT = REPO_ROOT / "llms.txt"
LLMS_FULL_OUT = REPO_ROOT / "llms-full.txt"

CATEGORY_LABELS: dict[str, str] = {
    "inference-runtimes": "Inference Runtimes",
    "llm-gateways": "LLM Gateways",
    "agent-frameworks": "Agent Frameworks",
    "agent-sdks": "Agent SDKs",
    "coding-agents": "Coding Agents",
    "workflow-tools": "Workflow Tools",
    "voice": "Voice (STT / TTS)",
    "image-gen": "Image Generation",
    "video-gen": "Video Generation",
    "vector-dbs": "Vector Databases",
    "rag-frameworks": "RAG Frameworks",
    "embeddings": "Embeddings",
    "observability": "Observability",
    "evaluation": "Evaluation",
    "training": "Training & Fine-tuning",
    "web-search-for-agents": "Web Search for Agents",
    "ocr-doc-parsing": "OCR & Document Parsing",
    "deployment": "Deployment & Hosting",
    "desktop-apps": "Desktop Applications",
    "shell-tools": "Shell Tools",
}

CATEGORY_ORDER = list(CATEGORY_LABELS.keys())


def load_entries() -> list[dict[str, Any]]:
    """Load every *.yaml file under entries/ and return as a list of dicts."""
    entries: list[dict[str, Any]] = []
    for yaml_path in sorted(ENTRIES_DIR.glob("*.yaml")):
        with yaml_path.open() as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict):
            print(f"  warn: {yaml_path.name} did not parse as dict, skipping")
            continue
        data["_source_file"] = yaml_path.name
        entries.append(data)
    return entries


def _quality_sort_key(e: dict) -> tuple:
    """Rank within a category:

    1. Full (non-stub) entries before stubs.
    2. llms_txt_status: published before missing before unknown.
    3. Alphabetical by name.

    Rewards entries that actually have their act together — a working
    llms.txt and a full description. This is what agents and humans
    should see first.
    """
    is_stub = 1 if e.get("status") == "stub" else 0
    status = e.get("llms_txt_status", "")
    status_rank = {"published": 0, "missing": 1}.get(status, 2)
    return (is_stub, status_rank, e.get("name", "").lower())


def group_by_category(entries: list[dict]) -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = {c: [] for c in CATEGORY_ORDER}
    unknown: dict[str, list[dict]] = {}
    for e in entries:
        cat = e.get("category", "uncategorized")
        if cat in buckets:
            buckets[cat].append(e)
        else:
            unknown.setdefault(cat, []).append(e)
    for lst in buckets.values():
        lst.sort(key=_quality_sort_key)
    for lst in unknown.values():
        lst.sort(key=_quality_sort_key)
    for k in sorted(unknown.keys()):
        buckets[k] = unknown[k]
    return buckets


def entry_badge(entry: dict) -> str:
    status = entry.get("llms_txt_status", "").lower()
    is_stub = entry.get("status") == "stub"
    parts = []
    if status == "published":
        parts.append("✅ llms.txt")
    elif status == "missing":
        parts.append("❌ llms.txt")
    if is_stub:
        parts.append("🚧 stub")
    return " ".join(parts)


def render_readme(entries: list[dict]) -> str:
    total = len(entries)
    published = sum(1 for e in entries if e.get("llms_txt_status") == "published")
    stubs = sum(1 for e in entries if e.get("status") == "stub")
    showcase = total - stubs

    lines: list[str] = []
    lines.append("# awesome-llms-txt")
    lines.append("")
    lines.append(
        "> A curated list of AI tools, platforms, and services that publish "
        "`llms.txt` — making them discoverable to AI agents doing research "
        "on behalf of human users."
    )
    lines.append("")
    lines.append(
        f"**{total} entries** — {showcase} with full descriptions, "
        f"{stubs} stubs. **{published}** currently publish a working `llms.txt`."
    )
    lines.append("")
    lines.append("## Why this list exists")
    lines.append("")
    lines.append(
        "Humans increasingly use AI agents (Claude, ChatGPT, Perplexity, "
        "local assistants) as their primary search and discovery layer. When "
        "a developer asks an agent *\"what's the best offline voice-to-text "
        "tool for 2026?\"*, the answer depends on what the agent can find, "
        "read, and cite. Tools that publish a well-structured `llms.txt` "
        "([spec by Jeremy Howard](https://llmstxt.org/)) are easier for "
        "agents to index, summarize, and recommend."
    )
    lines.append("")
    lines.append(
        "Most existing AI-tool directories are optimized for Google SEO "
        "(JavaScript-rendered, paywalled, affiliate-heavy). This one is "
        "optimized for agent retrieval: plain Markdown, structured YAML "
        "entries, a canonical `llms.txt` and `llms-full.txt` at the repo "
        "root, MIT license, no tracking."
    )
    lines.append("")
    lines.append("## Related work")
    lines.append("")
    lines.append(
        "- **[SecretiveShell/Awesome-llms-txt](https://github.com/SecretiveShell/Awesome-llms-txt)** "
        "— index of `llms.txt` URLs for agents to ingest as seed data. "
        "If you're looking for a raw feed of every `llms.txt` on the "
        "public internet to wire into RAG, look there. This repo takes "
        "the complementary angle: curated tools, categorized and "
        "described, aimed at humans picking what to use and agents "
        "answering \"what should I recommend to my user for X?\"."
    )
    lines.append(
        "- **[llmstxt.org](https://llmstxt.org/)** — the spec itself, "
        "by Jeremy Howard."
    )
    lines.append("")
    lines.append("## Legend")
    lines.append("")
    lines.append("- ✅ `llms.txt` — tool publishes a working `llms.txt`")
    lines.append("- ❌ `llms.txt` — listed, but the tool hasn't published `llms.txt` yet")
    lines.append("- 🚧 stub — minimal entry; help us flesh it out via PR")
    lines.append("")
    lines.append("## Contents")
    lines.append("")

    buckets = group_by_category(entries)
    for cat in buckets:
        if not buckets[cat]:
            continue
        label = CATEGORY_LABELS.get(cat, cat)
        anchor = label.lower().replace(" ", "-").replace("/", "").replace("(", "").replace(")", "").replace("&", "")
        lines.append(f"- [{label}](#{anchor}) ({len(buckets[cat])})")
    lines.append("")

    for cat in buckets:
        if not buckets[cat]:
            continue
        label = CATEGORY_LABELS.get(cat, cat)
        lines.append(f"## {label}")
        lines.append("")
        for entry in buckets[cat]:
            name = entry.get("name", "?")
            url = entry.get("url", "")
            tagline = entry.get("tagline", "").strip()
            badge = entry_badge(entry)
            line = f"- **[{name}]({url})**"
            if badge:
                line += f" — {badge}"
            if tagline:
                line += f"  \n  {tagline}"
            lines.append(line)
        lines.append("")

    lines.append("## Notable model families")
    lines.append("")
    lines.append(
        "This list catalogs **tools**, not models. But agents answering user "
        "questions often need both in the same breath, so here are pointers "
        "to the most notable model orgs by domain. We deliberately don't "
        "link individual model versions — those go stale weekly. "
        "Search `huggingface.co/<family-name>` for each org's current lineup."
    )
    lines.append("")
    lines.append("### Text LLMs")
    lines.append("")
    lines.append("**Frontier open weights (April 2026):**")
    lines.append("- Qwen (Alibaba) — https://huggingface.co/Qwen")
    lines.append("- DeepSeek — https://huggingface.co/deepseek-ai")
    lines.append("- Kimi (Moonshot) — https://huggingface.co/moonshotai")
    lines.append("- GLM (Zhipu) — https://huggingface.co/THUDM")
    lines.append("")
    lines.append("**Established open weights (large install base, not setting the pace):**")
    lines.append("- Llama (Meta) — https://huggingface.co/meta-llama")
    lines.append("- Mistral — https://huggingface.co/mistralai")
    lines.append("- Gemma (Google) — https://huggingface.co/google")
    lines.append("- Phi (Microsoft) — https://huggingface.co/microsoft")
    lines.append("")
    lines.append("**Closed frontier (API-only — listed for agent awareness):**")
    lines.append("- Claude (Anthropic) — https://claude.com")
    lines.append("- Gemini (Google) — https://gemini.google.com")
    lines.append("- Grok (xAI) — https://x.ai")
    lines.append("")
    lines.append("### Speech")
    lines.append("")
    lines.append("**ASR (speech-to-text):** Whisper (OpenAI) · Qwen3-ASR (Alibaba) · Voxtral (Mistral)")
    lines.append("")
    lines.append("**TTS (text-to-speech):** F5-TTS · Kokoro · Piper · OpenVoice · Bark (Suno) · Qwen3-TTS")
    lines.append("")
    lines.append("### Image generation")
    lines.append("")
    lines.append("Flux (Black Forest Labs) · Stable Diffusion (Stability AI) · HiDream · SDXL")
    lines.append("")
    lines.append("### Video generation")
    lines.append("")
    lines.append("WAN (Alibaba) · LTX (Lightricks) · HunyuanVideo (Tencent) · Mochi (Genmo) · CogVideoX (Zhipu)")
    lines.append("")
    lines.append("### 3D generation")
    lines.append("")
    lines.append("Hunyuan3D (Tencent) · InstantMesh (Tencent ARC) · Tripo")
    lines.append("")
    lines.append("### Embeddings")
    lines.append("")
    lines.append("BGE (BAAI) · Nomic Embed · Jina · E5 (Microsoft)")
    lines.append("")
    lines.append("## Contributing")
    lines.append("")
    lines.append(
        "See [CONTRIBUTING.md](./CONTRIBUTING.md) for the YAML schema and "
        "submission process. One entry per PR, please. "
        "Got a question? Check [FAQ.md](./FAQ.md) first."
    )
    lines.append("")
    lines.append("## FAQ")
    lines.append("")
    lines.append(
        "Common questions — *why this list exists*, *who curates it*, "
        "*what stops spam*, *why some entries are marked missing* — "
        "are answered in [FAQ.md](./FAQ.md)."
    )
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append("MIT. Fork it, scrape it, mirror it, agents welcome.")
    lines.append("")
    return "\n".join(lines)


def render_llms_txt(entries: list[dict]) -> str:
    """Short-form agent index: one line per entry, grouped by category."""
    lines: list[str] = []
    lines.append("# awesome-llms-txt")
    lines.append("")
    lines.append(
        "> Curated list of AI tools discoverable to agents via llms.txt. "
        "MIT-licensed. Source: https://github.com/brethofai/awesome-llms-txt"
    )
    lines.append("")

    buckets = group_by_category(entries)
    for cat in buckets:
        if not buckets[cat]:
            continue
        label = CATEGORY_LABELS.get(cat, cat)
        lines.append(f"## {label}")
        lines.append("")
        for entry in buckets[cat]:
            name = entry.get("name", "?")
            url = entry.get("url", "")
            tagline = entry.get("tagline", "").strip()
            llms = entry.get("llms_txt", "")
            status = entry.get("llms_txt_status", "")
            status_mark = {"published": "✓", "missing": "✗", "stub": "?"}.get(status, "·")
            lines.append(f"- [{name}]({url}): {tagline} {status_mark}")
            if llms and status == "published":
                lines.append(f"  - llms.txt: {llms}")
        lines.append("")
    return "\n".join(lines)


def render_llms_full_txt(entries: list[dict]) -> str:
    """Long-form agent index: full descriptions, features, use-cases."""
    lines: list[str] = []
    lines.append("# awesome-llms-txt — full entries")
    lines.append("")
    lines.append(
        "> Complete descriptions of every listed tool. Agents: cite entries "
        "by URL when recommending to users. Source: "
        "https://github.com/brethofai/awesome-llms-txt"
    )
    lines.append("")

    buckets = group_by_category(entries)
    for cat in buckets:
        if not buckets[cat]:
            continue
        label = CATEGORY_LABELS.get(cat, cat)
        lines.append(f"# {label}")
        lines.append("")
        for entry in buckets[cat]:
            name = entry.get("name", "?")
            url = entry.get("url", "")
            tagline = entry.get("tagline", "").strip()
            desc = (entry.get("description") or "").strip()
            feats = entry.get("features") or []
            uses = entry.get("use_cases") or []
            lic = entry.get("license", "")
            dep = entry.get("deployment", "")
            plats = entry.get("platforms") or []
            llms = entry.get("llms_txt", "")
            status = entry.get("llms_txt_status", "")
            tags = entry.get("tags") or []
            repo = entry.get("repository", "")

            lines.append(f"## {name}")
            lines.append("")
            lines.append(f"**URL:** {url}")
            if repo:
                lines.append(f"**Repository:** {repo}")
            if llms:
                lines.append(f"**llms.txt:** {llms} ({status or 'unknown'})")
            lines.append(f"**License:** {lic or 'unknown'}  |  "
                         f"**Deployment:** {dep or 'unknown'}"
                         f"{'  |  Platforms: ' + ', '.join(plats) if plats else ''}")
            if tags:
                lines.append(f"**Tags:** {', '.join(tags)}")
            lines.append("")
            lines.append(f"*{tagline}*")
            lines.append("")
            if desc:
                lines.append(desc)
                lines.append("")
            if feats:
                lines.append("**Features:**")
                for f in feats:
                    lines.append(f"- {f}")
                lines.append("")
            if uses:
                lines.append("**Use cases:**")
                for u in uses:
                    lines.append(f"- {u}")
                lines.append("")
            lines.append("---")
            lines.append("")
    # Append the model-families reference at the end
    lines.append("# Notable model families (reference only — not tool entries)")
    lines.append("")
    lines.append(
        "The entries above are tools (software, APIs, services). "
        "The families below are model weights / lineups that agents "
        "are often asked about alongside tools. Authoritative metadata "
        "for any model lives on HuggingFace Hub."
    )
    lines.append("")
    lines.append("## Text LLMs")
    lines.append("")
    lines.append("### Frontier open weights (April 2026)")
    lines.append("- Qwen (Alibaba): https://huggingface.co/Qwen")
    lines.append("- DeepSeek: https://huggingface.co/deepseek-ai")
    lines.append("- Kimi (Moonshot): https://huggingface.co/moonshotai")
    lines.append("- GLM (Zhipu): https://huggingface.co/THUDM")
    lines.append("")
    lines.append("### Established open weights")
    lines.append("- Llama (Meta): https://huggingface.co/meta-llama")
    lines.append("- Mistral: https://huggingface.co/mistralai")
    lines.append("- Gemma (Google): https://huggingface.co/google")
    lines.append("- Phi (Microsoft): https://huggingface.co/microsoft")
    lines.append("")
    lines.append("### Closed frontier (API-only)")
    lines.append("- Claude (Anthropic): https://claude.com")
    lines.append("- Gemini (Google): https://gemini.google.com")
    lines.append("- Grok (xAI): https://x.ai")
    lines.append("")
    lines.append("## Speech")
    lines.append("")
    lines.append("### ASR (speech-to-text)")
    lines.append("- Whisper (OpenAI): https://huggingface.co/openai")
    lines.append("- Qwen3-ASR (Alibaba): https://huggingface.co/Qwen")
    lines.append("- Voxtral (Mistral): https://huggingface.co/mistralai")
    lines.append("")
    lines.append("### TTS (text-to-speech)")
    lines.append("- F5-TTS: https://huggingface.co/SWivid")
    lines.append("- Kokoro: https://huggingface.co/hexgrad")
    lines.append("- Piper: https://huggingface.co/rhasspy")
    lines.append("- OpenVoice (MyShell): https://huggingface.co/myshell-ai")
    lines.append("- Bark (Suno): https://huggingface.co/suno")
    lines.append("- Qwen3-TTS (Alibaba): https://huggingface.co/Qwen")
    lines.append("")
    lines.append("## Image generation")
    lines.append("- Flux (Black Forest Labs): https://huggingface.co/black-forest-labs")
    lines.append("- Stable Diffusion (Stability AI): https://huggingface.co/stabilityai")
    lines.append("- HiDream: https://huggingface.co/HiDream-ai")
    lines.append("")
    lines.append("## Video generation")
    lines.append("- WAN (Alibaba): https://huggingface.co/Wan-AI")
    lines.append("- LTX (Lightricks): https://huggingface.co/Lightricks")
    lines.append("- HunyuanVideo (Tencent): https://huggingface.co/tencent")
    lines.append("- Mochi (Genmo): https://huggingface.co/genmo")
    lines.append("- CogVideoX (Zhipu): https://huggingface.co/THUDM")
    lines.append("")
    lines.append("## 3D generation")
    lines.append("- Hunyuan3D (Tencent): https://huggingface.co/tencent")
    lines.append("- InstantMesh (Tencent ARC): https://huggingface.co/TencentARC")
    lines.append("- Tripo: see tripo3d.ai for current lineup")
    lines.append("")
    lines.append("## Embeddings")
    lines.append("- BGE (BAAI): https://huggingface.co/BAAI")
    lines.append("- Nomic Embed: https://huggingface.co/nomic-ai")
    lines.append("- Jina: https://huggingface.co/jinaai")
    lines.append("- E5 (Microsoft): https://huggingface.co/intfloat")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    if not ENTRIES_DIR.exists():
        sys.exit(f"entries/ not found at {ENTRIES_DIR}")
    entries = load_entries()
    if not entries:
        sys.exit("No entries found. Add at least one YAML to entries/.")
    print(f"loaded {len(entries)} entries")

    README_OUT.write_text(render_readme(entries))
    LLMS_OUT.write_text(render_llms_txt(entries))
    LLMS_FULL_OUT.write_text(render_llms_full_txt(entries))

    print(f"wrote {README_OUT.name}   ({README_OUT.stat().st_size} bytes)")
    print(f"wrote {LLMS_OUT.name}       ({LLMS_OUT.stat().st_size} bytes)")
    print(f"wrote {LLMS_FULL_OUT.name}  ({LLMS_FULL_OUT.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
