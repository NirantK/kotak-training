# AI for Wealth Management
## Day 1: From Prompts to Pipelines
### Scaled Focus Inc. for Kotak Securities | January 2026
### Contact: nirant@scaledfocus.com | +91 7737887058

---

# OPENING

## By 4pm Today
You will turn a portfolio screenshot into a client-ready email using AI. No code. No API. Just prompts.

## Today's Path
- 10:00 Start → You've used ChatGPT
- 11:30 Module 1 → You can architect prompts
- 14:15 Module 2 → You can chain AI steps
- 15:00 Module 3 → You can build reusable systems
- 16:00 Capstone → You've built an AI analyst

Same data all day. New skills each hour.

## What You Need
**Required:** Browser with ChatGPT or Claude, ability to paste images, notepad for saving prompts

**We Provide:** Portfolio screenshot (MProfit), market news screenshot, all prompt templates

Azure AI Foundry available for those who prefer Microsoft stack.

## Meet the Mehta Family Portfolio
₹41 crore across 11 asset classes | Sensex down 0.55% today. This screenshot will be your input all day.

---

# MODULE 1: Advanced Prompt Architecture
## Scaled Focus Inc. | nirant@scaledfocus.com | +91 7737887058
*From vague requests to precise instructions*

## Why Prompts Fail
**Bad prompt:** "Look at this data and tell me what's happening."

What you get: Generic, unfocused, inconsistent output
What you need: Specific, structured, reliable output

The AI is capable. Your instructions aren't.

## Framework 1: RGC
Every good prompt has three parts:

| Component | Question | Example |
|-----------|----------|---------|
| **R**ole | Who is the AI? | "You are a senior portfolio analyst" |
| **G**oal | What should it do? | "Identify the key risk for a client meeting" |
| **C**onstraints | What are the rules? | "Use plain language, limit to 3 bullets" |

Memory trick: Role → Goal → Constraints = RGC

## RGC: Before & After
**Before (no RGC):** "Look at this data and tell me what's happening."
- No role, no clear goal, no constraints

**After (with RGC):** "You are a senior portfolio analyst. Analyze this portfolio and identify the key risk for a client meeting. Constraints: Plain language (no jargon), limit to 3 bullet points."
- Clear role, goal, constraints

## Framework 2: STIC
For complex tasks, add structure:

| Component | What It Does | Example |
|-----------|--------------|---------|
| **S**ituation | Set the context | "The market is down 2% today" |
| **T**ask | Define the job | "Write a client reassurance email" |
| **I**nstructions | Step-by-step guidance | "First summarize, then recommend" |
| **C**ontext | Provide background | "Client is conservative, 65 years old" |

STIC works well for multi-step or nuanced tasks.

## When to Use Which
| Situation | Use | Why |
|-----------|-----|-----|
| Quick analysis | RGC | Simple, fast |
| Client communication | STIC | Needs context, nuance |
| Data extraction | RGC | Structured output |
| Recommendations | STIC | Requires reasoning |

Rule of thumb: Start with RGC. Add STIC elements when output isn't right.

## Powerful Constraints
**Output format:** "Respond in JSON", "Use bullet points", "Limit to 100 words"

**Tone:** "Use plain language", "Be reassuring", "No jargon"

**Logic:** "Flag anything >15% as concentration risk", "Compare to benchmark", "Rank by importance"

**Safety:** "Do not give specific buy/sell advice", "Include disclaimer"

## Advanced: Meta-Prompting
Ask the AI to think before acting:
"First, describe your analysis approach. Then, analyze the portfolio. Finally, summarize your key finding."

Why it works: Forces structured reasoning, catches errors early

Pro tip: Add "Think step by step" for complex analysis

## Prompt Anti-Patterns
| Mistake | Problem | Fix |
|---------|---------|-----|
| Too vague | "Analyze this" | Specify what to analyze FOR |
| Too long | 500-word prompt | Focus on constraints, not instructions |
| No examples | Unclear format | Show one example of desired output |
| All at once | Overloaded | Break into steps |

Simplicity beats complexity. Add only what changes the output.

## Same Data, Different Output
**Vague prompt output:** "The portfolio shows various investments including stocks, mutual funds, and other assets. There appears to be some gains and losses..." - Generic, unhelpful

