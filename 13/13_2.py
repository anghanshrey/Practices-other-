print("="*40)
print("Q-1")
print("="*40)

import math

"""
number = int(input("Enter calculate number : "))

print(
    f"\nSquare root to {number} : {math.sqrt(number)}"
    f"\nfactorial to {number} : {math.factorial(number)}"
    f"\nPower of {number} : {math.pow(number , 2)}"
)
"""

print("="*40)
print("Q-2")
print("="*40)

"""
radius = float(input("Enter radius Value : "))

result = math.pi * radius * radius

print("The area of a circle : ", result)

natural_log = float(input("Enter natural logarithm Value : "))

print("The natural logarithm of a number : ",math.log(natural_log))
"""

print("="*40)
print("Q-3")
print("="*40)

"""
distance = 10
angle_degrees = 30

angle_radians = math.radians(angle_degrees)

sine_val = math.sin(angle_radians)
cosine_val = math.cos(angle_radians)
tangent_val = math.tan(angle_radians)

height = distance * tangent_val

print(
    f"\nSin(30): {sine_val:.4f}"
    f"\nCos(30): {cosine_val:.4f}"
    f"\nTan(30): {tangent_val:.4f}"
    f"\nCalculated Height of the tree: {height:.2f} meters"
)
"""

print("="*40)
print("Q-4")
print("="*40)

"""
number = float(input("Enter calculate ceiling, floor, absolute Value : "))

print(
    f"\ncurrent Value : {number}"
    f"\nceiling Value : {math.ceil(number)}"
    f"\nfloor Value : {math.floor(number)}"
    f"\nabsolute Value : {math.fabs(number)}"
)
"""

print("="*40)
print("Q-5")
print("="*40)

import random
"""
random_integers = [random.randint(1, 100) for _ in range(10)]

print("List of 10 random integers:", random_integers)
"""

print("="*40)
print("Q-6")
print("="*40)

"""
dice_roll = random.randint(1,6)
print(f"Dice roll result: {dice_roll}")

numbers = [10, 20, 30, 40, 50]
print(f"Original list: {numbers}")

random.shuffle(numbers)
print(f"Shuffled list: {numbers}")
"""

print("="*40)
print("Q-7")
print("="*40)

"""
string = ["Robinson" , "Robinhood", "Robin" , "Robins"]

selected_word = random.choice(string)

print(f"Selected item: {selected_word}")
"""

print("="*40)
print("Q-8")
print("="*40)

"""
options = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors : ").strip().lower()
computer_choice = random.choice(options)

print(f"Computer chose: {computer_choice}")

if user_choice not in options:
    print("invaild input! Please choose rock, paper, or scissors.")
elif user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
"""