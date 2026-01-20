# First Trade Activation: Functional Specification

> Engineering spec for Amount-First First Trade feature

---

## 1. Technical Architecture

| Layer | Technology | Notes |
|-------|------------|-------|
| Mobile | Flutter | Shared codebase, platform channels for native features |
| Backend | Microservices | Separate services for market data, wallet, orders |
| Voice | Azure Speech | Hindi + English STT, pay-per-use |
| Payments | Juspay + Razorpay + Kotak Bank | Orchestration layer with multiple rails |
| Analytics | Firebase + Mixpanel + CleverTap | Instrument all three for funnel tracking |

---

## 2. Feature Components

### 2.1 Home Widget

**Visibility Rules:**

- Show only to users with `first_trade_completed = false`
- Account age < 30 days
- Hide permanently after first trade is placed

**Widget Data:**

```dart
class FirstTradeWidget {
  final String userName;        // From user profile
  final int suggestedAmount;    // Default ₹500
  final bool isVisible;         // Based on first_trade_completed flag
}
```

**API Call:** None (uses cached user profile)

---

### 2.2 Amount + Stock Selection Screen

**Amount Picker:**

- Preset buttons: ₹500, ₹1000, ₹2000, ₹5000, Custom
- Voice input button → Azure Speech STT
- Voice languages: Hindi ("paanch hazaar"), English ("five thousand"), Mixed

**Voice Integration:**

```dart
// Azure Speech SDK integration
class VoiceAmountParser {
  Future<int?> parseAmount(String transcript) {
    // Handle: "paanch hazaar" → 5000
    // Handle: "five thousand" → 5000
    // Handle: "paanch thousand" → 5000
  }
}
```

**Stock Screener Request:**

```json
POST /api/v1/screener/beginner-stocks
{
  "max_price": 1000,
  "min_market_cap_cr": 50000,
  "min_daily_volume": 1000000,
  "limit": 2
}
```

**Stock Ranking (Client-side):**

```dart
// Static brand recognition scores (in-app)
const Map<String, int> brandScores = {
  'TATAMOTORS': 10, 'RELIANCE': 10, 'HDFCBANK': 10,
  'INFY': 9, 'TCS': 9, 'ITC': 9, 'MARUTI': 9,
  'ASIANPAINT': 8, 'HUL': 8, 'BAJFINANCE': 8,
  // ... ~50 household names
};

// Final ranking = brand_score + (3Y_return_percentile * 0.3) - (volatility_percentile * 0.2)
```

**No Results Handling:**

- If screener returns empty for amount < ₹500:
- Show: "Start with at least ₹500 to see stock options"
- Auto-suggest ₹500 button highlighted

**Price Updates:**

- Poll every 30 seconds via REST
- No WebSocket for this screen

---

### 2.3 Payment + Confirm Screen

**Balance Check:**

```
GET /api/v1/wallet/balance
Response: { "available_balance": 247.00, "currency": "INR" }
```

**Deficit Calculation:**

```dart
class PaymentCalculator {
  final double orderAmount;
  final double availableBalance;

  double get deficit => max(0, orderAmount - availableBalance);
  double get roundUpAmount => (orderAmount / 500).ceil() * 500;
}
```

**Payment Options (in priority order):**

1. Existing balance (if sufficient) → Skip payment step
2. Kotak Bank direct transfer
3. UPI via Juspay/Razorpay
4. Net Banking via Juspay/Razorpay

**Payment Request:**

```
POST /api/v1/payments/initiate
{
  "amount": 753.00,
  "method": "upi" | "netbanking" | "kotak_transfer",
  "purpose": "first_trade_deposit"
}
```

---

### 2.4 Order Placement

**Order Type:**

- User chooses: Market or Limit
- Default: Market order (simpler for beginners)

**Market Hours Logic:**

```dart
bool isMarketOpen() {
  final now = DateTime.now();
  final marketOpen = TimeOfDay(hour: 9, minute: 15);
  final marketClose = TimeOfDay(hour: 15, minute: 30);
  // Also check: not Saturday/Sunday, not NSE holiday
}

OrderType getOrderType(OrderType userChoice) {
  if (isMarketOpen()) return userChoice;
  return OrderType.AMO;  // Auto-switch to After Market Order
}
```

**Order Request:**

```
POST /api/v1/orders/place
{
  "symbol": "TATAMOTORS",
  "exchange": "NSE",
  "quantity": 1,
  "order_type": "MARKET" | "LIMIT" | "AMO",
  "transaction_type": "BUY",
  "price": null,
  "is_first_trade": true
}
```

**Success Response:**

```
{
  "order_id": "ORD123456",
  "status": "PLACED" | "EXECUTED",
  "symbol": "TATAMOTORS",
  "quantity": 1,
  "average_price": 947.50
}
```

---

### 2.5 Success Screen

**Post-Trade Actions:**

1. Show order confirmation (order ID, stock, quantity, price)
2. Mark `first_trade_completed = true` → hides widget permanently
3. Trigger celebration animation
4. Optional: Show SIP prompt ("Want to invest ₹500 monthly?")

**Analytics Events:**

```dart
// Fire to all 3 platforms
analytics.logEvent('first_trade_completed', {
  'amount': 1000,
  'stock': 'TATAMOTORS',
  'payment_method': 'upi',
  'voice_used': false,
  'time_to_complete_seconds': 45,
});
```

