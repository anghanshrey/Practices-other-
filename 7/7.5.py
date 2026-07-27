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

list_number = []
print("The 1D array :")
for i in range(1):
    i = list(map(int, input("Enter 1D array Elements : ").split(" ")))
    list_number.append(i)

print("Original List : ",list_number)

asc_list_number = sorted(list(list_number))

print("sorted Original List : ",asc_list_number)
