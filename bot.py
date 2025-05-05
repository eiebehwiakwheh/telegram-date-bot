import os
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

from weeks_after_easter import time_since_easter  # Import logic from separate file

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = datetime.now().date()
    today_str = today.strftime('%d.%m.%Y')

    # Get message from external file logic
    relative_msg = time_since_easter(today)

    # Send two separate replies
    await update.message.reply_text(today_str)
    await update.message.reply_text(relative_msg)

if __name__ == '__main__':
    token = os.getenv('BOT_TOKEN')  # Read token from Railway env vars
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
