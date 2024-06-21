a=int(input("enter the number"))
rev=0
for i in range(a):
    d=a%10
    rev=(rev*10)+d
    a//=10
    if a==0:
        break
print(rev)