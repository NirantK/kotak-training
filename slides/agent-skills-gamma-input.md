# Agent Skills: Teaching AI to Follow Your Playbook

**Kotak Securities AI Training — Standalone Module**

---

## Opening

### Title
**Agent Skills: Teaching AI to Follow Your Playbook**
From inconsistent AI to reliable assistants

---

### The Promise

By end of session, you'll design a skill that makes your AI do the same task the same way every time.

No code. No training. Just structured instructions.

---

### The Problem Without Skills

| Without Skills | With Skills |
|----------------|-------------|
| Different answers to same question | Consistent responses |
| Forgets org procedures | Follows your playbook |
| Needs constant re-prompting | Loads knowledge on demand |
| Generic, unfocused output | Domain-specific expertise |

> "While Claude is powerful, real-world work demands procedural knowledge and organizational context."
> — Anthropic Engineering

---

### Agenda

```
1. Why agents fail without skills (10 min)
2. What skills are and how they work (15 min)
3. The Skill Design Framework (20 min)
4. Examples in action (15 min)
5. Design your own skill (30 min)
```

---

## The Problem

### The Context Window Trap

- Agents can only hold ~200K tokens at once
- Your org has millions of tokens of procedures, policies, guides
- Stuffing everything in = slow, expensive, confused

**The math:**
- 200K tokens ≈ 150,000 words
- One policy manual ≈ 50,000 words
- Five departments = 250,000 words
- Result: Doesn't fit

---

### The Consistency Problem

**Same query, three different outputs:**

Query: "What's the risk in this portfolio?"

| Attempt 1 | Attempt 2 | Attempt 3 |
|-----------|-----------|-----------|
| "The equity allocation looks high" | "Market volatility is the main concern" | "Consider the client's age" |

No memory of "how we do things here."
Every interaction starts from scratch.

---

### The Fragmentation Problem

Today's reality:
- Custom prompts per use case
- 10 use cases = 10 separate prompt libraries
- No sharing, no versioning, no reuse

```
Team A: KYC extraction prompt v3.2
Team B: KYC extraction prompt v2.1
Team C: Built their own from scratch
```

---

### What Organizations Need

| Need | Description |
|------|-------------|
| **Composable** | Mix and match capabilities |
| **Scalable** | Add new procedures without retraining |
| **Shareable** | Teams contribute, everyone benefits |
| **Updatable** | Change procedures, agent updates automatically |

---

### Enter Agent Skills

> "Skills are like an onboarding guide for a new hire — instructions, examples, and best practices that teach an agent how to perform a specific task."
> — Anthropic

**Instead of:** Fragmented, custom-designed agents for each use case

**With skills:** Composable capabilities by capturing and sharing procedural knowledge

---

## What Are Skills

### Skills = Playbooks for AI

**Definition:** Folders of instructions, scripts, and resources that agents discover and load dynamically

**Key insight:** Agent loads only what's needed, when needed

Think: Employee handbook, not brain surgery

---

### Progressive Disclosure

Three-level system for managing context efficiently:

```
┌─────────────────────────────────────────┐
│ Level 1: Name + Description (~100 tok)  │  Always loaded
└─────────────────────────────┬───────────┘
                              │ Agent decides relevance
                              ▼
┌─────────────────────────────────────────┐
│ Level 2: Full SKILL.md (<5000 tokens)   │  Loaded when activated
└─────────────────────────────┬───────────┘
                              │ Agent needs details
                              ▼
┌─────────────────────────────────────────┐
│ Level 3: Scripts, references, assets    │  Loaded on demand
└─────────────────────────────────────────┘
```

**Analogy:** Like a well-organized manual — table of contents first, then specific chapters, finally detailed appendix.

---

### Skill Anatomy

```
my-skill/
├── SKILL.md          # Required: Instructions
├── scripts/          # Optional: Python, Bash, JS
├── references/       # Optional: Detailed docs
└── assets/           # Optional: Templates, data
```

**The only required file is SKILL.md**

Everything else loads only when needed.

---

### The SKILL.md File

Two parts: YAML frontmatter + Markdown content

```yaml
---
name: kyc-extraction
description: Extract and validate KYC documents. Use when
  user mentions KYC, identity verification, Aadhaar, PAN,
  or document check.
---

# KYC Extraction Workflow

## When to Use
- User uploads ID document
- User asks about KYC status
- Compliance check requested

## Steps
1. Classify document type (Aadhaar, PAN, Passport)
2. Extract required fields
3. Validate against format rules
4. Return structured result or escalate
```