**RGC prompt output:** "Key Risk: Stock concentration at 27% of portfolio during a down market (-0.55% Sensex). Action: Review equity allocation given client's risk profile." - Specific, actionable

## Exercise: Make the AI a Better Analyst
**Time:** 20 minutes

**Challenge:** Transform a bad prompt into a good one using RGC/STIC

**Steps:**
1. Add a Role (5 min)
2. Add a Goal (5 min)
3. Add Constraints (5 min)
4. Compare before/after (5 min)

**Win:** Same data, completely different output quality.

---

# MODULE 2: Workflows & Data Extraction
## Scaled Focus Inc. | nirant@scaledfocus.com | +91 7737887058
*From screenshots to structured data*

## AI Can Read Screenshots
**Old way:** Export to CSV, clean data, write parsing code, handle edge cases - Hours of work

**New way:** Paste screenshot, ask for JSON - 30 seconds

Vision models can extract structured data from images of spreadsheets, dashboards, documents.

## From Pixels to Pipeline
Screenshot → JSON → Analysis → Email
(image) → (data) → (insight) → (action)

JSON is the bridge between unstructured inputs (screenshots, PDFs, emails) and structured processing (analysis, comparison, decisions).

Once you have clean JSON, everything else is easy.

## Define What You Want
```json
{
  "client_name": "string",
  "net_worth": "number",
  "asset_classes": [
    {"type": "string", "current_value": "number", "today_gain_pct": "number"}
  ],
  "worst_performer_today": {"type": "string", "loss": "number"}
}
```
Be specific. The AI follows your schema exactly.

## The Extraction Pattern
"This is a screenshot of [WHAT IT IS]. Extract the data as JSON: {YOUR SCHEMA HERE} [PASTE SCREENSHOT]"

That's it. Schema in, data out.

Pro tip: Start with a simple schema. Add fields as needed.

## Workflows vs Agents
| Aspect | Workflow | Agent |
|--------|----------|-------|
| Control | You define each step | AI decides what to do |
| Predictability | High - same steps every time | Variable - may take different paths |
| Debugging | Easy - check each step | Hard - "why did it do that?" |
| Best for | Repeatable processes | Open-ended exploration |

For production use cases: Start with workflows. Add agency only if needed.

## The Workflow Pattern
Step 1: Extract → Structured data
Step 2: Analyze → Insights
Step 3: Generate → Output

Each step is a separate prompt. Output of one feeds into the next.

Why separate steps? Easier to debug, can verify intermediate results, reuse steps across workflows.

## Chaining in Practice
**Step 1: Extract** - "Extract portfolio data as JSON [SCREENSHOT]" → JSON output

**Step 2: Analyze** - "Given this portfolio: [JSON FROM STEP 1] And this news: [NEWS SCREENSHOT] What's the risk?" → Analysis

## Single vs Chained Prompts
**Single prompt problems:** Extraction errors hidden, can't verify intermediate data, hard to debug, inconsistent structure

**Chained prompt benefits:** Verify extraction before analysis, catch errors early, consistent JSON structure, reusable components

Rule: If extraction fails, analysis is garbage. Always verify the data.

## Combining Different Inputs
| Input Type | Example | Extraction |
|------------|---------|------------|
| Screenshot | Portfolio dashboard | Asset allocations |
| News image | BBC headline | Market context |
| PDF | Research report | Key findings |
| Text | Client notes | Preferences |

The AI sees it all. You decide what to extract.

## When Extraction Fails
| Problem | Symptom | Fix |
|---------|---------|-----|
| Low image quality | Missing fields | Use higher resolution |
| Complex layout | Wrong data | Simplify schema |
| Ambiguous labels | Confused mapping | Be explicit in prompt |

Always have backup JSON ready for exercises. Extraction isn't 100% reliable.

## What You're About To Do
1. Paste a screenshot of a portfolio dashboard
2. Get clean JSON with all the data extracted
3. Add market news screenshot
4. Get analysis combining both

No CSV export. No data cleaning. No code. Just paste → extract → analyze.

## Exercise: Screenshot to Pipeline
**Time:** 25 minutes

