# AI Social Media Agent (Agentic Workflow – Mock-Based)

## Overview

This project implements a **modular AI Social Media Agent** designed to automate the end-to-end workflow of social media content creation **with human-in-the-loop control**.

Instead of focusing only on AI text generation, the project emphasizes **agent architecture**, **workflow orchestration**, **approval gates**, and **persistent memory**—the core building blocks of production-grade AI systems.

The system currently uses a **mock AI generator** to keep development independent of external APIs. Any LLM (OpenAI, Claude, Mistral, Gemini, etc.) can be plugged in later without changing the agent logic.

---

## Key Features

* **Agent-based architecture**

  * Planner → Generator → Reviewer → Memory
* **Human-in-the-loop approval**

  * Generated content must be explicitly approved before being stored or published
* **Persistent memory**

  * Approved posts are saved to disk to simulate long-term agent memory
* **Clean separation of concerns**

  * Each agent role is isolated in its own module
* **LLM-agnostic design**

  * Mock generator today, real LLM tomorrow

---

## Project Architecture

```
ai-social-media-agent/
│
├── agent/
│   ├── planner.py      # Decides what topic to post about
│   ├── generator.py    # Generates post content (mock AI)
│   ├── reviewer.py     # Human approval gate
│
├── memory/
│   ├── store.py        # Persistent memory storage
│   └── memory.txt      # Saved approved posts (runtime data)
│
├── main.py             # Orchestrates the agent workflow
├── README.md
└── .gitignore
```

---

## How the Agent Works (Workflow)

1. **Planner Agent**

   * Selects a topic for the post

2. **Generator Agent**

   * Produces social media content (currently mock-generated)

3. **Reviewer (Human-in-the-Loop)**

   * User approves or rejects the post

4. **Memory Module**

   * Approved posts are stored as persistent memory

This mirrors how real-world AI systems enforce **control, safety, and accountability**.

---

## Example Output

```
🚀 Daily AI Insight

Topic: AI agents for beginners

Agents help automate workflows
while keeping humans in the loop.

#AI #Agents
```

---

## Why Mock AI?

This project intentionally uses mock data to:

* Avoid dependency on paid APIs during development
* Focus on **agent design**, not vendor-specific SDKs
* Enable easy swapping of LLM providers later

Replacing the mock generator with a real LLM requires changing **only one file**.

---

## Tech Stack

* Python 3
* Modular agent-based design
* Command-line human approval
* Git & GitHub for version control

---

## What This Project Demonstrates

From a hiring perspective, this project shows:

* Understanding of **agentic AI systems**
* Human-in-the-loop safety design
* Clean software architecture
* Practical automation thinking
* Ability to build AI systems beyond prompt engineering

---

## Future Enhancements

Planned or possible extensions:

* Plug in a real LLM (OpenAI, Mistral, Claude)
* Automated scheduling (cron-based posting)
* Rule-based or AI-based content review
* Topic de-duplication using memory
* Multi-platform posting simulation
* Analytics & feedback loop

---

## How to Run

```bash
python main.py
```

Follow the prompt to approve or reject generated posts.

---
## Memory-Aware Planning

The planner agent reads past approved topics from persistent memory
and avoids repeating them in future runs.

This demonstrates stateful agent behavior and adaptive decision-making
without relying on external AI services.


## Author

**Priyanka Wandhare**
AI / Agent Systems | Product-minded Engineer

