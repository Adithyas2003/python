#duplicate list in a loop:
l=[1,2,3,1,2,3]
a=[]
b=set()
for i in l:
    if i not in b:
        a.append(i)
        b.add(i)
print(a)
