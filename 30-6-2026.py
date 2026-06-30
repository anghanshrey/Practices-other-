# loop in python

"""

1. While loop
2. for loop

# while loop:

# A While loop runs as long as the condition is true.
"""

"""

while condition :
    # code block
"""

# print number 1 to 5

i = 1

while i <= 5:
    print(i)
    i += 1

print("="*20)
i = 5

while i >= 1:
    print(i)
    i -= 1

# for loop

# For loop iterate through:

'''
ranges
lists
strings
tuples
dictionaries
'''


'''

for variable in sequence:
    # code block
'''

# Print number 1 to 5

print("==== For Loop ======")

for i in range(1, 6):
    print(i)

print("==== loop through String ====")

name = "python"

for i in name:
    print(i)

print("==== loop through list ====")

fruits = ["Apple", "orange", "Banana", "Mango"]

for item in fruits:
    print(item)

# range() function

# range(start , stop , step)

for i in range(5):
    print(i)

print("="*20)

for i in range(1 , 6):
    print(i)

for i in range(0, 10, 3):
    print(i)

for i in range(10, 0, -1):
    print(i)

# Nested Loops in Python

# A loop inside another loop.

'''
tables
patterns
matrices
grids
'''

'''

for i in range():
    for j in range():
        # block of code

'''

print("=============")

for i in range(1, 6):
    for j in range(1, 6):
        print(j , end=" ")
    print()

print("===== Brack Statement =====")

# Stops the loop immediately.

for i in range(1 , 7):
    if i == 4:
        break
    print(i)

print("===== pass statement =====")

# skips current iterations.

for i in range(1 , 7):
    if i == 5:
        pass
