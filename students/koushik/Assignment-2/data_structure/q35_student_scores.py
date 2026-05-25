students = {
    "Rahul": {"math": 80, "science": 75},
    "Anu": {"math": 90, "science": 85},
    "Kaushik": {"math": 88, "science": 92}
}

name = input("Enter student name: ")

scores = students[name]

average = sum(scores.values()) / len(scores)

print("Average Score:", average)
