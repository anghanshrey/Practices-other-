# Q-1
"""
fruits = ["apple","banana","cherry","orange","date"]

print("Second fruits:",fruits[1])
print("Last fruits:",fruits[-1])

fruits.append("Mango")

fruits.pop()

fruits.sort()

fruits.reverse()

print("final List:",fruits)
"""

#Q-2
"""
number = (1,2,3,4,5)

print("number 3 element access:",number[2])

print("tuple object does not support item assignment")

number[1] = 99
"""

#Q-3
"""
fruit_list = ["Apple","banana","cherry"]
fruit_tuple = ("Apple","banana","cherry")

fruit_list[0] = "kiwi"
print("Modified list:", fruit_list)

print("tuples are stored in memory as a fixed. immutable sequcnce.")
fruit_tuple[0] = "kiwi"
"""

#Q-4
"""
squares = []

for i in range(1,11):
    squares.append(i*i)
print("squares:",squares)

events = []
for num in range(1,21):
    if num % 2 == 0:
        events.append(num)

print("events:",events)

list = ["hello","WORLD","PyThOn"]

lowercased = []
for word in list:
    lowercased.append(word.lower())
print("Lower:",lowercased)
"""
