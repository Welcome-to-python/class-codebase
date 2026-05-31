import csv
with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if int(row[1]) > 50