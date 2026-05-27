students = {
    "John": {"Math": 80, "Science": 90, "English": 85},
    "Alice": {"Math": 75, "Science": 95, "English": 88},
    "Bob": {"Math": 70, "Science": 82, "English": 78}
}

name = "Alice"

scores = students[name].values()

avg = sum(scores) / len(scores)

print("Average score of", name, "=", avg)