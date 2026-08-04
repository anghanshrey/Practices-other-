print("="*40)
print("Q-1")
print("="*40)

"""
class Person():

    def __init__(self , name , age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Hi, My Name is {self.name} , I Am {self.age} old.")

p1 = Person("Robinson", 20)
p2 = Person("Robinhood", 25)

p1.display()
p2.display()
"""

print("="*40)
print("Q-2")
print("="*40)

"""
class Count():

    def __init__(self , count = 0):
        self.count = count

    def incerment(self):
        self.count += 1

    def display(self):
        print(f"Count Value: {self.count}")

Sum = Count()

Sum.display()
Sum.incerment()
Sum.display()
"""

print("="*40)
print("Q-3")
print("="*40)

'''
class Dog:
    
    def bark():
        """ self is omitted here 
        TypeError: Dog.bark() takes 0 positional arguments but 1 was given """
        print("woof!")

my_dog = Dog()

print(my_dog.bark.__doc__)

my_dog.bark() 
'''

print("="*40)
print("Q- 4")
print("="*40)
"""
class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    # setter
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    # getter
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

b1 = Book("Train to Pakistan" , "Khushwant Singh")
print(f"Book: {b1.get_title()} by {b1.get_author()}")

b1.set_title("Animal Farm")
print(f"Updated Book: {b1.get_title()}")
"""


print("="*40)
print("Q- 5")
print("="*40)

'''
class Bankaccount:

    def __init__(self, name , balance):

        self.name = name
        self.__balance = balance

    def deposit(self , amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} sucessfully deposit.")
        else:
            print("Invaild Number")

    def withdraw(self , amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f"{amount} sucessfully withdraw.")

    def display(self):
        print(f"{self.name} name balance is {self.__balance}")

account = Bankaccount("Shrey" , 300)

while True:
    print("""
1. deposit
2. withdraw
3. display
4. exit
""")

    choice = int(input("Enter Your choice : "))

    if choice == 1:
        amount = int(input("Enter Deposit amount : "))
        account.deposit(amount)
    elif choice == 2:
        amount = int(input("Enter Withdraw amount : "))
        account.withdraw(amount)
    elif choice == 3:
        account.display()    
    elif choice == 4:
        print("Bye Bye")
        break
    else:
        print("Enter 1 to 4 choice")
'''

print("="*40)
print("Q- 6")
print("="*40)

"""
class student_age:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Setter
    def set_age(self):
        self.age = int(input("Enter New Age : "))

    # getter
    def get_age(self):
        if self.age > 0:
            print(f"Name : {self.name} | Age : {self.age}")
        else:
            print("Invaild Age.")

name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))

Student = student_age(name , age)

Student.get_age()
Student.set_age()
Student.get_age()
"""

print("="*40)
print("Q- 7")
print("="*40)

"""
class Student:

    def __init__(self , name , marks1 , marks2 , marks3):
        self.__name = name
        self.__marks = [marks1 , marks2 , marks3]

    def calculate_average(self):
        avg = sum(self.__marks) / len(self.__marks)
        print(f"Average Marks for {self.__name} : {avg:.2f}")

    def display_grade(self):
        avg = sum(self.__marks) /len(self.__marks)

        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 60:
            grade = 'D'
        else:
            grade = 'F'

        print(f"Final Grade: {grade}")

name = input("Enter Your Name : ")
marks1 = int(input("Enter Your maths marks :"))
marks2 = int(input("Enter Your science marks :"))
marks3 = int(input("Enter Your physical marks : "))

student1 = Student(name , marks1, marks2 , marks3)

student1.calculate_average()
student1.display_grade()
"""


