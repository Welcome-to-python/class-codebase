
from datetime import date

birth_month = int(input("Enter birth month: "))
birth_day = int(input("Enter birth day: "))

today = date.today()

birthday = date(today.year, birth_month, birth_day)

days = (birthday - today).days

print("Days left =", days)