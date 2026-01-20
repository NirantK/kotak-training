# Day 2: From Prototype to Production

**AI Product Accelerator - Day 2**

---

## Opening

### Kickoff (5 min)

**Yesterday you built it. Today you ship it.**

Day 1: "Does the prompt work?"
Day 2: "Should we build this? How? When?"

---

## Schedule Overview

| Time | Module | Content |
|------|--------|---------|
| 10:05-11:45 | Module 1: Agent Design | Prioritization + Patterns + Failure Modes |
| 1:30-2:30 | Module 2: Agent Infrastructure | Skills + Build vs Buy + Observability |
| 2:30-3:30 | Module 3: Ship It | Metrics + Roadmap + Presentations |

---

# Module 1: Agent Design

**Teaching: 25 min | Lab: 75 min**

---

## Part A: Use Case Prioritization

---

### From Brainstorm to Backlog

You have 10 ideas from Day 1.

You can only build 1 this quarter.

**How do you choose?**

---

### Impact/Effort Matrix

```
         HIGH IMPACT
              │
    Quick     │     Strategic
    Wins      │     Bets
              │
─────────────┼────────────────
              │
    Fill      │     Money
    Later     │     Pit
              │
         LOW IMPACT

    LOW EFFORT ───────── HIGH EFFORT
```

---

### Scoring Criteria

| Criterion | Weight | What to Ask |
|-----------|--------|-------------|
| Impact | 1-5 | How much time/money saved? |
| Effort | 1-5 | Dev weeks? Integration complexity? |
| Compliance Risk | H/M/L | Regulatory exposure? |
| Data Sensitivity | H/M/L | PII? Financial data? |
| Time-to-Value | Fast/Slow | When do users see benefit? |

**Score = Impact × (6 - Effort) × Risk Multiplier**

Risk Multiplier: H=0.5, M=0.8, L=1.0

---

## Part B: Agent Patterns

---

### What is an Agent?

**Agent = LLM + Tools + Memory + Control Flow**

- **LLM**: The reasoning engine
- **Tools**: APIs, databases, functions it can call
- **Memory**: Context it retains across turns
- **Control Flow**: Logic that decides what happens next

---

### The 4 Canonical Patterns

---

### Pattern 1: Router

**Classify → Route to Specialist**

```
           ┌─────────────┐
           │   Router    │
           │  (Classify) │
           └──────┬──────┘
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
┌─────────┐ ┌─────────┐ ┌─────────┐
│ Agent A │ │ Agent B │ │ Agent C │
│ (Sales) │ │(Support)│ │(Billing)│
└─────────┘ └─────────┘ └─────────┘
```

**Use when:** Clear categories, different expertise needed

---

### Pattern 2: Chain

**Step 1 → Step 2 → Step 3**

```
┌─────────┐    ┌─────────┐    ┌─────────┐
│ Extract │ ──▶│ Analyze │ ──▶│ Generate│
│  Data   │    │  Data   │    │ Report  │
└─────────┘    └─────────┘    └─────────┘
```

**Use when:** Sequential processing, each step builds on previous

---

### Pattern 3: Orchestrator

**Planner + Sub-agents**

```
           ┌─────────────┐
           │ Orchestrator│
           │  (Planner)  │
           └──────┬──────┘
                  │ assigns tasks
     ┌────────────┼────────────┐
     ▼            ▼            ▼
┌─────────┐ ┌─────────┐ ┌─────────┐
│ Worker 1│ │ Worker 2│ │ Worker 3│
└────┬────┘ └────┬────┘ └────┬────┘
     │           │           │
     └───────────┴───────────┘
                  │
                  ▼
           ┌─────────────┐
           │   Combine   │
           │   Results   │
           └─────────────┘
```

**Use when:** Complex tasks, parallel execution possible

---

### Pattern 4: Human-in-the-Loop

**Auto Easy, Escalate Hard**

```
┌─────────┐    ┌─────────────┐
│ Request │ ──▶│  Confidence │
└─────────┘    │    Check    │
               └──────┬──────┘
                      │
          ┌───────────┴───────────┐
          │                       │
     High │                       │ Low
          ▼                       ▼
    ┌──────────┐           ┌──────────┐
    │   Auto   │           │  Human   │
    │ Complete │           │  Review  │
    └──────────┘           └──────────┘
```

