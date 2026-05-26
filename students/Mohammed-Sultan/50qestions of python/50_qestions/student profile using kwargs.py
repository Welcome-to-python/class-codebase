def profile(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)

profile(name="Karthik", age=20, course="Python")
