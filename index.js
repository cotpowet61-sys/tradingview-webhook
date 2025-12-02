const express = require('express');
const axios = require('axios');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const TELEGRAM_BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN || '8329085403:AAH5DCLhjdM--YJgMxxqRFj9qo3ZKwSSTNM';
const TELEGRAM_CHAT_ID = process.env.TELEGRAM_CHAT_ID || '5751308265';

app.post('/webhook', async (req, res) => {
  try {
    const message = req.body.message || JSON.stringify(req.body);
    
    const telegramMessage = `TradingView Alert:\n${message}`;
    
    await axios.post(
      `https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`,
      {
        chat_id: TELEGRAM_CHAT_ID,
        text: telegramMessage,
        parse_mode: 'Markdown'
      }
    );
    
    console.log('Message sent to Telegram');
    res.status(200).json({ status: 'ok' });
  } catch (error) {
    console.error('Error:', error.message);
    res.status(500).json({ error: error.message });
  }
});

app.get('/', (req, res) => {
  res.status(200).send('Webhook ready');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
