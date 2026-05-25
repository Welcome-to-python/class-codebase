import csv

path = r"D:\Workspace\Python_of_Classmates\pavan_python\class-codebase\students\PavanVastrad\Assignment_02\file_handling\data.csv"

with open(path, "r") as file:

    reader = csv.reader(file)

    for row in reader:

        if int(row[1]) > 50:

            print(row)