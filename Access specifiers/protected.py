class Student:
    def __init__(self):
        self._name = "Rahul"
class Demo(Student):
    def display(self):
        print(self._name)

d = Demo()
d.display()
