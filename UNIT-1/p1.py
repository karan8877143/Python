num=int(input("enter a number: "))
i=0
sum=0
p=0
n=1

for i in range(i,num+1):
    sum=p+n
    p=n
    n=sum
    print(sum)