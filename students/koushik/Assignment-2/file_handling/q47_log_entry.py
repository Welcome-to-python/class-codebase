from datetime import datetime

entry = input("Enter your journal entry: ")

file = open("log.txt", "a")

time = datetime.now()

file.write(f"{time} - {entry}\n")

file.close()

print("Log entry added.")