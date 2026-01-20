# Day 1 Exercises: Building to the Capstone

**Theme:** Same mock data throughout. Each module adds a skill. Capstone combines them all.

**Audience:** Engineering + Product (primary), some Marketing

**Key Principle:** Success > Learning. Every exercise has a clear win moment.

---

## Mock Data (Used All Day)

### Portfolio Screenshot
MProfit wealth management dashboard showing Mehta Family portfolio (₹41 crore):
- Asset classes: Stocks, Mutual Funds (Equity/Debt), Insurance, Private Equity, FDs, Traded Bonds, NCD/Debentures, Post Office, Gold, Property
- Columns: Amount Invested, Current Price, Today's Gain, Unrealised Gain, Current Value
- Market context: Sensex/Nifty performance visible (-0.55%, -0.47%)
- Clear red/green gain indicators

### Market Context Screenshot
BBC News headline: "Trump says Venezuela will be 'turning over' up to 50 million barrels of oil to US"
- Geopolitical news affecting energy sector
- Oil price implications for portfolio

**Instructor prepares:** Both screenshots ready to share/display.
- `training/mock-data/portfolio.png`
- `training/mock-data/market-news.png`

---

## Skill Progression

| Module | Skill | Exercise | Builds To |
|--------|-------|----------|-----------|
| Module 1 | Prompt Architecture | Rewrite bad prompt using RGC/STIC | Capstone Round 1-2 |
| Module 2 | Data Extraction + Chaining | Screenshot → JSON → Analysis | Capstone pipeline |
| Module 3 | Systematizing | Make it a reusable template | Capstone Round 3 |
| Capstone | All combined | Full pipeline to client email | Final deliverable |

---

## Module 1 Exercise: Prompt Architecture

**Block:** Advanced Prompt Architecture & Meta-Prompting (10:15-11:45)
**Exercise Time:** 20 min
**Position:** After teaching RGC and STIC frameworks

### Exercise: "Make the AI a Better Analyst"

**Setup:** Give them this bad prompt and the portfolio screenshot:

```
Look at this data and tell me what's happening.
[PASTE PORTFOLIO SCREENSHOT]
```

**Challenge:** Rewrite using RGC/STIC to get structured output.

### Scaffolded Steps (each is a win)

**Step 1: Add a Role (5 min)**
```
You are a senior portfolio analyst at a wealth management firm.

Look at this data and tell me what's happening.
[PASTE PORTFOLIO SCREENSHOT]
```
→ Compare output. Already better.

**Step 2: Add a Goal (5 min)**
```
You are a senior portfolio analyst at a wealth management firm.

Analyze this portfolio and identify the key risk for a client review meeting.
[PASTE PORTFOLIO SCREENSHOT]
```
→ Compare output. More focused.

**Step 3: Add Constraints (5 min)**
```
You are a senior portfolio analyst at a wealth management firm.

Analyze this portfolio and identify the key risk for a client review meeting.

Constraints:
- Use plain language (no jargon)
- Limit to 3 bullet points
- Flag any holding >15% weight as concentration risk

[PASTE PORTFOLIO SCREENSHOT]
```
→ Compare output. Dramatically better.

**Step 4: Compare before/after (5 min)**
- Show original "Look at this data" output
- Show final RGC/STIC output
- "Same screenshot, completely different quality"

### Win Moment
"Same data, completely different output quality."

### Facilitator Notes
- Have both outputs ready to show side-by-side
- If someone finishes early, challenge them to add meta-prompting ("First, describe your analysis approach, then analyze")

---

## Module 2 Exercise: Data Extraction + Chaining

**Block:** Workflows vs Agents & Data Extraction (12:45-14:15)
**Exercise Time:** 25 min
**Position:** After teaching workflows and structured extraction

### Exercise: "Screenshot to Pipeline"

**The wow:** They paste a *screenshot* of a spreadsheet. AI extracts structured data from pixels. No CSV, no API, no data pipeline.

**Challenge:** Build a two-step chain:
1. Step 1: Screenshot of Excel → Structured JSON
2. Step 2: JSON + Market screenshot → Analysis

### Step 1: Extract (10 min)

**Prompt:**
```
This is a screenshot of a wealth management portfolio dashboard.

Extract the data as JSON:
{
  "client_name": string,
  "net_worth": number,
  "asset_classes": [
    {
      "type": string,
      "amount_invested": number,
      "current_value": number,
      "today_gain": number,
      "today_gain_pct": number,
      "unrealised_gain_pct": number
    }
  ],
  "market_context": {
    "sensex": number,
    "sensex_change_pct": number,
    "nifty": number,
    "nifty_change_pct": number
  },
  "largest_allocation": {"type": string, "value": number},
  "worst_performer_today": {"type": string, "loss": number},
  "concentration_flags": [asset classes > 25% of portfolio]
}

[PASTE PORTFOLIO SCREENSHOT]
```

**Win:** "It read a screenshot and gave me clean JSON."

