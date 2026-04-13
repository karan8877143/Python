# Write a program to overload addition (+) and subtraction (-) (Use 
# appropriate methods to overload the same.

class Number:
    def __init__(self):
        self.num1 =int(input("enter first number: "))
        self.num2 =int(input("enter first number: "))

    # def __add__(self):
    #     return self.num1 + self.num2

    # def __sub__(self):
    #     return self.num1 - self.num2
    
    
    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

obj=Number()
# print("Addition: ",obj.__add__())
# print("Subtraction: ",obj.__sub__())
print("Subtraction: ",obj.add())
print("Subtraction: ",obj.sub())

