# Control Flow in python

# statements in python

"""
1. if statement
2. if........else statement
3. if..elif..else statement
4. match statement
5. continue statement
6. break Statement
"""

#The if statement executes a block of code only if the specified condition is True. if the condition is False, the code inside the if block is skipped.

"""
if condition:
    # code
"""

age = 17

if age >= 18 :
    print("YOu are eligible to vote.")

# The if....else statement is used when there are two possible outcomes:
# if the condition is True, the if block executes.
# if the condition is False , the else block executes.

"""

if condition:
    # code (True)
else:
    # code (False)
    
"""

number = 0

if number >= 0:
    print("Positive Number")
else:
    print("Negative Number")

# if....elif....else statement

# if...elif..else statement is used when multiple condition need to be checked.

"""
if condition1:
    #code
elif condition2:
    #code
elif condition3:
    #code
else:
    #code
    
"""

marks = 82
grade = ""

if marks >= 90:
    grade += "Grade A"
elif marks >= 75:
    grade += "Grade B"
elif marks >= 60:
    grade += "Grade C"
else :
    print("Fail")

print(grade)

# match-case Statements

num1 = 10
num2 = 5

operator = input("Enter Your Operator Sign :")

match operator:

    case "+":
        print("Addition :", num1 + num2)
    case "-":
        print("Substraction :" , num1 - num2)
    case "/":
        print("Division : ", num1 / num2)
    case "*":
        print("Multiplication :" , num1 * num2)
    case _:
        print("Invaild Operator")

# Multiple Values in One Case Use

char = "b"

match char:

    case "a"| "e" | "i" | "o" | "u" :
        print("Vowel")
    case _:
        print("Consonents")
