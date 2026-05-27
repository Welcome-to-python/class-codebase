
from datetime import datetime

entry = input("Enter note: ")

file = open("log.txt", "a")

file.write(str(datetime.now()))
file.write(" - ")
file.write(entry)
file.write("\n")

file.close()

print("Saved")