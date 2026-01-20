# First Trade Activation: Amount-First Design

> **Alternative PRD** for Kotak Securities new user activation feature

**Problem:** 90% of new users never place their first trade.

**Insight:** Current PRD is stock-first (discover stocks → buy). New investors don't know stocks. They know amounts.

**Proposal:** Amount-first flow — "I have ₹1000, what can I buy?" in 3 steps.

---

## Core Flow (3 Steps)

### Step 1: Home Widget

```
┌─────────────────────────────────┐
│ Hi Amit, start investing        │
│ with just ₹500                  │
│                        [→]      │
└─────────────────────────────────┘
```

- Personalized with user name
- Anchors on low, non-threatening amount (₹500)
- Single tap opens investment screen

### Step 2: Amount + Stock Selection (Single Screen)

```
┌─────────────────────────────────┐
│ How much to start with?         │
│                                 │
│ [₹500]  [₹1000]  [₹2000]  [...]│
│                                 │
│ ┌─────────────────────────────┐ │
│ │ 🎤 "Or just tell me"        │ │
│ └─────────────────────────────┘ │
│                                 │
│ ─────────────────────────────── │
│ With ₹1000, you could invest in:│
│                                 │
│ ┌─────────┐  ┌─────────┐       │
│ │ TATA    │  │ INFY    │       │
│ │ ₹947    │  │ ₹1,420  │       │
│ │ +2.3%   │  │ +1.1%   │       │
│ └─────────┘  └─────────┘       │
│                                 │
│ [ Invest ₹1000 in TATA → ]     │
└─────────────────────────────────┘
```

**Key interactions:**

- Tap amount OR speak amount
- Stocks update dynamically based on amount
- Single CTA to proceed

### Step 3: Payment + Confirm

```
┌─────────────────────────────────┐
│ Invest ₹1,000 in TATA           │
│                                 │
│ Your balance: ₹247              │
│ Amount needed: ₹753             │
│                                 │
│ ○ Add ₹753 via UPI              │
│ ○ Add ₹753 via Net Banking      │
│ ○ Add ₹1,000 (round up)         │
│                                 │
│ [ Continue → ]                  │
└─────────────────────────────────┘
```

**Edge case:** If balance >= order amount, skip payment → direct confirm.

---

## Stock Selection Logic

**Server-side screener for beginners:**

```
Given amount ₹X:
1. Filter: share_price <= X (can afford at least 1 share)
2. Filter: market_cap > ₹50,000 Cr (large caps only)
3. Filter: avg_daily_volume > 1M (liquid)
4. Rank by: brand_recognition_score + 3Y_returns + low_volatility
5. Return top 2
```

**Brand Recognition List:** ~50 pre-tagged household names

- Tata, Reliance, HDFC, ITC, Maruti, Infosys, Asian Paints, HUL, Bajaj, etc.
- Beginners trust names they encounter in daily life

**Why 2 stocks?**

- Reduces decision paralysis
- "Pick one of two" beats "browse and choose"
- A/B testable (1 vs 2)

---

## Voice Input

**Design principle:** Voice is first-class, not afterthought.

| Step | Voice Input | Example |
|------|-------------|---------|
| Amount | "I want to invest two thousand" | Parses → ₹2000 |
| Stock preference | "Show me Reliance" | Overrides screener |
| Confirm | "Yes, buy it" | Executes order |

**Language support:**

- Hindi numerals: "paanch hazaar" → ₹5,000
- English: "five thousand" → ₹5,000
- Mixed: "paanch thousand" → ₹5,000
- Phase 2: Marathi, Tamil, Telugu

**Always show tap alternatives.** Voice is additive, not required.

---

## Payment & Fund Transfer

**Improvements over original PRD:**

| Gap in Original | This Design |
|-----------------|-------------|
| No balance visibility | Show balance upfront |
| Deposit full amount | Smart deficit — only add what's needed |
| UPI only | UPI + Net Banking + existing balance |
| No amount guidance | "Most start with ₹500-1000" hint |

**Payment options:**

1. UPI (intent flow)
2. Net Banking
3. Existing balance (if sufficient)
4. Round-up option ("Add ₹1000 instead of ₹753")

**Saved methods:** Remember last used for repeat behavior.

---

## Funnel Comparison

| Original PRD | This Design |
|--------------|-------------|
| Home → Widget → L2 → Prompt → Stocks → Detail → Order → Deposit → Confirm | Widget → Amount+Stock → Pay+Confirm |
| **8 steps** | **3 steps** |
| Stock-first discovery | Amount-first anchor |
| AI chatbot ("ask anything") | Focused voice for amounts |
| Educational prompts | Transactional focus |

---

## Future Evolution: Text-to-Screener

Once voice is mature, extend to natural language screeners:

```
User: "Show me IT stocks under 2000"
→ Parse: sector=IT, price<2000
→ Run screener
→ Return results

User: "Companies with high profit growth"
→ Parse: profit_growth>20%
→ Run screener
→ Return results
```

This replaces the static prompts in original PRD with dynamic, user-driven queries.

---

## Success Metrics

| Metric | Current | Target |
|--------|---------|--------|
| First trade activation | 10% | 25% |
| Time to first trade | Days | <5 minutes |
| Funnel drop-off | High (8 steps) | Low (3 steps) |
| Voice usage | N/A | 15% of activations |

---

## Acceptance Criteria

1. User can complete first trade in 3 taps (no voice)
2. User can complete first trade via voice amount input
3. Stock suggestions update within 500ms of amount change
4. Payment shows accurate balance and deficit
5. Multiple payment methods available (UPI, Net Banking, balance)
6. Hindi voice input works for amounts
7. Large-cap, liquid, recognizable stocks only shown to beginners

---

## NPS & Feedback Collection

**From original PRD:** If user drops off after 30 seconds of inactivity, trigger NPS via APN or in-app.

**Proposed approach for this design:**

| Trigger | Action |
|---------|--------|
| 30-sec inactivity on Amount+Stock screen | Soft nudge: "Need help picking?" (not NPS yet) |
| User exits without completing | NPS survey via push notification (1 hour delay) |
| User completes first trade | Celebration + optional "How was this?" rating |

**Feedback collection:**

- Text or voice input supported
- Auto-categorized: bug vs feature request vs confusion
- Summary aggregated for product team

**Why delay NPS?**

- Immediate popup during hesitation feels pushy
- 1-hour delay captures reflection ("I wanted to but...")
- Higher quality feedback when not interrupting flow

**Alternative:** Keep 30-sec in-app NPS for A/B testing — measure if immediate feedback captures different insights than delayed.

---

## Open Questions

1. **Fractional shares?** If enabled, removes the "can't afford 1 share" constraint
2. **SIP nudge?** After first trade, prompt "Want to invest ₹500 monthly?"
3. **Celebration screen?** Confetti/gamification after first trade completion
4. **NPS timing?** Immediate 30-sec vs delayed 1-hour — A/B test?

---

## API Dependencies

| API | Purpose | Exists? |
|-----|---------|---------|
| Market data | Stock prices, % change | Yes |
| Screener | Filter by market cap, volume | Yes |
| Balance | User's available funds | Yes |
| Payment | UPI, Net Banking rails | Yes |
| Voice STT | Speech to text | Needs integration |
| Brand tags | Household name mapping | New (static list) |

---

## Not In Scope (YAGNI)

- AI chatbot ("ask me anything") — compliance risk, scope creep
- News integration — not needed for first trade
- F&O suggestions — focus is cash/equity beginners
- Multiple language UI — voice only for phase 1
- Social features — no sharing, leaderboards
