print("="*40)
print("Q-1")
print("="*40)

"""
array = [10, 20, 30, 40, 50]

for i in array:
    print(i)
"""

print("="*40)
print("Q-2")
print("="*40)

"""
size = int(input("Enter Your size of elements :"))

numbers =[]
total_sum = 0

for i in range(size):
           value = int(input(f"Enter { i + 1} Elements: "))

           numbers.append(value)
           total_sum += value

print(numbers)
print(f"The sum of all elements is: {total_sum}")
"""
print("="*40)
print("Q-3")
print("="*40)
"""
numbers = [11, 22, 33, 44, 55]

print("Original array: ",numbers)

add = int(input("Enter the Update value : "))
index = int(input("Enter the spectific index: "))

print(f"Insert element {add} at index {index}...")

numbers.insert(index, add)

print("Inserting array : ",numbers)
"""

print("="*40)
print("Q-4")
print("="*40)
"""
numbers = [11, 22, 33, 44, 55]

print("Original array: ",numbers)

Remove = int(input("Enter the Update value : "))

print(f"Delete element with value {Remove} ...")

numbers.remove(Remove)
print("Removeing Element array : ",numbers)
"""

print("="*40)
print("Q-5")
print("="*40)

"""
numbers = [11, 22, 33, 44, 55]

print("Original array: ",numbers)

add = int(input("Enter the Update value : "))
index = int(input("Enter the spectific index: "))

print(f"Update element {add} at index {index}...")
numbers[index] = add
print("Updating array: ", numbers)
"""

print("="*40)
print("Q-6")
print("="*40)

"""
number = [11, 22, 33, 44, 55, 66]

print("Original array: ",number)

choice_element = int(input("Choice your value : "))

result  = 0

for i in range(len(number)):
    if number[i] < 0:
        print(f"Skipping negative number at index {i}")
        continue
    
    if number[i] == choice_element:
         result = i
         print(f"search index found is {result}")
         break
"""

print("="*40)
print("Q-7")
print("="*40)

"""
array1_list = [1, 2, 3, 4]
array2_list = [11, 22, 33, 44]

print("array 1 : ",array1_list)
print("array 2 : ",array2_list)

marge_array = list(set(array1_list).union(array2_list))

print("concatenate array 1 and array 2 : ",marge_array)
"""
