import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        if int(row[1]) > 50:   # second column
            print(row)