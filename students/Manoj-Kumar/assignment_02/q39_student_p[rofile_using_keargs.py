
def student_profile(**details):

    for key, value in details.items():
        print(key, ":", value)


student_profile(
    name="Manoj kumar",
    age=18,
    course="Python"
)