# Write a program to create a class for student with RollNo, Name, Age, 
# Gender and methods named AddStudent() and DisplayStudent()

class Student:
    def AddStudent(self):
        self.name=input("enter name: ")
        self.rollno=int(input("enter rollno: "))
        self.age=int(input("enter age: "))
        self.gender=input("enter gender: ")
    
    def DisplayStudent(self):
        print("\n-----Student Deatails-----\n")
        print("name: ",self.name)
        print("rollno: ",self.rollno)
        print("age: ",self.age)
        print("gender: ",self.gender)
obj=Student()
obj.AddStudent()
obj.DisplayStudent()