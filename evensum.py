a=int(input("enter the starting number"))
b=int(input("enter the ending number"))
sum=0
i=a
while i<=b:
    if i%2==0:
        sum=sum+i
    i+=1
print(sum)

