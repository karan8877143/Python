# Use appropriate functions for each classWrite a program to display MRO using 
# multiple inheritance. Multiple inheritance can be done as per your choice.

class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):   
    pass

obj=C()
obj.show()
print("MRO",C.mro())