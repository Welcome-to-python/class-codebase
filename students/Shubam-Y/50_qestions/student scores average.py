students = {
    "Karthik": {"math": 80, "science": 90},
    "Rahul": {"math": 70, "science": 85},
    "Anu": {"math": 95, "science": 88}
}

name = input()

scores = students[name]

avg = sum(scores.values()) / len(scores)

print(avg)