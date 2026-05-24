from datetime import date


today = date.today()

birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month: "))
birth_day = int(input("Enter birth day: "))

next_birthday = date(today.year, birth_month, birth_day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birth_month, birth_day)

difference = next_birthday - today

print("Days until next birthday:", difference.days)