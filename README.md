# TradingView Webhook to Telegram

Webhook server that receives alerts from TradingView and forwards them to Telegram.

## Setup

1. Install dependencies: `npm install`
2. Set environment variables:
   - `TELEGRAM_BOT_TOKEN` - Your Telegram bot token
   - `TELEGRAM_CHAT_ID` - Your Telegram chat ID

3. Start server: `npm start`

## Usage

Send POST requests to `/webhook` with message in body:

```json
{
  "message": "Your trading signal here"
}
```

The message will be forwarded to your Telegram chat.

## Deployment to Vercel

1. Connect GitHub repo to Vercel
2. Add environment variables in Vercel dashboard
3. Deploy automatically on push

## Quick Start - TradingView Alerts to Telegram

**Webhook URL**: `https://tradingview-webhook-cotpowet61.replit.dev/webhook`

1. Open TradingView chart (e.g., AVAXUSDT on Bybit)
2. Click **Alert** button
3. Set your conditions (Price crossing, RSI, etc.)
4. Go to **Notifications** tab
5. For **FREE** users:
   - Use **Email** notifications
   - System will forward to Telegram automatically
6. For **Premium** users:
   - Enable **Webhook URL** in Notifications
   - Add message: `{"message": "SIGNAL {{ticker}}: {{close}}"}`

## Trading Signals Format

```
📊 Signal: {{ticker}}
💰 Price: {{close}}
📈 Time: {{interval}}
```

All signals are automatically sent to Telegram for manual trading on Bybit.

**Bot Token**: 8329085403:AAH5DCLhjdM--YJgMxxqRFj9qo3ZKwSSTNM
**Chat ID**: 5751308265
