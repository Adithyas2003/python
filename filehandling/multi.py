# a=int(input("enter the number"))
# f=open('python/filehandling/table.txt','w')
# for i in range(1,11):
#     b=str(i)+'*'+str(a)+'='+str(i*a)+'\n'
#     f.write(b)


a=int(input('enter the number'))
f=open('python/filehandling/table2.txt','w')
for a in range(1,a+1):
    f.write(f"table of {a}:\n")
    for i in range(1,11):
        b=f'{i}*{a}={i*a}\n'
        f.write(b)
    f.write("\n")
f.close()        
