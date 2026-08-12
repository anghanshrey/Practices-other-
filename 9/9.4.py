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



