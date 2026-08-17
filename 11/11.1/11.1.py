print("="*40)
print("Q-1")
print("="*40)


file = open("sample.txt" , "w")

file.write("Python is a versatile programming language.")

file.close()


print("="*40)
print("Q-2")
print("="*40)

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


