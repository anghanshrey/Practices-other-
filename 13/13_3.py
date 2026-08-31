print("="*40)
print("Q-1")
print("="*40)

import uuid
"""
random_uuid = uuid.uuid4()

print(f"Random UUID: {random_uuid}")

name = "Example.com"

named_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, name)
print(f"named_uuid: {named_uuid}")
"""

print("="*40)
print("Q-2")
print("="*40)
"""
student_ids = ["S101", "S102", "S103", "S104", "S105"]
student_dict = {}

for s_id in student_ids:
    student_dict[s_id] = uuid.uuid4()

print("Student Database:", student_dict)
"""

print("="*40)
print("Q-3")
print("="*40)

"""
uuid1 = uuid.uuid4()
uuid2 = uuid.uuid4()

if uuid1 == uuid2:
    print("UUIDs are equal.")
else:
    print("UUIDs are not equal.")
"""

print("="*40)
print("Q-4")
print("="*40)

"""
class ECommerceSystem:
    def __init__(self):
        self.orders = {}

    def place_order(self, item_name):
        order_id = str(uuid.uuid4())
        self.orders[order_id] = {"item": item_name}
        return order_id

system = ECommerceSystem()
id1 = system.place_order("Loptop")
id2 = system.place_order("Wireless Mouse")

print(f"Order 1 ID: {id1} -> {system.orders[id1]}")
print(f"Order 2 ID: {id2} -> {system.orders[id2]}")
"""

print("="*40)
print("Q-5")
print("="*40)

"""
numbers = [42, 15, 67, 30, 35]

asc_number = sorted(numbers)
print("Ascending:", asc_number)

desc_number = sorted(numbers, reverse=True)
print("Descending:", desc_number)
"""

print("="*40)
print("Q-6")
print("="*40)

"""
words = ["banana", "apple", "cherry", "fig"]

by_length = sorted(words)
print("Sorted by length:", by_length)

by_last_letter = sorted(words, key = lambda word: word[-1])
print("sorted by last letter:", by_last_letter)
"""

print("="*40)
print("Q-7")
print("="*40)

"""
student = [
    {"name" : "Robinson" , "age" : 20}, 
    {"name" : "Rosan" , "age" : 27}, 
    {"name" : "Robinhood" , "age" : 23}, 
    {"name" : "Robin" , "age" : 25}
    ]

sorted_student = sorted(student, key=lambda student:student["age"])

print("Sort list by age",sorted_student)
"""

print("="*40)
print("Q-8")
print("="*40)

"""
names = [
    "Vikas",
    "vatsal",
    "Vihar",
    "Vinay",
]

upper_names = list(map(str.upper, names))
print("Uppercase strings:", upper_names)
"""

print("="*40)
print("Q-9")
print("="*40)

"""
numbers = [1, 2, 3, 4, 5, 6]

square = list(map(lambda x : x ** 2, numbers))

print("Square list:", square)
"""

print("="*40)
print("Q-10")
print("="*40)

"""
prices = [ 1000, 2000, 3000, 4000, 100]

tax_price = list(map(lambda x : round(x * 1.18, 2) , prices))

print("Final prices with 18% tax:", tax_price)
"""

print("="*40)
print("Q-11")
print("="*40)

"""
numbers = [ 11, 22, 33, 44, 55, 66]

even_number = list(filter(lambda x : x % 2 == 0, numbers))

print("Even numbers:", even_number)
"""

print("="*40)
print("Q-12")
print("="*40)

"""
words = ["apple", "banana", "Kiwi", "orange", "fig"]

long_words = list(filter(lambda word : len(word) > 5, words))

print("Strings longer than 5 chars:", long_words)
"""

print("="*40)
print("Q-13")
print("="*40)

"""
scores = [35, 65, 55, 67, 87, 90, 29, 18, 43, 99]

passed_student = list(filter(lambda x : x >= 40, scores))

print("Passing Scores:", passed_student)
"""

print("="*40)
print("Q-14")
print("="*40)

from functools import reduce

"""
nums = [1, 2, 3 ,4 ,5]

product = reduce(lambda x, y: x* y, nums)
print("Product of elements:", product)
"""

print("="*40)
print("Q-15")
print("="*40)

"""
words = ["cat", "elephant", "dog", "hippopotamus", "giraffe"]

longest_word = reduce(lambda x , y : x if len(x) > len(y) else y, words)

print("Longest word:", longest_word)
"""

print("="*40)
print("Q-16")
print("="*40)

"""
sentence_words = ["Python", "is", "a", "powerful", "language"]

sentance = reduce(lambda x, y: f"{x} {y}", sentence_words)

print("Concatenated sentance:", sentance)
"""



