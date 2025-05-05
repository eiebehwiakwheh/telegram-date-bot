from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import ApplicationBuilder, InlineQueryHandler, ContextTypes
from uuid import uuid4
from datetime import date, timedelta
import os
import re

BOT_TOKEN = os.getenv("BOT_TOKEN")

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

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query.strip().lower()
    match = re.search(r"(easter|ash|pentecost)[^\d]*(\d{4})", query)

    if not match:
        result_text = "Type something like 'easter 2045', 'ash 2045', or 'pentecost 2045'."
    else:
        feast, year = match.group(1), int(match.group(2))
        if not (1583 <= year <= 9999):
            result_text = "Please provide a year between 1583 and 9999."
        else:
            easter = calculate_easter(year)
            if feast == "easter":
                result_text = f"Easter in {year} is on {easter.strftime('%-d %B %Y')}"
            elif feast == "ash":
                ash = easter - timedelta(days=46)
                result_text = f"Ash Wednesday_
