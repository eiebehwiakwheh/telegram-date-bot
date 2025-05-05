import os
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# Easter and target date calculation
def compute_target_date(year):
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
    easter = datetime(year, month, day)
    target = easter + timedelta(days=15)
    return f"{target.strftime('%d.%m.%Y')}\nMonday after the second Sunday after Easter"

# Telegram message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    year = datetime.now().year
    msg = compute_target_date(year)
    await update.message.reply_text(msg)

# Main app
if __name__ == "__main__":
    token =
