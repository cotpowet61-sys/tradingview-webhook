#!/usr/bin/env python3
import os
import json
import requests
from datetime import datetime

# Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '8329085403:AAH5DCLhjdM--YJgMxxqRFj9qo3ZKwSSTNM')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '5751308265')
WEBHOOK_URL = 'https://tradingview-webhook-cotpowet61.replit.dev/webhook'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'

def send_to_telegram(message):
    """Send message to Telegram"""
    try:
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown'
        }
        response = requests.post(TELEGRAM_API_URL, json=payload)
        print(f'Telegram response: {response.status_code}')
        return response.status_code == 200
    except Exception as e:
        print(f'Error sending to Telegram: {e}')
        return False

def parse_tradingview_alert(email_text):
    """Extract signal from TradingView email"""
    # Parse email subject and body
    if 'SIGNAL' in email_text or 'Alert' in email_text:
        return email_text
    return None

def main():
    # Test message
    test_message = "📊 TradingView Signal Received\n" \
                   "🔔 Alert System Active\n" \
                   "✅ Webhook Connected\n" \
                   "Time: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
    
    send_to_telegram(test_message)
    print('Email to Telegram service started')

if __name__ == '__main__':
    main()
