from datetime import datetime, timedelta

def easter_date(year):
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
    return datetime(year, month, day)

def time_since_easter():
    today = datetime.now().date()
    easter = easter_date(today.year).date()
    delta = today - easter

    if delta.days < 0:
        return f"Easter is in {-delta.days} days."

    weeks = delta.days // 7
    days = delta.days % 7

    if weeks == 0:
        return f"{days} day{'s' if days != 1 else ''} after Easter"
    if days == 0:
        return f"{weeks} week{'s' if weeks != 1 else ''} after Easter"
    return f"{weeks} week{'s' if weeks != 1 else ''} and {days} day{'s' if days != 1 else ''} after Easter"

if __name__ == "__main__":
    print(time_since_easter())
