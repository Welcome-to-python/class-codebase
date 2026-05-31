import datetime
entry = input("Enter log entry: ")
with open("log.txt","a") as f:
    f.write(f"{datetime.datetime.now()}: {entry}\n")
