print("="*40)
print("Q-1")
print("="*40)
"""
numbers = [10, 20, 40, 30, 50]

print(len(numbers))
print(max(numbers))
print(sorted(numbers))
print(sum(numbers))
print(type(numbers))
"""

print("="*40)
print("Q-2")
print("="*40)
"""
def factorial(n):
    result = 1
    if n < 0:
        print("negative value is not vaild")
    else:
        for i in range(1, n+1):
            result *= i
        return result

num = int(input("Enter a Factorial Number: "))

print(f"{num} Number Factorial is {factorial(num)}")
"""

print("="*40)
print("Q-3")
print("="*40)
"""
def square(n):
    result = 0
    return [num ** 2 for num in n]

num = [10, 20, 30 , 40, 50]
square_list = square(num)

print("original List",num)
print("Square List",square_list)
"""

print("="*40)
print("Q - 4")
print("="*40)
"""
def frequency(input_string):
    frequencys = {}
    for char in input_string:
        if char in frequencys:
            frequencys[char] += 1
        else:
            frequencys[char] = 1
    return frequencys

string = "banana nenno"
result = frequency(string)
print(result)
"""

print("="*40)
print("Q - 5")
print("="*40)

"""
def cude(num):
    cude_list = []

    return [ nm * 3 for nm in num]

list_num = [1, 2, 3, 45, 4, 5]

result = cude(list_num)

print("Original List = ", list_num)
print("Cude List = ", result)
"""

print("="*40)
print("Q - 6")
print("="*40)
"""
def sum_multiplt(*args):

    if len(args) == 0:
        return 0

    sum_product = 0
    for num in args:
        sum_product += num

    product = 1
    for num in args:
        product *= num

    return sum_product,product

sum_product,product = sum_multiplt(2, 5, 3, 6)
print(f"1 Test sum:{sum_product} | and Product: {product}")

result_sum, result_product = sum_multiplt(2, 43, 44, 55, 66)
print(f"1 Test sum:{result_sum} | Product: {result_product}")
"""

print("="*40)
print("Q - 7")
print("="*40)
"""
def Student_list(*args):

    if not args:
        print("No Student Provide Name. list is empty.")
        return

    for num in args:
        print(num)

Student_list("Alice", "Bob", "Robinsion", "Shrey")
Student_list()
"""

print("="*40)
print("Q - 8")
print("="*40)
"""
def mixed_args(*args):

    strings = ()
    numbers = ()
    
    for i in args:
        if type(i) == str:
            strings += (i,)
        elif type(i) == int or type(i) == float:
            numbers += (i,)

    return strings , numbers

string , number = mixed_args("AI",20,"fultter",30,"ui/ux digion",40)

print("Strings tuple: ",string)
print("Numbers tuple:", number)
"""

print("="*40)
print("Q - 9")
print("="*40)
"""
def Student(**kwargs):
    print("Student Details")

    for key,value in kwargs.items():
        print(f"{key} : {value}")


Student(name="shrey", age = 20 , city = "surat")
"""

print("="*40)
print("Q - 10")
print("="*40)

"""
def Product(**kwargs):
    total = kwargs["price"] * kwargs["quantity"]

    return f"Product: {kwargs['name']}\nTotal Cost: {total}"

result = Product(name ="Laptop", price=50000, quantity = 2)

print(result)
"""

print("="*40)
print("Q - 11")
print("="*40)
"""
def employee(**kwargs):
    if "name" not in kwargs:
        print("Name is missing")
    if "department" not in kwargs:
        print("department is missing")
    if "salary" not in kwargs:
        print("salary is missing")
    if "name" in kwargs and "department" in kwargs and "salary" in kwargs:
        print("Employee Details")
        print("Name :", kwargs["name"])
        print("Department  :", kwargs["department"])
        print("Salary :", kwargs["salary"])

employee(name="Robinson",department="BCA",salary=40000)
"""

print("="*40)
print("Q - 12")
print("="*40)

"""
def rectangle_area(length, width):
    '''
    Calculate the area of a rectangle.

    Parameters:
    length : Length of the rectangle
    width  : Width of the rectangle

    Returns:
    Area of the rectangle
    '''
    return length * width

area = rectangle_area(10, 5)
print("Area =", area)

print("\nDocstring:")
print(rectangle_area.__doc__)
"""

print("="*40)
print("Q - 13")
print("="*40)
"""
def fibonacci(n):
    '''
    Function Name : fibonacci

    Purpose:
        Returns the Fibonacci sequence up to the given number.

    Parameter:
        n : Integer
            The maximum limit for the Fibonacci sequence.

    Return:
        A list containing Fibonacci numbers up to n.
    '''

    a = 0
    b = 1

    while a <= n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c

num = int(input("Enter a number: "))
fibonacci(num)

print("\n\nDoc string")
print(fibonacci.__doc__)
"""
