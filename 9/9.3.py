print(":-"*40)
print("Q-1")
print(":-"*40)

"""
class parent:
    def display(self):
        print("parent class.")

class Child(parent):
    def display(self):
        print("child class.")
        parent.display(self)

c1 = Child()

c1.display()
"""

print(":-"*40)
print("Q-2")
print(":-"*40)

"""
class Teacher:
    def teaching(self):
        print("teaching the student.")

class Administrator:
    def manage(self):
        print("manageing the School.")

class headmaster(Teacher , Administrator):
    def services(self):
        print("services avalibe")
        Teacher.teaching(self)
        Administrator.manage(self)

head = headmaster()

head.services()
"""

print(":-"*40)
print("Q-3")
print(":-"*40)
"""
class Grandparent:
    def role(self):
        print("Time pass")

class parent(Grandparent):
    def resposibilty(self):
        print("Working....")

class Child(parent):
    def study(self):
        print("studying....")

c1 = Child()

c1.study()
c1.resposibilty()
c1.role()
"""

print(":-"*40)
print("Q-4")
print(":-"*40)

"""
class Animal:
    def eat(self):
        print("Animal eating.")

class dog(Animal):
    def sound(self):
        print("dhow.....dhow........")

class cat(Animal):
    def sound(self):
        print("meow....meow......")

d = dog()
c = cat()

d.sound()
d.eat()

c.sound()
c.eat()
"""

print(":-"*40)
print("Q-5")
print(":-"*40)
"""
class car:
    def start(self):
        print("car is Starting.....")

class bike(car):
    def start(self):
        super().start()
        print("Bike is Starting.....")

class cycle(car):
    def start(self):
        super().start()
        print("cycle is Starting.......")

class serach(bike , cycle):

    def start(self):
        super().start()
        print("Starting all vehicals.")

s = serach()

s.start()
"""

print(":-"*40)
print("Q-6")
print(":-"*40)
"""
class Student:
    def __init__(self , name):
        self.name = name
        print(f"{self.name} Welcome.")

    def display(self):
        print("Hello , Student.")

class child(Student):
    def display(self):
        super().display()
        print("Hello , Child.")

c1 = child("Shrey")

print(type(c1))
"""

print(":-"*40)
print("Q-7")
print(":-"*40)
"""
class car:
    def __init__(self , name):
        self.name = name
        print(f"{self.name} Welcome")

    def display(self):
        print("Hello car.")

class bike(car):
    def display(self):
        super().display()
        print("Hello , bike.")

b1 = bike("pagani")

print(dir(b1))
"""

print(":-"*40)
print("Q-8")
print(":-"*40)
"""
class car:
    def __init__(self, name):
        self.name = name


c1 =  car("Alice")

print(isinstance(c1 , car))
print(isinstance(c1 , str))
"""

print(":-"*40)
print("Q-9")
print(":-"*40)

"""
class Calculator:
    """This class performs basic arithmetic operations like addition."""

    def add(self, a, b):
        """Returns the sum of two numbers."""
        return a +b

print("--- Class Documentation ---")
help(Calculator)

print("\n--- Method Documentation --- ")
help(Calculator.add)
"""
