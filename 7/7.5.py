"""
print("="*40)
print("Q-1")
print("="*40)


matrix = []
rows = int(input("Enter the rows : "))
print(f"Enter the Elements of a {rows}x{rows} matrix: ")
for i in range(rows):
    value = list(map(int, input(f"Enter the {i + 1} Rows : ").split(" ")))
    matrix.append(value)

print(f"{rows}x{rows} Matrix:")

for i in matrix:
    for val in i:
        print(val,end = " ")
    print("")
"""

print("="*40)
print("Q-2")
print("="*40)
"""
matrix = []
rows = int(input("Enter the rows :"))

print(f"Enter the Elements of a {rows}x3 matrix : ")
for i in range(rows):
    value = list(map(int, input(f"Enter the {i + 1} Rows:").split(" ")))
    matrix.append(value)

print(f"{rows}x3 Matrix:")

for i in matrix:
    for val in i:
        print(val,end=" ")
    print("")

print("transpose 3x2 matrix: ")

for i in range(3):
    for val in matrix:
        print(val[i],end=" ")
    print(" ")
"""

print("="*40)
print("Q-3")
print("="*40)

"""
matrix = []
rows = int(input("Enter the rows :"))

print(f"Enter the Elements of a {rows}x{rows} matrix : ")
for i in range(rows):
    value = list(map(int, input(f"Enter the {i + 1} rows : ").split(" ")))
    matrix.append(value)

print(f"{rows}x{rows} matrix : ")

sum = 0

for i in matrix:
    for val in i:
        print(val, end = " ")
        sum += val
    print("")

print("Sum of matrix : ",sum)
"""

print("="*40)
print("Q-4")
print("="*40)

"""
matrix = []
rows = int(input("Enter the rows : "))

print(f"Enter the Elements of a {rows}x{rows} matrix : ")

for i in range(rows):
    val = list(map(int, input(f"Enter the {i + 1} rows : ").split(" ")))
    matrix.append(val)

print(f"{rows}x{rows} matrix : ")

maximum = 0
minimum = 40

for i in matrix:
    for val in i:
        print(val,end=" ")
        if val > maximum:
            maximum = val
        if val < minimum:
            minimum = val
    print()

print("\nMaximum Value =", maximum)
print("Minimum Value =", minimum)
"""

print("="*40)
print("Q-5")
print("="*40)

"""
list_number = []
print("The 1D array :")

array = list(map(int, input("Enter 1D array Elements : ").split(" ")))

print("Original List : ",array)

array.sort()

print("Sorted Original List : ",array)
"""

print("="*40)
print("Q-6")
print("="*40)

"""
numbers = [
    ("Raj" , 40),
    ("Robinson" , 50),
    ("Robinhood", 30),
    ("Rohit", 60)
]

result = sorted(numbers , key = lambda x : x[1] )

print("List in Sorted 2 Elements : ",result)
"""

print("="*40)
print("Q-7")
print("="*40)

"""
diction = [
    {\n"name" : "Robin" , "Age": 20},
    {\n"name" : "Robinson" , "Age": 21},
    {\n"name" : "Robinhood" , "Age": 19},
    {\n"name" : "Robinhood juinor" , "Age": 43}
]

result = sorted(diction , key = lambda x : x["Age"])

print("Dictionaries  in Sorted 2 Elements : ", result)
"""

print("="*40)
print("Q-8")
print("="*40)

array = [1, 42, 33, 50, 12]

print("--- DEMONSTRATING sorted() ---")

print("\n\n Original list_a before: ",array)

result = sorted(array)
print("\n Returned value: ",result)

print("\n Original list_a after: ",array)

print("\n\n--- DEMONSTRATING list.sorted() ---")

print("\n\n Original list_b before: ",array)

return_result = array.sort()
print("\n Returned value: ",return_result)

print("\n Original list_b after: ",array)
