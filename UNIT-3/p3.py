# Write a program to make use of class method and instance method.
# Instance Method: A method that works on object data using self.
# Class Method: A method that works on class data using cls and @classmethod.

class Student:
    university="Marwadi University, Rajkot"  #class variable
    
    def __init__(self):
        #instance variable
        self.name=input("enter name: ")
        self.mark=int(input("enter marks: "))
        
        
    #instance method   
    def StudentInfo(self):
        print("name: ",self.name)
        print("mark: ",self.mark)
    
    
    #class method
    @classmethod
    def UniversityInfo(cls):
        print("University Name: ",cls.university)

obj=Student()
obj.StudentInfo()
obj.UniversityInfo()