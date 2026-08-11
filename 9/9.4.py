print(" ================== ")
print(" Q-1 ")
print(" ================== ")

class Sum():

    def __init__(self, a , b , name1 , name2):
        self.a = a
        self.b = b
        self.name1 = name1
        self.name2 = name2

    def get_number(self):
        return self.a + self.b

    def get_string(self):
        return self.name1 + self.name2

s = Sum(10 , 5 , "Shrey " , " Anghan")
print("Sum of  2 Number : "s.get_number())
print("Concatenation of 2 string : "s.get_string())
        

    
