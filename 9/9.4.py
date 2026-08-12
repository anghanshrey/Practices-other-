print(" ================== ")
print(" Q-1 ")
print(" ================== ")

"""
class Sum():

    def __init__(self, a , b , name1 , name2):
        self.a = a
        self.b = b
        self.name1 = name1
        self.name2 = name2

    def get_number(self):
        return self.a + self.b

    def get_string(self):
        return self.name1 + self.name2

s = Sum(10 , 5 , "Shrey " , " Anghan")
print("Sum of  2 Number : "s.get_number())
print("Concatenation of 2 string : "s.get_string())
"""

print("="*40)
print("Q-2")
print("="*40)

"""
import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")
"""

print("="*40)
print("Q-3")
print("="*40)
"""
class string:
    def __init__(self, name):

        self.name = name

    def display(self):
        print(f"name : {self.name} length of : {len(self.name)} ")

class lists(string):

    def __init__(self,lists):

        self.lists = lists

    def display(self):
        print(f"list : {self.lists} length of : {len(self.lists)}")

class dicts(string):

    def __init__(self, Dict):

        self.Dict = Dict

    def display(self):
        print(f"dict : {self.Dict} length of : {len(self.Dict)}")

displays = [string("Shrey") , lists([1, 2, 3, 4 ,5, 6]) , dicts({"name" : "Shrey" , "Age" : 30})]

for dis in displays:
    dis.display()
"""

print("="*40)
print("Q-4")
print("="*40)

"""
class Transport:
    def travel(self):
        pass

class Train(Transport):
    def travel(self):
        return "Traveling on tracks thought countryside."

class plane(Transport):
    def travel(self):
        return "Flying high in the clouds."

vehicles = [Train(), plane()]

for vehicle in vehicles:
    print(vehicle.travel())
"""

print("="*40)
print("Q-5")
print("="*40)

"""
class Calculator:

    def multiply(self, a , b=1, c = 1):
        return a * b * c

calc = Calculator()
print("multiple of 3 arguments (2 defaulter)",calc.multiply(4))
print("multiple of 3 arguments (1 defaulter)"calc.multiply(4, 5))
print("multiple of 3 arguments (0 defaulter)"calc.multiply(4, 5, 6))
"""

print("="*40)
print("Q-6")
print("="*40)

"""
class Animal:

    def speak(self):
        return "Animal Speak."

class Dog(Animal):

    def speak(self):
        return "Dog Speak Bhow... Bhow..."

class cat(Animal):

    def speak(self):
        return "Cat Speak Meow... Meow..."

animals = [Dog(), cat()]
for animal in animals:
    print(animal.speak())
"""

print("="*40)
print("Q-7")
print("="*40)

print("="*40)
print("Q-8")
print("="*40)

"""
class Vehicle:

    def start(self):
        print("Start Vehicle....")

class bike(Vehicle):

    def start(self):
        print("Start Bike......")

class Car(Vehicle):

    def start(self):
        print("Start Car......")

vehicles = [bike(), Car()]

for veh in vehicles:
    veh.start()
"""

print("="*40)
print("Q-9")
print("="*40)

"""
class Printer:
    def print_data(self, arg1=None, arg2= None):
        if arg1 is not None and arg2 is not None:
            print(f"Both: {arg1} and {arg2}")
        elif arg1 is not None:
            if isinstance(arg1, str):
                print(f"String: {arg1}")
            elif isinstance(arg1, int):
                print(f"Integer: {arg1}")
        else:
            print("No arguments provided")

p = Printer()
p.print_data("Hello")
p.print_data(45)
p.print_data("Age", 21)
"""

print("="*40)
print("Q-10")
print("="*40)

"""
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

result = issubclass(Student, Person)
print(f"Is Student a subclass of Person := {result}")
"""

print("="*40)
print("Q-11")
print("="*40)

"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
        print(f"Employee Initialized: {self.name}, Salary Initialized: {self.salary}")

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        print(f"Manager initialized for department: {self.department}")

mgr = Manager("Alice", 90000 , "IT")
"""

print("="*40)
print("Q-12")
print("="*40)
"""
class Grandparent:

    def display(self):
        print("Grandparent display.")

class Parent(Grandparent):

    def display(self):
        print("Parent display.")

class Child(Parent):

    def display(self):
        print("Child display.")

print(f"Is subclass Relationship : {issubclass(Child, Parent)}")
print(f"Is subclass Relationship : {issubclass(Child, Grandparent)}")
print(f"Is subclass Relationship : {issubclass(Parent, Grandparent)}")
"""

print("="*40)
print("Q-13")
print("="*40)

"""
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        print(f"User profile created for: {self.username}")

class Admin(User):
    def __init__(self, username, email, access_level):
        # Call the parent User constructor
        super().__init__(username, email)
        self.access_level = access_level
        print(f"Admin level set to: {self.access_level}")

# Testing the code
admin_user = Admin("john_doe", "john@example.com", "Full Access")
"""
