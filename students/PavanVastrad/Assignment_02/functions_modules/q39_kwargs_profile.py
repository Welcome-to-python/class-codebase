def student_profile(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")


student_profile(
    name="pavan",
    age=19,
    course="CSE"
)
