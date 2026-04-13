# Write a program to make use of inner class
# An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.

class Outer:
    def __init__(self):
        self.name="Outer Class"
    
    class Inner:
        def __init__(self):
            self.name="Inner Class"
        def display(self):
            print("this a inner claas functions")
obj=Outer()
print(obj.name)

inner=Outer.Inner()
print(inner.name)
print(inner.display())
