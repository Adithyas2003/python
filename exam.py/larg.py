l=[1,3,4,11,3,'abc',8]
n=l[0]
for i in l:
    if type(i)==int or type(i)==float:
        if i>n:
            n=i
print(n)