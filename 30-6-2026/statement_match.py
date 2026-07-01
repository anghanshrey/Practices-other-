#Q-1
"""
num1 = int(input("Enter Your First Number:"))
num2 = int(input("Enter Your Second Number:"))
num3 = int(input("Enter Your Third Number:"))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is maximum number")
    elif num2 > num3:
        print(f"{num2} is maximum number")
else:
    print(f"{num3} is maximum number")
"""

#Q-2
"""
num1 = int(input("Enter Your First Number:"))
num2 = int(input("Enter Your Second Number:"))
num3 = int(input("Enter Your Third Number:"))

if num2 < num1:
    if num3 < num1:
        print(f"{num3} is minimum number")
    elif num3 < num2:
        print(f"{num3} is minimum number")
else:
    print(f"{num1} is minimum number")
"""

#Q-3
"""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))


if num1 >= num2:
    if num1 >= num3:
        if num1 >= num4:
            max_num = num1
        else:
            max_num = num4
    else:
        if num3 >= num4:
            max_num = num3
        else:
            max_num = num4
else:
    if num2 >= num3:
        if num2 >= num4:
            max_num = num2
        else:
            max_num = num4
    else:
        if num3 >= num4:
            max_num = num3
        else:
            max_num = num4

print("The maximum number is:", max_num)
"""

#Q-4
"""
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Sceond Number:"))

operator = input("Enter Operator + , - , * , / :")

match operator:
    case "+":
        print(f"{num1}+{num2}={num1+num2}")
    case "-":
        print(f"{num1}-{num2}={num1-num2}")
    case "*":
        print(f"{num1}*{num2}={num1*num2}")
    case "/":
        print(f"{num1}/{num2}={num1/num2}")
"""

#Q-5
"""
print("1. SandWich \n2. Pizza \n3. Burger \n")

num = int(input("Choice the Number:"))

match num:
    case 1:
        print("Order a Sandwith")
    case 2:
        print("1. Thin Crust Pizza\n2. Cheese Burst Pizza\n3. Fresh Dough pizza")
        choice = int(input("Choice the Pizza"))
        match choice:
            case 1:
                print("Order Thin Crust Pizza")
            case 2:
                print("Order Cheese Burst Pizza")
            case 3:
                print("Order Fresh Dough Pizza")
    case 3:
        print("Order a Burger")
"""

#Q-6
"""
print("1. English \n2. Hindi \n3. Gujarati \n")

num = int(input("Choice the Number:"))

match num:
    case 1:
        print("choice English")
    case 2:
        print("choice Hindi")
    case 3:
        print("choice Gujarati")
"""
    
