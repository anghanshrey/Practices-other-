
print("="*40)
print("Q-1")
print("="*40)

"""
file = open("sample.txt" , "w")

file.write("Python is a versatile programming language.")

file.close()
"""

print("="*40)
print("Q-2")
print("="*40)

"""
file = open("sample.txt" , "r")

data = file.read()

print(data)

file.close()

file1 = open("sample.txt", "w+")

file1.write("Learning file handing in python is fun!")

file1.seek(0)

data1 = file1.read()

print(data1)

file1.close()
"""

print("="*40)
print("Q-3")
print("="*40)

"""
file = open("sample.txt", "r")

print(file.readlines())

file.close()
"""

print("="*40)
print("Q-4")
print("="*40)

'''
file = open("notes.txt", "w")

file.writelines("""Line 1 : Python is easy to learn.
Line 2: It has numerous libraries.
Line 3: file handing is one of its features.
""")

file = open("notes.txt", "r")

print(file.read())

file.close()
'''

print("="*40)
print("Q-5")
print("="*40)

"""
file = open("notes.txt", "a")

file.write("LIne 4: Python supports multiple modes of file handing.")

file = open("notes.txt", "r")

print(file.read())

file.close()
"""

print("="*40)
print("Q-6")
print("="*40)

"""
file = open("notes.txt", "rb")

data = file.read()

print(data)

file.close()
"""

print("="*40)
print("Q-7")
print("="*40)

"""
file = open("notes.txt", "r")

data = file.read()

print("Words:", len(data.split()))
print("Characters:", len(data))
print("Lines:", len(data.splitlines()))

file.close()
"""

print("="*40)
print("Q-8")
print("="*40)

"""
file = open("notes.txt", "r+")

data = file.read()

print(data)

file.write("\nThis file was last modified by adding this sentence.")

file.close()
"""

print("="*40)
print("Q-9")
print("="*40)

"""
word = input("Enter a word to search in the file: ")

line_number = 0
file = open("notes.txt", "r")

for line in file:
    if word in line:
        print(f"Word '{word}' found in line {line_number + 1}.")

    line_number += 1

file.close()
"""

print("="*40)
print("Q-10")
print("="*40)

"""
file = open("notes.txt", "r")

data = file.read()

file.close()

file = open("backup.txt", "w")

file.write(data)

file.close()
"""

print("="*40)
print("Q-11")
print("="*40)

with open("text.txt", "w") as file:
    file.write("hello python")

with open("text.txt", "r") as file:
    data = file.read()
    print("--- 1. Read Mode ---")
    print(data)



with open("text.txt", "a") as file:
    file.write("Line 2: Hello Java")


with open("text.txt", "r+") as file:
    data = file.read()
    print("\n--- 2. Read/Write Mode (r+) ---")
    print(data)  
    file.write("Line 3: Hello Javascript")

with open("text.txt", "w+") as file:
    file.write("LIne 4: Hello R")
    file.seek(0) 
    data = file.read()
    print("\n--- 3. Write/Read Mode (w+) ---")
    print(data) 

with open("text.txt", "a+") as file:
    file.seek(0) 
    data_before = file.read()
    print("\n--- 4. Append/Read Mode (a+) ---")
    print("Before append: ", data_before) 
    
    file.write("\nLine 5: Hello CSS")
    
    file.seek(0)
    data_after = file.read()
    print("After append:  ", data_after)


with open("text.txt", "a+") as file:
    file.seek(0)
    data_before1 = file.read()
    print("\n--- 5. Append Mode (a) ---")
    print("Before append: ", data_before1)

    file.write("\nLine 6: Hello HTML")

    file.seek(0)
    data_after = file.read()
    print("After append:  ", data_after)

