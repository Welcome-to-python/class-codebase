def student_profile(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")


student_profile(
    name="Sahil",
    age=19,
    course="CSE"
)
