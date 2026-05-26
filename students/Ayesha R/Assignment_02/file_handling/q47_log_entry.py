from datetime import datetime


entry = input("Enter journal entry: ")

current_time = datetime.now()

with open("log.txt", "a") as file:

    file.write(f"{current_time} - {entry}\n")

print("Entry saved")
