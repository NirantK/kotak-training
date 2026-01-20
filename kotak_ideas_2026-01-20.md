# Kotak Securities - Agentic Ideas Analysis
**Date:** 2026-01-20
**Status:** ✅ Complete (5/5 ideas collected)

---

## Idea #1: Idea for ScaledFocus Training (Neo Watchlist Bridge)

**From:** rhiddhijit ghosh (Product, KSL) <rhiddhijit.ghosh@kotak.com>
**Date:** 2026-01-20T05:14:45Z
**Message ID:** 19bd9d3b35814d9c

### Completeness Check

| Section | Status | Details |
|---------|--------|---------|
| **WHO** | ✓ Present | Users who collect information from multiple non-Neo sources and place orders on Neo |
| **WHY** | ✓ Present | Users read news/WhatsApp/Instagram but have to manually search for stocks on Neo App. No bridge between non-Neo content and Neo watchlist. Users get distracted from stocks they started following. |
| **WHAT/HOW** | ✓ Present | Users can share screenshots or news article URLs with Neo which will add stocks to watchlist and keep user updated about that scrip |

### Agentic Mapping

| Component | Status | Details |
|-----------|--------|---------|
| **Router** | ✓ Identified | Input type detection (screenshot vs URL) |
| **Orchestrator** | ✓ Identified | Coordinates between content parsing, stock identification, and watchlist management |
| **Sub-agents** | ✓ Identified | Image/URL parser, Stock entity extractor, Watchlist manager, Notification system |
| **HITL** | ✗ Not identified | No explicit human approval points mentioned |

### Action Taken
**Status:** COMPLETE - No reply needed (all sections present)

---

## Idea #2: Zinder (Social Connection App)

**From:** nishant sachdeva (Product, KSL) <nishant.sachdeva@kotak.com>
**Date:** 2026-01-20T05:14:39Z
**Message ID:** 19bd9d39e8db0629

### Completeness Check

| Section | Status | Details |
|---------|--------|---------|
| **WHO** | ✓ Present | Adults who are socially motivated but lack access to like-minded communities - young professionals in new cities, people rediscovering interests after life transitions, activity enthusiasts without partners |
| **WHY** | ✓ Present | Loneliness has reached epidemic levels affecting mental/physical health. Traditional friend-making structures have eroded. People struggle to form meaningful friendships and find companions for activities. |
| **WHAT/HOW** | ✗ Missing | Problem statement and target audience defined, but no technical solution or implementation approach provided |

### Agentic Mapping

| Component | Status | Details |
|-----------|--------|---------|
| **Router** | ✗ Not identified | No routing logic described |
| **Orchestrator** | ✗ Not identified | No workflow coordination described |
| **Sub-agents** | ✗ Not identified | No specialized tools/agents described |
| **HITL** | ✗ Not identified | No human approval points mentioned |

### Action Taken
**Status:** REPLY NEEDED - Missing WHAT/HOW section (solution approach)

---

## Idea #3: AI Agent for Simplified Stock Chart Interpretation

**From:** akhilesh chobey (Product, KSL) <akhilesh.chobey@kotak.com>
**Date:** 2026-01-20T05:11:12Z
**Message ID:** 19bd9d09492b100b

### Completeness Check

| Section | Status | Details |
|---------|--------|---------|
| **WHO** | ✓ Present | First-time and early-stage equity investors who actively view stock charts but lack understanding of candlestick charts, patterns, and price-movement rationale. Scope limited to equity stocks only. |
| **WHY** | ✓ Present | New investors are curious about stock price movements but candlestick patterns are difficult to interpret, concepts like OHLC/volume/trends feel overwhelming, and users lack contextual explanations connecting chart movement with news/events. This leads to confusion, misinterpretation, or disengagement. |
| **WHAT/HOW** | ✓ Present | Smart AI Agent that accepts chart images or stock symbols, detects candlestick patterns, overlays contextual tooltips, and summarizes relevant news explaining price movement. Acts as a learning companion without trading recommendations. |

### Agentic Mapping

| Component | Status | Details |
|-----------|--------|---------|
| **Router** | ✓ Identified | Input type detection (chart image vs stock symbol/name) |
| **Orchestrator** | ✓ Identified | Coordinates between image analysis, pattern detection, and news retrieval |
| **Sub-agents** | ✓ Identified | Chart image analyzer, Pattern detector, News summarizer, Tooltip generator |
| **HITL** | ✗ Not identified | No explicit human approval points mentioned |

