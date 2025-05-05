from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from datetime import date
import os
import re

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Set in Railway or .env

# Calculate Easter (Gregorian calendar)
def calculate_easter(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return date(year, month, day)

# Respond only to "Easter YYYY"
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    match = re.match(r"^Easter (\d{4})$", text)
    if match:
        year = int(match.group(1))
        if 1583 <= year <= 9999:
            easter = calculate_easter(year)
            await update.message.reply_text(f"Easter in {year} is on {easter.strftime('%-d %B %Y')}")
        else:
            await update.message.reply_text("Please provide a year between 1583 and 9999.")
    # No response otherwise

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
