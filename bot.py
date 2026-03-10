import os
import logging
import anthropic
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize Anthropic client
claude = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! I'm ai-bot-experiment, powered by Claude.\n\nSend me any message and I'll respond!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n"
        "/start - Start the bot\n"
        "/help  - Show this message\n\n"
        "Just send any message to chat with Claude!"
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    logger.info(f"User ({update.effective_user.id}): {user_message}")

    # Show typing indicator while waiting for Claude
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action="typing"
    )

    try:
        response = claude.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.content[0].text
    except Exception as e:
        logger.error(f"Claude API error: {e}")
        reply = "Sorry, I couldn't get a response from Claude. Please try again."

    logger.info(f"Claude: {reply}")
    await update.message.reply_text(reply)


def main():
    BOT_TOKEN = os.environ["BOT_TOKEN"]

    app = ApplicationBuilder() \
        .token(BOT_TOKEN) \
        .build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    logger.info("✅ ai-bot-experiment is running with Claude...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
