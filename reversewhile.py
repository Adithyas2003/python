a=int(input("enter the number"))
rev=0
i=a
while i>=0:
    d=a%10
    rev=(rev*10)+d
    a//=10
print(rev)
    