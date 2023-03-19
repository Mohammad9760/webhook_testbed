import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


TOKEN = "5772643402:AAGCk43NQFjIAoKcLTEDfo0bCUQtluAwNiI"
PORT = int(os.environ.get('PORT', '8443'))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str.upper(update.message.text))

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start, block=False))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), message, block=False))

    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        secret_token='ASecretTokenIHaveChangedByNow',
        webhook_url="https://<appname>.herokuapp.com/"
    )