### Action Taken
**Status:** COMPLETE - No reply needed (all sections present)

---

## Idea #4: Kotak IPO Live-Scout

**From:** sankalp parab (Innovation Lab, KSL) <sankalp.parab@kotak.com>
**Date:** 2026-01-20T05:19:34Z
**Message ID:** 19bd9d81e0cfddb1

### Completeness Check

| Section | Status | Details |
|---------|--------|---------|
| **WHO** | ✗ Weak | "Retail investors" mentioned in passing but no explicit user persona definition. Who specifically? First-time IPO investors? Experienced traders? What's their current behavior? |
| **WHY** | ✓ Present | Solves "analysis paralysis" by giving investors clear, data-backed summaries. Guides users through essential IPO concepts and market sentiment. |
| **WHAT/HOW** | ✓ Present | Embedded AI agent on Kotak Neo IPO page using live web search to aggregate Strengths, Risks, and Grey Market Premium (GMP), generating real-time insights. |

### Agentic Mapping

| Component | Status | Details |
|-----------|--------|---------|
| **Router** | ✓ Identified | Could route between IPO name input vs general query |
| **Orchestrator** | ✓ Identified | Coordinates web search, data aggregation, and insight generation |
| **Sub-agents** | ✓ Identified | Web search agent, GMP aggregator, Strengths analyzer, Risk analyzer, Insight generator |
| **HITL** | ✗ Not identified | No explicit human approval points mentioned |

### Action Taken
**Status:** REPLIED - Requested WHO section clarification (target user persona)

---

## Summary

| # | Idea | Sender | WHO | WHY | WHAT | Action |
|---|------|--------|-----|-----|------|--------|
| 1 | Neo Watchlist Bridge | rhiddhijit ghosh | ✓ | ✓ | ✓ | None |
| 2 | Zinder | nishant sachdeva | ✓ | ✓ | ✗ | Replied |
| 3 | Stock Chart Interpreter | akhilesh chobey | ✓ | ✓ | ✓ | None |
| 4 | IPO Live-Scout | sankalp parab | ✗ | ✓ | ✓ | Replied |

---

## Idea #5: Margin Queries (Margin Support Chatbot)

**From:** pankhudi jain (Product, KSL) <pankhudi.jain@kotak.com>
**Date:** 2026-01-20T05:22:32Z
**Message ID:** 19bd9dadc6f178aa

### Completeness Check

| Section | Status | Details |
|---------|--------|---------|
| **WHO** | ✓ Present | End customers of Kotak Neo who rely on margin for trading and face discrepancies. Typically active traders who are time-sensitive and margin-dependent. |
| **WHY** | ✓ Present | Margin issues block trades causing financial opportunity loss. Users need clarity ("why different from expected?"), diagnosis ("system delay or my issue?"), actionability ("what to do now?"), and transparency (simple explanations without jargon). |
| **WHAT/HOW** | ✓ Present | Margin Support Chatbot as single explanation/resolution layer. Understands NL queries, fetches real-time margin context, explains using standardized reason codes, provides next-best action with ETAs, reduces support contacts. |

### Agentic Mapping

| Component | Status | Details |
|-----------|--------|---------|
| **Router** | ✓ Identified | Intent classification for query types: "margin not showing", "order rejected", "margin reduced", "when will margin update" |
| **Orchestrator** | ✓ Identified | Coordinates query understanding → margin data fetch → reason code matching → action recommendation |
| **Sub-agents** | ✓ Identified | NLU for margin queries, Margin data fetcher, Reason code explainer, Action recommender, Support ticket creator |
| **HITL** | ✓ Identified | "Raise a support ticket with prefilled context if not resolved" - explicit escalation to human support |

### Action Taken
**Status:** COMPLETE - No reply needed (all sections present, excellent structure)

---

## Summary

| # | Idea | Sender | WHO | WHY | WHAT | Action |
|---|------|--------|-----|-----|------|--------|
| 1 | Neo Watchlist Bridge | rhiddhijit ghosh | ✓ | ✓ | ✓ | None |
| 2 | Zinder | nishant sachdeva | ✓ | ✓ | ✗ | Replied |
| 3 | Stock Chart Interpreter | akhilesh chobey | ✓ | ✓ | ✓ | None |
| 4 | IPO Live-Scout | sankalp parab | ✗ | ✓ | ✓ | Replied |
| 5 | Margin Support Chatbot | pankhudi jain | ✓ | ✓ | ✓ | None |

**✅ MONITORING COMPLETE - 5/5 ideas collected**