**Use when:** High stakes, regulatory requirements, trust building

---

### Which Pattern for Enterprise?

**Usually #4 (Human-in-the-Loop)**

- Regulatory compliance requires human oversight
- Building trust takes time
- "AI-assisted" beats "AI-replaced" for adoption

**Sometimes #1 (Router)**

- Clear intent classification
- Different workflows per category
- Enables incremental automation

---

### State Machine Anatomy

Every agent has these components:

```
┌─────────────────────────────────────────┐
│                 AGENT                    │
├─────────────────────────────────────────┤
│  TRIGGER                                │
│  └─ API call / Schedule / User action   │
│                                         │
│  DECISION POINTS                        │
│  └─ If confidence < 80% → escalate      │
│  └─ If amount > $10K → require approval │
│                                         │
│  GUARDRAILS                             │
│  └─ Block if PII detected               │
│  └─ Reject if off-topic                 │
│                                         │
│  HUMAN CHECKPOINTS                      │
│  └─ Final review before send            │
│  └─ Override capability always on       │
└─────────────────────────────────────────┘
```

---

### Example: Document Validation Agent

```
┌─────────────────┐
│ Document Upload │  ◄── TRIGGER
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Extract Fields  │  ◄── STEP 1
│ (Name, ID, Date)│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Validate Format │  ◄── DECISION
│ & Completeness  │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
  Valid    Invalid
    │         │
    ▼         ▼
┌───────┐ ┌───────────┐
│ Auto  │ │  Human    │  ◄── HUMAN CHECKPOINT
│Approve│ │  Review   │
└───────┘ └───────────┘
```

---

## Part C: Failure Modes

---

### Pre-Mortem: Assume It Failed

**Before building, imagine it's 6 months from now.**

Your agent has been shut down.

**What went wrong?**

This mindset shift catches failures you'd otherwise miss.

---

### Failure Mode Table

| Failure Mode | Likelihood (1-5) | Severity (1-5) | Mitigation |
|--------------|------------------|----------------|------------|
| ? | ? | ? | ? |

**Risk Score = Likelihood × Severity**

Focus on high-risk failures first.

---

### Common Failure Mode Categories

| Category | Example | Why It Happens |
|----------|---------|----------------|
| **Hallucinated Identifiers** | Wrong account number, fake ticker | LLM generates plausible-looking data |
| **Missed Validation Flags** | Compliance issue not caught | Training data didn't cover edge cases |
| **Latency Spikes** | Slow during peak hours | API rate limits, cold starts |
| **Prompt Injection** | User tricks agent into wrong action | Adversarial input not filtered |

---

## Lab 1: Design Your Agent

**75 minutes total**

---

### Lab 1 Part A: Prioritize (20 min)

**Worksheet:**

| Use Case | Impact (1-5) | Effort (1-5) | Compliance Risk | Data Sensitivity | Score | Rank |
|----------|--------------|--------------|-----------------|------------------|-------|------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

**Score = Impact × (6 - Effort) × Risk Multiplier**

Risk Multiplier: H=0.5, M=0.8, L=1.0

**Outcome:** Pick ONE use case to design in Part B.

---

### Lab 1 Part B: Draw Your Agent (35 min)

**Template:**

```
TRIGGER: [API call / Schedule / User action]
    │
    ▼
STEP 1: [_______________]
    │
    ▼
DECISION: [If ___ then → Human Review]
          [Else → Step 2]
    │
    ▼
STEP 2: [_______________]
    │
    ▼
GUARDRAIL: [Block if ___]
    │
    ▼
OUTPUT: [_______________]
```

**Questions to answer:**
1. What pattern are you using? (Router/Chain/Orchestrator/Human-in-loop)
2. Where are your human checkpoints?
3. What triggers escalation?

---

### Lab 1 Part C: Failure Modes (20 min)

**Fill in for YOUR agent:**

| Failure Mode | Likelihood (1-5) | Severity (1-5) | Mitigation |
|--------------|------------------|----------------|------------|
| Hallucinated identifiers | | | |
| Missed validation flag | | | |
| Latency spike | | | |
| Prompt injection | | | |
| [Your specific risk] | | | |

**Debrief question:** Which mitigations are table stakes vs nice-to-have?

---

# Module 2: Agent Infrastructure

**Teaching: 20 min | Lab: 40 min**

---

## Part A: Agent Skills

---

