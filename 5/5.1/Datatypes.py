"""
print("="*40)
print("Q -1")
print("="*40)

firstname=input("Enter User First Name :")
lastname=input("Enter User Last Name :")

print(f"Hello, {firstname}, {lastname}.")
"""

"""
print("="*40)
print("Q -2")
print("="*40)

item = "apple"
price = 5.50

print(f"The price of {item} is {price} dollars.")
"""

"""
print("="*40)
print("Q -3")
print("="*40)

name = input("Enter Your string world :")

reverse_name = name[::-1]

print(f"Reversed string: {reverse_name}")

if name.lower() == reverse_name.lower():
    print("This string is a palindrome.")
else:
    print("This String is not a palindrome. ")
"""

"""
print("="*40)
print("Q-4")
print("="*40)

user = input("User Enter a String :")

upper_user = user.upper()

print("String convert to Uppercase",upper_user+".")

lower_user = user.lower()

print("String convert to lowercase",lower_user)

title_user = user.title()

print("string convert to titlecase", title_user)
"""

"""
print("="*40)
print("Q-5")
print("="*40)

sentence = "Machine Learning and AI are trending."

position = sentence.find("AI")

print(f"position of 'AI' : {position}")

new_sentence = sentence.replace("AI","Aritifical Intelligence")

print(f"Modified sentence: {new_sentence}")

data = "data data mining and big data"

data_Count = data.count("data")

print(f"Occurrences of 'data' : {data_Count}.")
"""

"""
print("="*40)
print("Q-6")
print("="*40)

fruits_string = "apple,banana,grapes"

fruits_list = fruits_string.split(",")

print(f"Resulting list: {fruits_list}")

add_list = ["Python", "is","awesome"]

joined_sentence = " ".join(add_list)

print(f"Resultingt Sentence: {joined_sentence}\n")

words = "Line 1: my name is shrey.
Line 2: i am 20 years old.
Line 3:i am AI engineer.
"

for line in words.splitlines():
    print(line)
"""

print("="*40)
print("Q-7")
print("="*40)

string = "Hello to the World"

starts_string = string.startswith("Hello")
ends_string = string.endswith("World")

print(f"starting Word is 'Hello' {starts_string}.\nEnding String Word is 'World' {ends_string}.")

mixed_string = "Data123#Science!"

print("Cleand String :",end=" ")
for word in mixed_string:
    if word.isalpha():
        print(word,end="")

print()

reverse = "Python"

reverse_string = reverse[::-1]

print(f"{reverse} reverse String is {reverse_string}.")




