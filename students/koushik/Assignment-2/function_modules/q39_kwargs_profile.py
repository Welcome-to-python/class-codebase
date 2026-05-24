def student_profile(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)


student_profile(
    name="Kaushik",
    age=20,
    course="Python"
)