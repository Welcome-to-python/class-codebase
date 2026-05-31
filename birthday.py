import datetime
today = datetime.date.today()
birthday = datetime.date(today.year, 12, 25)  # example
if birthday < today:
    birthday = datetime.date(today.year+1, 12, 25)
print((birthday - today).days)