---

### Industry Adoption

Open standard at **agentskills.io** adopted by:

| Company | Integration |
|---------|-------------|
| Microsoft | VS Code Copilot |
| OpenAI | Codex CLI |
| Atlassian | Jira/Confluence agents |
| GitHub | Copilot workspace |
| Cursor, Figma | Native support |

Partner skills from: Canva, Stripe, Notion, Zapier

**Write once, use everywhere.**

---

### Skills + MCP = Complete Stack

| Layer | What It Does |
|-------|--------------|
| **MCP** | Connects AI to external tools (APIs, databases) |
| **Skills** | Teaches AI HOW to use those tools effectively |

> "MCP provides secure connectivity to external software and data, while skills provide the procedural knowledge for using those tools effectively."

**MCP = hands. Skills = training.**

---

## Skill Design Framework

### The 5-Part Framework

Every effective skill has:

```
1. TRIGGER: When should this skill activate?
2. CONTEXT: What background does the agent need?
3. STEPS: What's the procedure?
4. EXAMPLES: What does good look like?
5. GUARDRAILS: What should the agent never do?
```

---

### Part 1: Triggers

The description is the most critical component.

| Quality | Example |
|---------|---------|
| **Bad** | "Help with documents" |
| **Good** | "Extract and validate KYC documents from uploaded images. Use when user mentions KYC, identity verification, Aadhaar, PAN card, or document check." |

**Rules:**
- Write from Claude's perspective
- Include keywords users would actually say
- Be specific about boundaries
- Balance triggers with anti-triggers

---

### Part 2: Context

What the agent needs to know BEFORE acting:

- Relevant policies
- Domain terminology
- Organizational preferences
- Compliance requirements

**Rule of thumb:**
- Always needed? Put in SKILL.md
- Sometimes needed? Put in references/
- Rarely needed? Link to external source

---

### Part 3: Steps

Write like you're onboarding a new employee:

```markdown
## Workflow

### Step 1: Classify Document
Look for these indicators:
- Aadhaar: 12-digit number, UIDAI logo
- PAN: XXXXX1234X format, Income Tax logo

### Step 2: Extract Fields
Required fields for each type:
| Document | Required Fields |
|----------|----------------|
| Aadhaar | Name, DOB, Address, Number |
| PAN | Name, DOB, Father's Name, Number |
```

**Test:** Would a new hire understand this?

---

### Part 4: Examples

Show both good patterns AND edge cases:

```markdown
## Examples

### Good Extraction
Input: [Clear Aadhaar image]
Output:
{
  "document_type": "Aadhaar",
  "name": "Rajesh Kumar",
  "number": "XXXX-XXXX-1234",
  "confidence": 0.95
}

### Edge Case: Blurry Image
Input: [Blurry image]
Output: "Unable to extract with confidence.
Please upload a clearer image."
```

---

### Part 5: Guardrails

What the agent should NEVER do:

```markdown
## Guardrails

- Never store raw Aadhaar numbers — mask all but last 4 digits
- Never approve if confidence < 80%
- Never process documents that appear altered
- Always escalate to human if:
  - Document type unrecognized
  - Multiple failed extraction attempts
  - Information mismatch detected
```

**Think:** What would get us in trouble?

---

### The Complete Template

```yaml
---
name: [skill-name]
description: [What it does. When to use. Keywords.]
---

# [Skill Name]

## When to Use
[Trigger conditions]

## Context
[Background knowledge needed]

## Workflow
### Step 1: [Action]
[Details]

### Step 2: [Action]
[Details]

## Examples
[Good and bad patterns]

## Guardrails
[What to never do]
```

---

## Examples in Action

### Example 1: Portfolio Analysis Skill

From Day 1 — turn the extraction workflow into a reusable skill:

```yaml
---
name: portfolio-analysis
description: Analyze portfolio screenshots and generate
  client-ready insights. Use when user shares MProfit,
  Zerodha, Kite, or other portfolio data.
---

# Portfolio Analysis

## When to Use
- Client shares portfolio screenshot
- RM needs quick analysis
- Market movement requires client update

## Workflow
1. Extract holdings from image → JSON
2. Calculate concentration risk
3. Compare to today's market
4. Generate client email

## Guardrails
- No specific buy/sell advice
- Include disclaimer on all outputs
- Escalate if portfolio > ₹10 crore
```

