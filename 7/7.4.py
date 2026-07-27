print("="*40)
print("Q-1")
print("="*40)
"""
numbers = int(input("Enter array size : "))

arr = []

for i in range(numbers):
    val = int(input(f"a[{i}] = "))
    arr.append(arr)

print("Length of an Array: ",len(arr))
"""

print("="*40)
print("Q-2")
print("="*40)
"""
numbers = int(input("Enter array size : "))

arr = []
sum = 0

for i in range(numbers):
    val = int(input(f"a[{i}] ="))
    arr.append(val)
    sum += val

print("Average of an Array : ",sum/len(arr))
"""

print("="*40)
print("Q-3")
print("="*40)

"""
arr1 = []
arr2 = []

size = int(input("Enter array size : "))

print("\nEnter array A's elements: ")
for i in range(size):
    val = int(input(f"a[{i}] = "))
    arr1.append(val)

print("\nEnter array B's elements: ")
for i in range(size):
    val = int(input(f"b[{i}] = "))
    arr2.append(val)

arr3 = []
su = 0

for i in range(size):
    su = arr1[i] + arr2[i]
    arr3.append(su)

print("Array C is:", arr3)
"""

print("="*40)
print("Q-4")
print("="*40)

"""
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr1 = []
for i in arr:
    val = i * 2
    arr1.append(val)

print("Original list : ",arr)

print("\nResult : ",arr1)
"""

print("="*40)
print("Q-5")
print("="*40)

"""
array = list(map(int, input("Enter the array : ").split(" ")))

print("List : ",array)

numbers = int(input("Enter the array number : "))

found = False

for i in range(len(array)):
    if array[i] == numbers:
        print("Index : ", i)
        found = True
        break
        
if not found:
    print("Not Found")
"""

print("="*40)
print("Q-6")
print("="*40)

"""
size = int(input("Enter array size: "))

array = []
even = []
odd = []

for i in range(size):
    val = int(input(f"Element {i + 1}: "))
    array.append(val)

for i in array:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers: ",even)
print("Odd numbers: ",odd)
"""

print("="*40)
print("Q-7")
print("="*40)

"""
array = list(map(int, input("Enter the array : ").split(" ")))

print("array : ",array)

first_five = array[:5]

alter_array = array[::2]

print("First five elements: ", first_five)
print("Alternate elements: ", alter_array)
"""

print("="*40)
print("Q-8")
print("="*40)

"""
array = list(map(int, input("Enter the array list : ").split(" ")))

print(array)

print("First :", array[0])
print("Last :", array[-1])
print("Middle :", array[len(array) // 2])
"""
