#!/usr/bin/env python3
"""
Script to update the README with chapter completion status.
Run this script whenever you complete a chapter.
"""

import re
from pathlib import Path

# Configuration
CHAPTERS = [
    {
        "num": 0,
        "title": "Simple Chat Model: Hello World",
        "notebook": "ch0_hello_world.ipynb",
        "description": "Your first LLM interaction - calling a chat model, understanding tokens, and basic parameters"
    },
    {
        "num": 1,
        "title": "Intro + Environment & Tools",
        "notebook": "ch1_intro_setup.ipynb",
        "description": "Course overview, setup Python environment, API keys, and repository walkthrough"
    },
    {
        "num": 2,
        "title": "LLM Parameters & Internals",
        "notebook": "ch2_llm_parameters.ipynb",
        "description": "Context windows, temperature, max_tokens, streaming, and cost optimization"
    },
    {
        "num": 3,
        "title": "Prompting 101 — Basics",
        "notebook": "ch3_prompting_basics.ipynb",
        "description": "Roles (system/user/assistant), prompt framing, and instruction clarity"
    },
    {
        "num": 4,
        "title": "Prompt Engineering & Patterns",
        "notebook": "ch4_prompt_engineering.ipynb",
        "description": "Few-shot learning, chain-of-thought, role-playing, and advanced patterns"
    },
    {
        "num": 5,
        "title": "Structured Output & Parsers",
        "notebook": "ch5_structured_output.ipynb",
        "description": "JSON/CSV/YAML output, validation, schema enforcement"
    },
    {
        "num": 6,
        "title": "RAG: Retrieval-Augmented Generation — Concepts",
        "notebook": "ch6_rag_concepts.ipynb",
        "description": "Embeddings, vector databases (FAISS/Pinecone), chunking strategies"
    },
    {
        "num": 7,
        "title": "RAG — Production Considerations",
        "notebook": "ch7_rag_production.ipynb",
        "description": "Vector maintenance, hybrid search, performance optimization"
    },
    {
        "num": 8,
        "title": "Agents Fundamentals",
        "notebook": "ch8_agents_basics.ipynb",
        "description": "When to use agents, tools vs chains, memory management"
    },
    {
        "num": 9,
        "title": "Advanced Agents & Orchestration",
        "notebook": "ch9_advanced_agents.ipynb",
        "description": "Multi-step planners, custom tools, LangGraph integration"
    },
    {
        "num": 10,
        "title": "Open-source & Local LLMs",
        "notebook": "ch10_local_llms.ipynb",
        "description": "Running Llama locally, quantization, cloud/local hybrid systems"
    },
    {
        "num": 11,
        "title": "Testing, Monitoring, MLOps for LLMs",
        "notebook": "ch11_mlops.ipynb",
        "description": "Unit tests, evaluation metrics, monitoring, cost dashboards"
    },
    {
        "num": 12,
        "title": "Security, Ethics, Safety",
        "notebook": "ch12_security_ethics.ipynb",
        "description": "Hallucination mitigation, PII handling, guardrails, red-teaming"
    },
    {
        "num": 13,
        "title": "Capstone Project",
        "notebook": "ch13_capstone.ipynb",
        "description": "Build a full RAG-powered assistant with agents and web UI"
    },
]


def check_notebook_exists(notebook_name: str) -> bool:
    """Check if a notebook file exists."""
    notebook_path = Path("notebooks") / notebook_name
    return notebook_path.exists()


def get_chapter_status(chapter: dict) -> tuple[str, str]:
    """Determine the status of a chapter."""
    if check_notebook_exists(chapter["notebook"]):
        return "✅ Complete", f"[{chapter['notebook']}](notebooks/{chapter['notebook']})"
    else:
        return "🚧 In Progress" if chapter["num"] == 1 else "🔜 Planned", "Coming Soon"


def calculate_progress() -> tuple[int, int]:
    """Calculate the number of completed chapters."""
    completed = sum(1 for ch in CHAPTERS if check_notebook_exists(ch["notebook"]))
    total = len(CHAPTERS)
    return completed, total


def generate_table() -> str:
    """Generate the chapter table markdown."""
    table = "| # | Chapter | Status | Notebook | Videos | Description |\n"
    table += "|---|---------|--------|----------|--------|-------------|\n"
    
    for chapter in CHAPTERS:
        status, notebook_link = get_chapter_status(chapter)
        videos = "🎥 Coming Soon" if status == "✅ Complete" else "🔜"
        
        table += f"| {chapter['num']} | **{chapter['title']}** | {status} | {notebook_link} | {videos} | {chapter['description']} |\n"
    
    return table


def update_readme():
    """Update the README.md file with current progress."""
    readme_path = Path("README.md")
    
    if not readme_path.exists():
        print("❌ README.md not found!")
        return
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Calculate progress
    completed, total = calculate_progress()
    progress_percent = int((completed / total) * 100)
    
    # Update progress badges
    content = re.sub(
        r'!\[Progress\]\(https://img\.shields\.io/badge/Chapters%20Complete-\d+%2F\d+-blue\)',
        f'![Progress](https://img.shields.io/badge/Chapters%20Complete-{completed}%2F{total}-blue)',
        content
    )
    
    content = re.sub(
        r'!\[Progress\]\(https://progress-bar\.dev/\d+/\?title=Course%20Progress\)',
        f'![Progress](https://progress-bar.dev/{progress_percent}/?title=Course%20Progress)',
        content
    )
    
    # Update chapter table
    new_table = generate_table()
    
    # Find and replace the table
    table_pattern = r'\| # \| Chapter \| Status.*?\n(?:\|.*?\n)+'
    content = re.sub(table_pattern, new_table, content, flags=re.DOTALL)
    
    # Write back
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ README updated successfully!")
    print(f"📊 Progress: {completed}/{total} chapters complete ({progress_percent}%)")
    
    # List completed chapters
    completed_chapters = [ch for ch in CHAPTERS if check_notebook_exists(ch["notebook"])]
    if completed_chapters:
        print("\n✅ Completed chapters:")
        for ch in completed_chapters:
            print(f"   - Chapter {ch['num']}: {ch['title']}")
    
    # List pending chapters
    pending_chapters = [ch for ch in CHAPTERS if not check_notebook_exists(ch["notebook"])]
    if pending_chapters:
        print(f"\n🚧 Remaining chapters ({len(pending_chapters)}):")
        for ch in pending_chapters[:3]:  # Show next 3
            print(f"   - Chapter {ch['num']}: {ch['title']}")
        if len(pending_chapters) > 3:
            print(f"   ... and {len(pending_chapters) - 3} more")


if __name__ == "__main__":
    print("🔄 Updating README with current progress...\n")
    update_readme()
    print("\n✨ Done!")

