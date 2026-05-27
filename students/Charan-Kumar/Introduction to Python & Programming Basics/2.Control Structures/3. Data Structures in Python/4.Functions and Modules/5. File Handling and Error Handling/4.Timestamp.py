from datetime import datetime

entry = input("Enter your journal entry: ")

time = datetime.now()

with open("log.txt", "a") as file:
    file.write(f"{time} - {entry}\n")

print("Entry added to log.txt")