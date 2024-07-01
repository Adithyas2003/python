dtl=[{'name':'anu','age':20},{'name':'appu','age':45},{'name':'manu','age':35}]
for i in range(0):
    name=input('name')
    age=int(input('age'))
    dtl.append({'name':name,'age':age})
print("{:<10}{:<6}".format("name","age"))
print('_'*20)
for i in dtl:
    print("{:<10}{:<6}".format(i['name'],i['age']))

print('age>30')
print("{:<10}{:<6}".format("name","age"))
for i in dtl:
    if i['age']>=30:
        print("{:<10}{:<6}".format(i['name'],i['age']))
        
       
print('age<30')
print("{:<10}{:<6}".format("name","age"))
for i in dtl:
    if i['age']<30:
        print("{:<10}{:<6}".format(i['name'],i['age']))