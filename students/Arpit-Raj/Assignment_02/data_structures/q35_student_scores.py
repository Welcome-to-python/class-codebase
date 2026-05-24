students = {

    "Rahul": {
        "math": 90,
        "science": 85,
        "english": 88
    },

    "Aditya": {
        "math": 70,
        "science": 75,
        "english": 80
    },

    "Arpit": {
        "math": 95,
        "science": 92,
        "english": 89
    }
}

student_name = "Arpit"

scores = students[student_name].values()

average = sum(scores) / len(scores)

print("Average Score:", average)