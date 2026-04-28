class Student:

    def _init_(self, name):
        self.name = name
    def display(self):
        print("Student Name:", self.name)

obj = Student("Lakshmi")

obj.display()