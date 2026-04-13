
#Write a program to create a simple class with 2 methods and execute both methods
class Simple:
    def __init__(self):
        self.a=int(input("Enter First Number:"))
        self.b=int(input("Enter Second Number:"))
    def add(self):
        c=self.a+self.b
        print("Sum of two numbers: ",c)
    def sub(self):
        c=self.a-self.b
        print("Sub of two numbers: ",c)
obj=Simple()
obj.add()
obj.sub()