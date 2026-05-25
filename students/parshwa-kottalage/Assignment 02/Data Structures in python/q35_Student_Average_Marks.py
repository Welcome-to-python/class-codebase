
students = {
    "Ram": [80, 85, 90],
    "Shyam": [70, 75, 80],
    "Ravi": [60, 65, 70]
}

name = input("Enter student name: ")

marks = students[name]

average = sum(marks) / len(marks)

print("Average Marks =", average)