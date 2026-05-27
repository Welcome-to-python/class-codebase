def student_profile(**kwargs):
    print("Student Profile")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# Function call
student_profile(
    Name="Charan",
    Age=18,
    Course="CSE",
    Grade="A"
)