### Teaching Agents Repeatable Workflows

What if your agent could:
- Load organizational procedures on demand
- Follow the same steps every time
- Be updated without retraining?

**Enter: Agent Skills**

---

### What are Agent Skills?

> "Folders of instructions, scripts, and resources that agents can discover and load dynamically"
> — Anthropic

Think of them as **playbooks for AI**.

---

### Progressive Disclosure

Agent loads only what's needed, when needed.

```
User: "Help me with KYC"
        │
        ▼
┌─────────────────┐
│ Agent discovers │
│   KYC Skill     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Loads relevant  │
│  instructions   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Executes with   │
│  full context   │
└─────────────────┘
```

**Not** loading everything upfront.

---

### Skill Anatomy

```
my-skill/
├── SKILL.md          # Required: YAML frontmatter + instructions
├── templates/        # Optional: Document templates
├── scripts/          # Optional: Automation scripts
└── examples/         # Optional: Few-shot examples
```

**SKILL.md structure:**
```yaml
---
name: kyc-extraction
description: Extract and validate KYC documents
triggers: [kyc, identity verification, document check]
---

# KYC Extraction Workflow

## Step 1: Document Classification
...
```

---

### Open Standard: agentskills.io

Works across:
- Claude
- GitHub Copilot
- OpenAI Codex
- Cursor
- VS Code

**Write once, use everywhere.**

---

## Part B: Build vs Buy

---

### The Real Question

It's not "build vs buy."

It's **"What layer do you own?"**

---

### The AI Stack

```
┌─────────────────────────────┐
│        DATA LAYER           │  Your proprietary data
├─────────────────────────────┤
│     EVAL/MONITORING         │  How you measure quality
├─────────────────────────────┤
│    SKILLS/WORKFLOWS         │  Your business logic
├─────────────────────────────┤
│     ORCHESTRATION           │  How agents coordinate
├─────────────────────────────┤
│       MODEL LAYER           │  The LLM itself
└─────────────────────────────┘
```

**Rule of thumb:** Own higher layers, rent lower layers.

---

### The Vector DB Question

**2023:** "You need a vector database for RAG"

**2025:** "Maybe not"

Modern agent SDKs (Claude Agent SDK, etc.) provide:
- **Tool Search**: Access thousands of tools without context bloat
- **Files API**: Document corpus management built-in
- **Memory**: Store/retrieve facts outside context window
- **MCP Tools**: Custom retrievers as simple Python functions

**When you still need Vector DB:**
- Millions of documents
- Sub-second latency requirements
- Complex hybrid search (semantic + filters)

**When you don't:**
- Thousands of docs (fits in tool search)
- Agent can query sources directly
- Skills handle retrieval logic

---

### Observability: Langfuse

**Open-source LLM observability**

What it tracks:
- **Traces**: Full request/response chains
- **Costs**: Token usage per request
- **Latency**: Response times
- **Prompt versions**: A/B testing prompts

**Deployment options:**
- Self-hosted (full control)
- Cloud (managed)

```
langfuse.com
```

---

### Testing: Ragas Framework

**Evaluate RAG pipelines**

| Metric | What It Measures |
|--------|-----------------|
| **Faithfulness** | Does answer match retrieved context? (hallucination detection) |
| **Answer Relevancy** | Does answer address the question? |
| **Context Precision** | Is retrieved context relevant? |
| **Citation Accuracy** | Are sources correctly attributed? |

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy

