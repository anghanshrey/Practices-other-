print("="*40)
print("Q-1")
print("="*40)
"""
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} is login!")

    def display(self):
        print(f"Name : {self.name} | Age : {self.age}")

    def __del__(self):
        print(f"{self.name} is logout.!")

s1 = Student("Shrey" , 20)
s2 = Student("Pal" , 22)

s1.display()
s2.display()

del s1
del s2
"""

print("="*40)
print("Q-2")
print("="*40)

"""
class Animal:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Animal Name is : {self.name}")

cat = Animal("cat")

cat.display()
"""

print("="*40)
print("Q-3")
print("="*40)
"""
class Rectangle:

    def __init__(self , length = float, width = float):

        self.length = length
        self.width = width
        self.__total = 0

    def calculate(self):
        self.__total = self.length * self.width

    def display(self):
        print(f"Area of Rectangle {self.length} x {self.width} : {self.__total}")

rec = Rectangle(10, 5)

rec.calculate()

rec.display()
"""

print("="*40)
print("Q-4")
print("="*40)
"""
class Employee:
    def __init__(self):
         self.name = "Shrey"
         self.department = "IT"
         print(f"Name : {self.name} | Department : {self.department}")

    def __del__(self):
        print(f"Good Bye : {self.name}")

emp1 = Employee()

del emp1
"""

print("="*40)
print("Q-5")
print("="*40)

"""
class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name : {self.name} | Age : {self.age}")

s1 = Student("Robinson", 23)

s1.display_info()
"""
