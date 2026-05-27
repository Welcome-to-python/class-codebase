from datetime import date

# User input
year = int(input("Enter birth year: "))
month = int(input("Enter birth month: "))
day = int(input("Enter birth day: "))

today = date.today()

# Next birthday
next_birthday = date(today.year, month, day)

if next_birthday < today:
    next_birthday = date(today.year + 1, month, day)

days_left = (next_birthday - today).days

print("Days until next birthday:", days_left)