### Step 2: Analyze (10 min)

**Prompt:**
```
Given this portfolio analysis:
[PASTE JSON FROM STEP 1]

And this market context:
[PASTE SCREENSHOT OF NEWS/CHART]

Answer:
1. Is this portfolio more or less exposed to today's market move than average?
2. What's the single biggest risk right now?
3. What would you tell the client first?
```

**Win:** "Two inputs combined into one analysis."

### Step 3: Reflect (5 min)

Discussion questions:
- Why separate extraction from analysis?
- What could go wrong if we did it all in one prompt?
- Where else could you use this pattern?

### Win Moment
"It read a screenshot and turned it into data I can use. I just built a pipeline."

### Facilitator Notes
- Have backup JSON ready if someone's extraction fails
- Emphasize: "This is the foundation of every AI workflow"

---

## Module 3 Exercise: Systematizing AI

**Block:** Systematizing AI: Projects, Automation & Workflows (14:15-15:00)
**Exercise Time:** 15 min
**Position:** After teaching automation patterns

### Exercise: "Make It Reusable"

**The shift:** From "this worked once" → "this works every time"

**Challenge:** Take the chain from Module 2 and turn it into a reusable template for ANY client.

### Step 1: Identify Variables (5 min)

**Worksheet:**
```
What CHANGES between clients?
□ Client name
□ Portfolio screenshot
□ Market context screenshot
□ Client risk profile (conservative/moderate/aggressive)
□ Relationship manager name
□ ______________________
□ ______________________

What STAYS THE SAME?
□ Extraction JSON format
□ Analysis structure
□ Output format
□ ______________________
```

### Step 2: Build the Template (10 min)

**Starter template (they complete it):**
```
=== CLIENT PORTFOLIO ANALYZER v1.0 ===

INPUTS (change per client):
- Client Name: {{CLIENT_NAME}}
- Risk Profile: {{RISK_PROFILE}} [conservative/moderate/aggressive]
- RM Name: {{RM_NAME}}
- Portfolio Screenshot: {{PORTFOLIO_IMAGE}}
- Market Context: {{MARKET_IMAGE}}

=== STEP 1: EXTRACT ===
This is a screenshot of a wealth management portfolio dashboard.

Extract the data as JSON:
{
  "client_name": string,
  "net_worth": number,
  "asset_classes": [...],
  "market_context": {...},
  "largest_allocation": {...},
  "worst_performer_today": {...},
  "concentration_flags": [...]
}

[INSERT {{PORTFOLIO_IMAGE}}]

=== STEP 2: ANALYZE ===
Given this portfolio analysis:
[INSERT STEP 1 OUTPUT]

And this market context:
[INSERT {{MARKET_IMAGE}}]

Client risk profile: {{RISK_PROFILE}}

Answer:
1. Exposure vs market average?
2. Single biggest risk?
3. What to tell client first?

=== STEP 3: GENERATE EMAIL ===
Write an email to {{CLIENT_NAME}} that:
- Matches their {{RISK_PROFILE}} risk tolerance
- [They add more criteria here]

Sign off as {{RM_NAME}}.
```

### Win Moment
"I just built a system, not just a prompt."

### Bridge to Capstone
"In the capstone, you'll run this full pipeline end-to-end and produce a client-ready email."

### Facilitator Notes
- This previews the capstone structure
- If time short, do Step 1 as group discussion, Step 2 as demo

---

## Day 1 Flow Summary

```
10:00  Opening (15 min)
       - Introductions, logistics
       - Show the portfolio screenshot they'll use all day
       - "By 4pm, you'll turn this into a client email"
       ↓
10:15  Module 1: Learn RGC/STIC (75 min)
       Exercise: Improve bad prompt → good prompt
       ↓
12:00  Lunch (45 min)
       ↓
12:45  Module 2: Learn workflows + extraction (90 min)
       Exercise: Screenshot → JSON → Analysis
       ↓
14:15  Module 3: Learn systematization (45 min)
       Exercise: Make it a reusable template
       ↓
15:00  CAPSTONE: Do it all together (60 min)
       One end-to-end prompt combining everything:
       Round 1: Basic extraction
       Round 2: Add structure
       Round 3: Add personalization
       → Client-ready email
       ↓
16:00  Done. Everyone succeeded.
```

---

## Materials Checklist

**Instructor prepares:**
- [ ] Portfolio screenshot (Excel showing 10 stocks)
- [ ] Market context screenshot (news headline or chart)
- [ ] Bad prompt example for Module 1
- [ ] Backup JSON for Module 2 (in case extraction fails)
- [ ] Template worksheet for Module 3
- [ ] Rescue prompts for capstone (100% complete versions)
- [ ] Nano Banana demo ready for capstone close

**Participants need:**
- [ ] Access to ChatGPT/Claude (or Azure AI Foundry)
- [ ] Ability to paste images
- [ ] Notepad/doc for saving their prompts
