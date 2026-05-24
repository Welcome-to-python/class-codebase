from datetime import date


birth_month = int(input("Enter birth month: "))
birth_day = int(input("Enter birth day: "))

today = date.today()

next_birthday = date(
    today.year,
    birth_month,
    birth_day
)

if next_birthday < today:

    next_birthday = date(
        today.year + 1,
        birth_month,
        birth_day
    )

remaining_days = (next_birthday - today).days

print("Days until next birthday:", remaining_days)
