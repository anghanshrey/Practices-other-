import email


print("="*40)
print("Q-1")
print("="*40)

"""
number = int(input("Enter a Number : "))

if number < 0:
    raise ValueError("User enters a negative number.")

print("Number : ", number)
"""

print("="*40)
print("Q-2")
print("="*40)
"""
def check_even(number):

    if number == int:
        raise TypeError("The input is not an integer.")
    if number%2 == 1:
        raise ValueError("The number is odd.")
    print(f"Even Number is : {number}")

number = int(input("Enter a Number : "))

check_even(number)
"""

print("="*40)
print("Q-3")
print("="*40)

"""
try:
    age = int(input("Enter Your age: "))

    assert age > 18, "Age must be above 18!"
    print("Access granted")
except AssertionError as e:
    print(f"AssertionError: {e}")
except ValueError:
    print("please enter a vaild inter for age.")
"""

print("="*40)
print("Q-4")
print("="*40)

"""
def check_palindrome(s):
    assert len(s) > 0, "The input String cannot be empty!"

    cleaned = s.replace(" ","").lower()
    is_for = cleaned == cleaned[::-1]
    return is_for

try:
    print(check_palindrome("radar"))
    print(check_palindrome(""))
except AssertionError as e:
    print("Error", e)
"""

print("="*40)
print("Q-5")
print("="*40)
"""
class InsufficientBalanceError(Exception):
    pass

class BankAccount:

    def __init__(self, balance = 0):
        self.__balance = balance

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientBalanceError(f"Your Withdrawal amount {amount} and current balance is {self.__balance}")
        self.__balance -= amount
        print(f"Sucessfully withdraw ${amount}. Remaining balance: ${self.__balance}")

try:
    bank = BankAccount(1000)

    bank.withdraw(900)
    bank.withdraw(200)
except InsufficientBalanceError as e:
    print("Error:", e)
"""

print("="*40)
print("Q-6")
print("="*40)

"""
class InvalidEmailError(Exception):
    pass

class User_Email:

    def __init__(self, email):
        self.email = email

    def checkemail(self):
        if "@" not in self.email:
            raise InvalidEmailError("Email must contain an '@' symbol.")
        if not (self.email.endswith(".com") or self.email.endswith(".org")):
            raise InvalidEmailError("Email must end with .com or .org.")
        print(f"'{self.email}' is a valid email.")

try:
    User = User_Email("john@example.com")
    User.checkemail()
    User1 = User_Email("johnexample.com")
    User1.checkemail()
except InvalidEmailError as e:
    print("Error:", e)
"""

print("="*40)
print("Q-7")
print("="*40)

"""
class InvaildGradeError(Exception):
    pass

class grade:

    def __init__(self, marks):
        self.marks = marks

    @property
    def check_grade(self):
        assert self.marks.strip() != "", "The input is not empty."

        self.marks = int(self.marks)

        if self.marks < 0 or self.marks > 100:
            raise ValueError("The grade is not between 0 and 100.")
        if self.marks < 40:
            raise InvaildGradeError("The grade is below 40 (failing grade.)")
        if self.marks > 90:
            print("grade A.")
        elif self.marks > 80:
            print("grade B.")
        elif self.marks > 70:
            print("grade c.")
        else:
            print("grade d.")

try:
    marks = input("Enter Your Marks : ")
    Grade = grade(marks)

    Grade.check_grade
except InvaildGradeError as e:
    print("Error :",e)
except AssertionError as e:
    print("Error :",e)
except ValueError as e:
    print("Error :",e)
finally:
    print("Thank you.")
"""

print("="*40)
print("Q-8")
print("="*40)

"""
class HighTemperatureError(Exception):
    pass

def Convert_c_to_f(temp_input):

    if temp_input == (int,float):
        raise TypeError("Temperature input must be a number.")

    assert temp_input >= -273.15 and temp_input <=10000, "Temperature out of planetary bounds!"

    if temp_input > 1000:
        raise HighTemperatureError("Temperature Exceeds 1,000c.")

    fach = (temp_input * 9/5) + 32
    return fach

try:
    print(f"25c to Fachrenheit: {Convert_c_to_f(25)}")
    Convert_c_to_f(1500)
except (TypeError, AssertionError, HighTemperatureError) as e:
    print(f"Validation Error: {e}")
"""