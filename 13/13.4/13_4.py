print("="*40)
print("Q-1")
print("="*40)
"""
from math_utils import add, subtract, multiply, divide

print("Add Value:", add(10, 5))
print("Subtract Value:", subtract(10, 5))
print("multiply Value:", multiply(10, 5))
print("divide Value:", divide(10, 5))
"""

print("="*40)
print("Q-2")
print("="*40)

"""
from math import sqrt
import math as m

print(sqrt(49))

radians = m.radians(90)
sin_val = m.sin(radians)
print(f"sin(90°): {sin_val}")
"""

print("="*40)
print("Q-3")
print("="*40)

"""
import string_utils

sample_text = "Hello World"
vowel_count = string_utils.count_vowels(sample_text)
print(f"Number of vowels in '{sample_text}' : {vowel_count}")
"""

print("="*40)
print("Q-4")
print("="*40)

"""
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    print("This script is excuted directly.")
    greet("Alice")
else:
    print("This script is imported as a module.")
"""

print("="*40)
print("Q-5")
print("="*40)

"""
import helper

if __name__ == "__main__":
    print("This is importing the helper module.")
    helper.greet()
"""

print("="*40)
print("Q-6")
print("="*40)

"""
from shapes import rectangle, circle

print(f"Circle Area (5): {circle.area(5):.2f}")
print(f"Circle Circumference (5): {circle.circumference(5):.2f}")

print(f"Rectangle Area (4, 6): {rectangle.area(4, 6)}")
print(f"Rectangle Perimeter (4, 6): {rectangle.perimeter(4, 6)}")
"""

print("="*40)
print("Q-7")
print("="*40)
"""
from utilities import file_utils, date_utils

file_utils.write_file("sample.txt", "Hello, this is a simple text file.")
print(f"file contents: {file_utils.read_file('sample.txt')}")

days = date_utils.days_between("2023-01-01", "2023-12-31")
print(f"Days between dates: {days}")
"""

print("="*40)
print("Q-8")
print("="*40)

"""
import math as m

for d in dir(m):
    print(f"{d}\n")

class Python:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}\n, Age: {self.age}\n")

python = Python("Python", 30)

print(f"class All Dir attributes and methods : {dir(python)}\n")
"""

print("="*40)
print("Q-9")
print("="*40)

"""
from geometry import circle, triangle

print(f"Area of circle (4): {circle(4):.2f}")
print(f"Area of triangle (3, 4): {triangle(6, 3):.2f}")
"""