results = evaluate(dataset, metrics=[faithfulness, answer_relevancy])
```

---

### Decision Framework

| Layer | Build When | Buy When |
|-------|------------|----------|
| **Model** | Never (for most) | Always (Azure OpenAI, etc.) |
| **Orchestration** | Core differentiator | Standard patterns |
| **Skills** | Proprietary workflows | Generic tasks |
| **Eval** | Custom metrics needed | Standard benchmarks |
| **Observability** | Strict data residency | Speed to market |

**Hybrid:** Own the workflow, rent the compute.

---

## Lab 2: Build vs Buy Matrix

**40 minutes**

---

### Exercise: Fill the Matrix (30 min)

| Component | Build Option | Buy Option | Decision | Rationale |
|-----------|-------------|------------|----------|-----------|
| LLM | Azure OpenAI | OpenAI API | | |
| Prompt templates | Internal | Template library | | |
| Retrieval | Agent tools/MCP | Vector DB (Pinecone) | | |
| Skills/Workflows | Internal | Pre-built | | |
| Eval (Ragas) | Custom | Langsmith/Ragas | | |
| Observability | Grafana | Langfuse/Datadog | | |

**Rules:**
- No "TBD" allowed
- Best guess with stated assumptions
- Document your rationale

---

### Debrief Questions (10 min)

1. Where did your team disagree?
2. What assumptions drove your decisions?
3. What would change your answer?

---

# Module 3: Ship It

**Teaching: 10 min | Lab: 50 min**

---

### You Can't Prove ROI Without Baselines

> "We saved 50% of time!"
>
> "Compared to what?"
>
> "...we don't know."

**Measure BEFORE you build.**

---

### Three Metric Tiers

```
┌─────────────────────────────┐
│      BUSINESS METRICS       │  ◄── Execs care about this
│  Revenue, Cost, NPS, Risk   │
├─────────────────────────────┤
│      PRODUCT METRICS        │  ◄── PMs care about this
│  Adoption, Time saved, UX   │
├─────────────────────────────┤
│       MODEL METRICS         │  ◄── Engineers care about this
│  Accuracy, Latency, Cost    │
└─────────────────────────────┘
```

---

### The Trap

| What Teams Measure | What Execs Ask |
|-------------------|----------------|
| "95% accuracy!" | "Did revenue go up?" |
| "200ms latency!" | "Are customers happier?" |
| "$0.002 per call!" | "What's the total ROI?" |

**Bridge the gap:** Connect Tier 1 to Tier 3.

---

### Ship Monday, Not Someday

Your 1-pager should answer:

1. **What** are we building? (Use case + why)
2. **How** does it work? (Agent architecture)
3. **What** do we own? (Build vs Buy)
4. **How** do we know it works? (Metrics)
5. **What's** the first milestone?

---

### 1-Pager Template

```
┌─────────────────────────────────────────┐
│            [USE CASE NAME]              │
├─────────────────────────────────────────┤
│ PRIORITIZATION SCORE: ___               │
│ Pattern: [Router/Chain/Orchestrator/    │
│          Human-in-loop]                 │
├─────────────────────────────────────────┤
│ ARCHITECTURE                            │
│ [Your diagram from Lab 1]               │
├─────────────────────────────────────────┤
│ BUILD VS BUY                            │
│ [Key decisions from Lab 2]              │
├─────────────────────────────────────────┤
│ SUCCESS METRICS                         │
│ • Model: ___                            │
│ • Product: ___                          │
│ • Business: ___                         │
├─────────────────────────────────────────┤
│ FIRST MILESTONE: [Date] - [Deliverable] │
└─────────────────────────────────────────┘
```

---

## Lab 3: Ship It

**50 minutes**

---

### Lab 3 Part A: Define Metrics (15 min)

| Metric | Tier | Baseline | Target (3mo) | Target (12mo) | How to Measure |
|--------|------|----------|--------------|---------------|----------------|
| | Model | | | | |
| | Model | | | | |
| | Product | | | | |
| | Product | | | | |
| | Business | | | | |

**Requirement:** At least one baseline number (even a guess).

---

### Lab 3 Part B: Build Your 1-Pager (20 min)

Combine everything:
- Use case from Lab 1 prioritization
- Architecture from Lab 1 diagram
- Build vs Buy from Lab 2
- Metrics from Part A

**One page. No appendices.**

---

### Lab 3 Part C: Present (15 min)

**3 minutes per team**

Structure:
1. What's the use case? (30 sec)
2. What pattern? Why? (30 sec)
3. Key build vs buy decision (30 sec)
4. Top metric + baseline (30 sec)
5. First milestone (30 sec)
6. Biggest risk (30 sec)

---

## Wrap-Up

---

### What You Built Today

1. **Prioritized** your use cases
2. **Designed** an agent architecture
3. **Identified** failure modes
4. **Made** build vs buy decisions
5. **Defined** success metrics
6. **Created** a shippable 1-pager

---

### Next Steps

1. Get baseline metrics THIS WEEK
2. Build v0.1 in a sandbox
3. Define your human-in-the-loop checkpoints
4. Set up observability (Langfuse)
5. Ship to 5 users, then 50, then 500

---

### Remember

> "Ship Monday, not someday."

The best AI product is the one that's live.
