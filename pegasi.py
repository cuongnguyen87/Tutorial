class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname = str(firstname)
        self.lastname = str(lastname)
        self.age = int(age)
class Student(Person):
    def __init__(self,ID):
        self.ID = int(ID)

    def display(self):
        print(self.ID)
        print(self.lastname)
        print(self.firstname)
        print(self.age)

p1 = Student(Person('cuong','nguyen',32))
print(p1.display())
