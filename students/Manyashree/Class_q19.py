class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name =", self.name)

s1 = Student("Ravi")
s1.display()
