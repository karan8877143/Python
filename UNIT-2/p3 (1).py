a=int(input("enter number 1:"))

def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
fact(a)

def recfact(num):
    if num < 0:
        return "Factorial not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1) 

print(recfact(a))
