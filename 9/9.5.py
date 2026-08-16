print("="*40)
print("Q-1")
print("="*40)

"""
from abc import ABC,  abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

try:
    shape_obj = Shape()
except TypeError as e:
    print(f"Error sucessfully raised: {e}\n")

rect = Rectangle(5, 10)
circle = Circle(7)

print(f"Rectangle Area : {rect.area()}")
print(f"Circle Area : {circle.area():.2f}")
"""

print("="*40)
print("Q-2")
print("="*40)

"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @ abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width *self.height

    def perimeter(self):
        return 2 * (self.width * self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class incompleteshape(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

rect = Rectangle(5, 10)
circle = Circle(5)

print(f"Rectangle - Area: {rect.area()}, perimeter: {rect.perimeter()}")
print(f"Circle - Area: {circle.area():.2f} , perimeter: {circle.perimeter():.2f}")

try:
    bad_shape = incompleteshape(5)
except TypeError as e:
    print(f"Observerd Error: {e}")
"""

print("="*40)
print("Q-3")
print("="*40)

"""
from abc import ABC, abstractmethod

class MLModel(ABC):
    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, new_data):
        pass

class LinerRegressionModel(MLModel):
    def train(self, data):
        print(f"Training Liner Regression model using math formulas on: {data}")

    def predict(self, new_data):
        print(f"Liner Regression predicting continous value for: {new_data}")
        return [1.5, 2.3]

class DecisionTreeModel(MLModel):
    def train(self, data):
        print(f"Training Decision Tree model by splitting nodes on: {data}")

    def predict(self, new_data):
        print(f"Decision Tree predicting classification category for: {new_data}")
        return ['Class A', 'Class B']

lr_model = LinerRegressionModel()
dt_model = DecisionTreeModel()

models = [lr_model, dt_model]

dummy_training_set = "Housing Dataset 2026"
dummy_test_features = [5.1, 3.5]

for model in models:
    print(f"Using model type: {type(model).__name__}")
    model.train(dummy_training_set)
    predictions = model.predict(dummy_test_features)
    print(f"Results: {predictions}")
    print("="*50)
"""

print("="*40)
print("Q-4")
print("="*40)

from abc import ABC, abstractmethod

class Account(ABC):      

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class BankAccount(Account):
    
    def __init__(self, account_number, balance=0.0):
        self.__account_number = account_number
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):  
        self.__balance = amount

    def get_account_number(self):
        return self.__account_number

    def deposit(self, amount):  
        if amount > 0:
            current_bal = self.get_balance()
            self.set_balance(current_bal + amount)
            print(f"Deposited ${amount:.2f} into Account {self.__account_number}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):  
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        current_bal = self.get_balance()
        if current_bal >= amount:
            self.set_balance(current_bal - amount)
            print(f"Withdrew ${amount:.2f} from Account {self.__account_number}")  
            return True
        else:
            print(f"Transaction Failed: Insufficient Funds in Account {self.__account_number}.")  
            return False

class SavingAccount(BankAccount):
    def __init__(self, account_number, balance=0.0, interest_rate = 0.05):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest:.2f} added at a rate of {self.interest_rate * 100}%.")

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance = 0.0, overdraft_limit = 300.0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):  
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        current_bal = self.get_balance()

        if current_bal + self.overdraft_limit >= amount:
            self.set_balance(current_bal - amount)
            print(f"Withdrew ${amount:.2f} (Using Overdraft) from Account {self.get_account_number()}")
            return True
        else:
            print(f"Transaction failed: Exceeded overdraft limit of ${self.overdraft_limit:.2f}.")
            return False

# --- Verification & Demonstration ---

savings = SavingAccount("SAV-101", 2000.0, 0.05)
current = CurrentAccount("VDE-202", 200.0, 300.0)

print(f"Savings initial balance: ${savings.get_balance():.2f}")
print(f"Current initial balance: ${current.get_balance():.2f}\n")

print("--- Running Savings Transactions ---")
savings.deposit(500.0)
savings.withdraw(200.0)
savings.add_interest()
print(f"Final Savings Balance: ${savings.get_balance():.2f}\n")

print("--- Running Current Transactions ---")
current.deposit(100.0)
current.withdraw(200.0)
print(f"Current Account Balance (Overdrawn): ${current.get_balance():.2f}\n")

print("--- Testing Overdraft Breach ---")
current.withdraw(100.0) 