---

### Example 2: KYC Extraction Skill

Common enterprise use case:

```yaml
---
name: kyc-extraction
description: Extract and validate identity documents.
  Triggers: KYC, Aadhaar, PAN, verification, ID check.
---

## Workflow
1. Classify: Aadhaar / PAN / Passport / Other
2. Extract: Required fields per document type
3. Validate: Format rules, completeness
4. Route: Auto-approve or human review

## Guardrails
- Mask sensitive numbers in logs
- Confidence < 80% → human review
- Never approve altered documents
```

---

### Example 3: Customer Query Router

Service desk automation:

```yaml
---
name: query-router
description: Classify customer queries and route to
  appropriate specialist. Triggers: support, help,
  question, issue, problem.
---

## Classification
| Intent | Route To |
|--------|----------|
| Account balance | Balance Skill |
| Transaction issue | Dispute Skill |
| New product | Sales Skill |
| Complaint | Human Agent |

## Guardrails
- Unknown intent → Human Agent
- Frustrated language → Human Agent immediately
- Never promise resolution without human approval
```

---

### Skill Ecosystem Preview

Categories available today:

| Category | Examples |
|----------|----------|
| **Document** | PDF, DOCX, XLSX, PPTX processing |
| **Development** | Code review, MCP builder, testing |
| **Design** | Theme factory, brand guidelines |
| **Security** | Vulnerability scanning, audit trails |
| **Workflow** | Linear, n8n, Notion integration |
| **Finance** | Portfolio analysis, KYC, compliance |

Source: github.com/VoltAgent/awesome-claude-skills

---

## Design Lab

### Lab Setup

```
Time: 30 minutes
Outcome: First draft of a skill for YOUR use case

Materials:
- Skill Design Worksheet (next slide)
- Examples from earlier sessions
- Partner for peer review
```

---

### Skill Design Worksheet

```
┌─────────────────────────────────────────────────────┐
│ SKILL NAME: ____________________________________    │
├─────────────────────────────────────────────────────┤
│ TRIGGERS (keywords users would say):                │
│ 1. ____________________                             │
│ 2. ____________________                             │
│ 3. ____________________                             │
├─────────────────────────────────────────────────────┤
│ CONTEXT (what agent needs to know):                 │
│ ________________________________________________    │
│ ________________________________________________    │
├─────────────────────────────────────────────────────┤
│ STEPS (write like onboarding a new hire):           │
│ 1. ____________________                             │
│ 2. ____________________                             │
│ 3. ____________________                             │
│ 4. ____________________                             │
├─────────────────────────────────────────────────────┤
│ EXAMPLE (what does good output look like?):         │
│ ________________________________________________    │
│ ________________________________________________    │
├─────────────────────────────────────────────────────┤
│ GUARDRAILS (what should agent NEVER do?):           │
│ 1. ____________________                             │
│ 2. ____________________                             │
└─────────────────────────────────────────────────────┘
```

---

### Lab Instructions

**Part A (10 min): Pick your use case**
- What repetitive task would benefit from consistency?
- What procedures exist but aren't followed consistently?
- What do you explain over and over to new team members?

**Part B (15 min): Fill the worksheet**
- Be specific on triggers — what words would someone say?
- Write steps like onboarding a new hire
- Think about what could go wrong

**Part C (5 min): Peer review**
- Swap with neighbor
- Ask: "Would a new hire understand this?"
- Identify missing guardrails

---

### Closing

**What You Can Do Now:**
- Recognize when a skill would help
- Design skill structure using the 5-part framework
- Write trigger-rich descriptions
- Create step-by-step procedures agents can follow

**Next Steps:**
1. Pick ONE skill to build this week
2. Start with SKILL.md only (no scripts yet)
3. Test with a colleague before deploying
4. Iterate based on what doesn't work

---

### Resources

- **Specification:** agentskills.io/specification
- **Best practices:** platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- **Examples:** github.com/VoltAgent/awesome-claude-skills
- **Anthropic blog:** anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

---

*Save your worksheet. You'll turn it into a real SKILL.md file this week.*
