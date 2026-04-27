class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student name:", self.name)

s1 = Student("Kaveri")
s1.display()