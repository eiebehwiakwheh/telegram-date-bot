from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def date_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now()
    date_str = now.strftime("%A, %d %B %Y")
    await update.message.reply_text(f"📅 Today's date is: {date_str}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("date", date_command))
    app.run_polling()

if __name__ == "__main__":
    main()