**Challenge:** Build a two-step extraction and analysis chain

**Steps:**
1. Extract portfolio data to JSON (10 min)
2. Add market context, get analysis (10 min)
3. Reflect on the pattern (5 min)

**Win:** "I just built a data pipeline with screenshots."

---

# MODULE 3: Systematizing AI
## Scaled Focus Inc. | nirant@scaledfocus.com | +91 7737887058
*From "it worked once" to "it works every time"*

## Prompts → Templates → Systems
| Level | What It Is | Reliability |
|-------|------------|-------------|
| Prompt | One-off instruction | Works sometimes |
| Template | Reusable with variables | Works consistently |
| System | Automated pipeline | Works at scale |

Goal: Turn your working prompts into templates anyone can use.

## Identifying Variables
**What CHANGES between runs?**
- {{CLIENT_NAME}} - Different client each time
- {{PORTFOLIO_IMAGE}} - Different data
- {{RISK_PROFILE}} - Conservative/moderate/aggressive
- {{RM_NAME}} - Who signs the email

**What STAYS THE SAME?**
- JSON schema structure
- Analysis questions
- Output format

## A Complete Template
```
=== CLIENT PORTFOLIO ANALYZER v1.0 ===
INPUTS: Client: {{CLIENT_NAME}}, Risk Profile: {{RISK_PROFILE}}, RM: {{RM_NAME}}
=== STEP 1: EXTRACT === [Fixed extraction prompt] [INSERT {{PORTFOLIO_IMAGE}}]
=== STEP 2: ANALYZE === [Fixed analysis prompt] Client risk profile: {{RISK_PROFILE}}
=== STEP 3: GENERATE === Write email to {{CLIENT_NAME}}... Sign as {{RM_NAME}}
```

## Templates Enable Scale
**Without templates:** Rewrite prompt each time, inconsistent quality, knowledge in one person's head, can't delegate

**With templates:** Fill in variables, consistent output, documented process, anyone can run it

Templates turn expertise into infrastructure.

## The Automation Path
Manual: You paste, you run, you edit
↓
Template: You fill variables, run template
↓
Semi-auto: System fills variables, you review
↓
Full auto: System runs, flags exceptions

Today: We're building the template layer.
Tomorrow: We'll discuss productization.

## Exercise: Make It Reusable
**Time:** 15 minutes

**Challenge:** Turn your working chain into a template for ANY client

**Steps:**
1. Identify what changes vs stays same (5 min)
2. Build the template with variables (10 min)

**Win:** "I just built a system, not just a prompt."

## What You've Built Today
| Module | Skill | You Can Now... |
|--------|-------|----------------|
| 1 | RGC/STIC | Write precise, effective prompts |
| 2 | Extraction | Turn screenshots into data |
| 3 | Templates | Make workflows reusable |

Capstone: Combine all three into one end-to-end system.
15-minute break, then we put it all together.

---

# CAPSTONE: Build Your AI Analyst
## Scaled Focus Inc. | nirant@scaledfocus.com | +91 7737887058
*60 minutes to client-ready output*

## Your Final Challenge
**Input:** Portfolio screenshot (Mehta Family, ₹41 crore), Market news (Venezuela oil headline)

**Output:** Client-ready email for Mr. Rajesh Mehta, Conservative investor, anxious about volatility, Reassuring tone, clear next steps

**Time:** 60 minutes, 3 rounds

## Capstone Structure
| Round | Time | Goal | Win |
|-------|------|------|-----|
| 1 | 15 min | Basic extraction | "It read my data!" |
| 2 | 15 min | Add structure | "This is usable!" |
| 3 | 15 min | Add personalization | "I could send this!" |
| Demo | 10 min | See visual version | "Wow, what's possible" |

Remember: Working > Perfect. Get something running, then improve.

---

# Day 1 Complete
## Scaled Focus Inc. for Kotak Securities

**You built:**
- Prompts that work consistently (RGC/STIC)
- Data extraction from screenshots
- A reusable AI analyst template

**Tomorrow:** Product architecture, metrics, and your Impact Memo

Save your prompts. You'll use them tomorrow.

### Contact: nirant@scaledfocus.com | +91 7737887058