---

## 3. API Contracts

### 3.1 Screener API

```
GET /api/v1/screener/stocks
Query params:
  - max_price: number (required)
  - min_market_cap_cr: number (default: 50000)
  - min_daily_volume: number (default: 1000000)
  - limit: number (default: 2)

Response:
{
  "stocks": [
    {
      "symbol": "TATAMOTORS",
      "name": "Tata Motors Ltd",
      "ltp": 947.50,
      "change_percent": 2.3,
      "market_cap_cr": 350000,
      "avg_volume": 15000000
    }
  ]
}
```

### 3.2 Voice STT (Azure Speech)

```dart
// Flutter package: azure_speech_recognition
final speechConfig = SpeechConfig.fromSubscription(
  subscriptionKey: AZURE_SPEECH_KEY,
  region: 'centralindia'
);

speechConfig.speechRecognitionLanguage = 'hi-IN';  // or 'en-IN'

// Handle mixed language with phrase list hints
phraseList.addPhrase('paanch hazaar');
phraseList.addPhrase('das hazaar');
```

### 3.3 Payment Initiation (Juspay)

```
POST /api/v1/payments/initiate
Body:
{
  "amount": 753.00,
  "method": "upi",
  "customer_id": "USR123",
  "order_id": "FIRST_TRADE_123"
}

Response:
{
  "payment_id": "PAY123",
  "status": "PENDING",
  "upi_intent_url": "upi://pay?...",
  "redirect_url": "https://..."
}
```

---

## 4. State Management

```dart
// Riverpod providers
final firstTradeStateProvider = StateNotifierProvider<FirstTradeNotifier, FirstTradeState>((ref) {
  return FirstTradeNotifier(ref);
});

class FirstTradeState {
  final int? selectedAmount;
  final List<Stock> suggestedStocks;
  final Stock? selectedStock;
  final double walletBalance;
  final PaymentMethod? selectedPaymentMethod;
  final OrderType orderType;
  final FirstTradeStep currentStep;
  final bool isLoading;
  final String? error;
}

enum FirstTradeStep {
  amountSelection,
  stockSelection,
  payment,
  confirmation,
  success
}
```

---

## 5. Analytics Events

| Event | Trigger | Properties |
|-------|---------|------------|
| `first_trade_widget_shown` | Widget appears on home | user_id, account_age_days |
| `first_trade_widget_tapped` | User taps widget | user_id |
| `amount_selected` | User picks amount | amount, method (tap/voice) |
| `voice_input_started` | User taps mic | user_id |
| `voice_input_success` | Voice parsed successfully | transcript, parsed_amount, language |
| `voice_input_failed` | Voice parsing failed | transcript, error |
| `stock_selected` | User taps stock card | symbol, price, rank |
| `payment_initiated` | Payment flow started | amount, method |
| `payment_completed` | Payment successful | amount, method, duration_ms |
| `payment_failed` | Payment failed | amount, method, error |
| `order_placed` | Order submitted | symbol, quantity, order_type, is_amo |
| `first_trade_completed` | Order confirmed | full order details |
| `first_trade_abandoned` | User exits without completing | last_step, time_spent_seconds |

---

## 6. Error States

| Scenario | User Message | Action |
|----------|--------------|--------|
| Screener API fails | "Unable to load stocks. Tap to retry." | Retry button |
| Amount too low | "Start with at least ₹500 to see options" | Highlight ₹500 button |
| Voice parsing fails | "Didn't catch that. Try again or tap an amount." | Show tap options |
| Payment fails | "Payment failed. Try again or use a different method." | Show payment options |
| Order fails | "Order could not be placed. [Error details]" | Retry or contact support |
| Market closed | "Markets are closed. Your order will execute tomorrow at 9:15 AM." | Informational, proceed with AMO |
| Insufficient balance | "Add ₹[X] to place this order" | Show payment options |

---

## 7. Security Considerations

- All API calls over HTTPS
- Payment tokens never stored on device
- Voice recordings not persisted (streamed to Azure, discarded)
- Order placement requires active session token
- Rate limit voice requests (max 10/minute)

---

## 8. Testing Checklist

### Unit Tests

- Amount parser (voice transcripts → amounts)
- Brand score ranking algorithm
- Deficit calculator
- Market hours detection
- AMO auto-switch logic

### Integration Tests

- Screener API → Stock card rendering
- Payment flow → Order placement
- Voice → Amount selection → Stock update

### E2E Tests

- Happy path: Widget → Amount → Stock → Pay → Success
- Voice path: Widget → Voice amount → Stock → Pay → Success
- Edge: Low amount → Minimum suggestion → Proceed
- Edge: Off-hours → AMO warning → Proceed
- Edge: Sufficient balance → Skip payment → Confirm

---

## 9. Open Items for Backend Team

1. Confirm screener API supports `max_price` filter
2. Confirm wallet API returns real-time balance
3. Add `is_first_trade` flag to order API for analytics
4. Endpoint to mark `first_trade_completed` on user profile

---

## 10. Dependencies

| Dependency | Owner | Status |
|------------|-------|--------|
| Azure Speech subscription | Platform team | Needed |
| Screener API filter support | Market data team | Confirm |
| Juspay integration | Payments team | Exists |
| Analytics SDK setup | Mobile team | Exists |
| User profile `first_trade_completed` flag | Backend team | Needed |
