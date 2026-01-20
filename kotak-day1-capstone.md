# Day 1 Capstone: Build Your AI Analyst

**Title:** "From Raw Data to Client Communication"
**Time:** 60 minutes (15:00-16:00)
**Audience:** Engineering + Product (primary), some Marketing

---

## Overview

Participants run a complete end-to-end prompt that turns portfolio screenshot + market screenshot into a personalized client email. This is synthesis of everything from Day 1 - doing it all together as one combined flow.

**Key Principle:** Success > Learning. Everyone completes. Everyone feels accomplished.

---

## Structure

| Phase | Time | What happens |
|-------|------|--------------|
| Setup | 5 min | Explain the challenge, distribute mock data |
| Round 1 | 15 min | Basic extraction → working but ugly output |
| Round 2 | 15 min | Add structure → clean, organized output |
| Round 3 | 15 min | Add personalization → client-ready email |
| Demo + Close | 10 min | Instructor demos Nano Banana visual version, celebrate wins |

---

## Mock Data (Instructor Provides)

### Screenshot 1: Portfolio (MProfit Dashboard)
MProfit wealth management dashboard showing Mehta Family portfolio (₹41 crore):
- Asset classes: Stocks, Mutual Funds (Equity/Debt), Insurance, Private Equity, FDs, Traded Bonds, NCD/Debentures, Post Office, Gold, Property
- Columns: Amount Invested, Current Price, Today's Gain, Unrealised Gain, Current Value
- Market context: Sensex/Nifty performance visible (-0.55%, -0.47%)

### Screenshot 2: Market Context
BBC News headline: "Trump says Venezuela will be 'turning over' up to 50 million barrels of oil to US"
- Geopolitical news affecting energy sector and oil prices

**Files:** `training/mock-data/portfolio.png`, `training/mock-data/market-news.png`

**Same screenshots used all day** - continuity from Module 1 → Module 2 → Module 3 → Capstone

---

## Round 1: Basic Extraction (15 min)

**Goal:** Get something working. Ugly is fine.

**Starter prompt (participants fill the gaps):**

```
You are analyzing a client portfolio.

Here is the portfolio screenshot:
[PASTE PORTFOLIO SCREENSHOT]

Here is today's market context:
[PASTE MARKET SCREENSHOT]

Extract:
1. Total net worth
2. Top 3 asset classes by value
3. Worst performer today (biggest loss)
4. ______________________ (add 1-2 more fields)

Then write a brief summary.
```

**What they learn:** Basic extraction works. Output is functional but robotic.

**Win:** "It read my screenshot and extracted the data!"

---

## Round 2: Add Structure (15 min)

**Goal:** Organize output, make it usable.

**They modify prompt to add:**

```
Format your response as:

## Portfolio Snapshot
- Net worth:
- Asset classes count:

## Market Impact Assessment
| Asset Class | Value | Today's Gain/Loss | Risk Flag |
|-------------|-------|-------------------|-----------|

## Key Concern
[One sentence on biggest risk]

## Recommended Talking Point
[One sentence for client conversation]
```

**What they learn:** Structure transforms usability. Same data, much clearer.

**Win:** "This actually looks like something I'd use."

---

## Round 3: Add Personalization (15 min)

**Goal:** Client-ready email they could send.

**They add context + tone:**

```
The client is Mr. Rajesh Mehta, a conservative investor
who gets anxious during market volatility. He's been with
Kotak for 8 years.

Write an email that:
- Opens with reassurance, not alarm
- Explains the market context simply
- Highlights what's protecting his portfolio
- Ends with a clear next step (call scheduling)

Tone: Calm, confident, personal. No jargon.
Sign off as: Priya, his Relationship Manager
```

**What they learn:** Context + constraints = dramatically better output.

**Win:** "I could actually send this."

---

## Demo + Close (10 min)

### Instructor Demo: Visual Briefing
Show what's possible with Nano Banana 3 Pro:
- Take the same analysis
- Generate a one-page visual briefing with charts/graphics
- "This is where it's going - you just built the foundation"

### Celebrate Wins
- Ask 2-3 participants to share their email output
- Highlight what worked well
- "You just built an AI analyst in 45 minutes"

---

## Connection to Earlier Modules

**This is synthesis, not new learning.** They've practiced each skill separately. Now they do it all together in one end-to-end flow.

| Module | Skill Practiced | Used in Capstone |
|--------|----------------|------------------|
| Module 1: Prompt Architecture | RGC/STIC frameworks, meta-prompting | Role, goal, constraints in prompt |
| Module 2: Workflows & Data Extraction | Screenshot → JSON → Analysis | Extraction + reasoning chain |
| Module 3: Systematizing AI | Template with variables | Personalization placeholders |

**Why this works:** Each round of the capstone reinforces a skill they already practiced. No new concepts, just combination.

---

## Facilitator Notes

### If someone gets stuck:
- Have a "rescue prompt" ready that's 100% complete
- Pair them with someone who finished
- Remind: "Working > Perfect"

### Time buffer:
- Round 3 can be shortened to 10 min if running late
- Demo can be cut to 5 min if needed

### Success metric:
Every participant has a working client email by 15:55.
