# ai-bot-experiment

A simple single-instance Telegram bot, deployed on Railway.

## Deploy to Railway

1. **Push this repo to GitHub**

2. **Create a new project on [Railway](https://railway.app)**
   - New Project → Deploy from GitHub repo → select this repo

3. **Add environment variable:**
   - Go to your service → Variables
   - Add `BOT_TOKEN` = your token from [@BotFather](https://t.me/BotFather)

4. **Railway will auto-deploy.** Check logs to confirm:
   ```
   ✅ ai-bot-experiment is running...
   ```

## Redeploy (clean restart)

To avoid polling conflicts, always redeploy via Railway dashboard:
- Go to your service → Deployments → **Redeploy**
- This cleanly stops the old instance before starting the new one

## Commands

| Command | Description       |
|---------|-------------------|
| /start  | Start the bot     |
| /help   | Show help message |
