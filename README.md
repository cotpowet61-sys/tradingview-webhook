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
