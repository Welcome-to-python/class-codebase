import csv

file = open("data.csv", "r")

reader = csv.reader(file)

for row in reader:
    if int(row[1]) > 50:
        print(row)

file.close()
