from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from datetime import date
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Set this in Railway or your .env file

# Function to calculate Easter (Western)
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

# Respond to any numeric year
async def respond_year(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text.isdigit():
        year = int(text)
        if 1583 <= year <= 9999:
            easter = calculate_easter(year)
            await update.message.reply_text(f"Easter in {year} is on {easter.strftime('%-d %B %Y')}")
        else:
            await update.message.reply_text("Please send a valid year (1583–9999).")
    else:
        await update.message.reply_text("Send a year like '2045' to get the Easter date.")

# Main bot setup
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond_year))
    app.run_polling()

if __name__ == "__main__":
    main()
