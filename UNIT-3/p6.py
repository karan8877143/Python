# Write a Python Program that creates a class and inherit into another class (Base Class : Student with 
# rollno, name, gender, age) (Derived Class : Course with coursename, duration, fee)

class Student:
    def __init__(self):
        self.name=input("enter student name: ")
        self.rollno=int(input("enter student rollno: "))
        self.gender=input("enter student gender: ")
        self.age=int(input("enter student age: "))
    def displayStudent(self):
        print("\n-----Student Information-----\n")
        print("Name: ",self.name)
        print("Roll No: ",self.rollno)
        print("Gender: ",self.gender)
        print("Age: ",self.age)
        
class Course(Student):
    def __init__(self):
        super().__init__()
        self.coursename=input("enter course name: ")
        self.duration=input("enter course duration: ")
        self.fee=int(input("enter course fees: "))
        
    def displayCourse(self):
        self.displayStudent()
        print("Course Name: ",self.coursename)
        print("Course Duration: ",self.duration)
        print("Course Fee: ",self.fee)
        
obj=Course()
obj.displayCourse()