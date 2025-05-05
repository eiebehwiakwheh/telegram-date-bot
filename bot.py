import os
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

async def reply_with_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = datetime.now().strftime('%d.%m.%Y')
    await update.message.reply_text(today)

if __name__ == '__main__':
    app = ApplicationBuilder().token(os.environ['BOT_TOKEN']).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply_with_date))
    app.run_polling()
