std=[]
while True:
    print("1.add \n 2.view \n 3.update \n 4.delete \n 5.exit \n")
    ch=int(input("enter your choice"))
    if ch==1:
        name=input("enter the name")
        age=int(input("enter the age"))
        cls=input("enter the class")
        std.append([name,age,cls])
    elif ch==2:
        for i in std:
            print(i)
    elif ch==3:
        f=0
        a_name=input("enter name")
        for i in std:
            if a_name in i:
                age=int(input("enter new age"))
                i[1]=age
                f=1
            if f==0:
                print("std not available")
    elif ch==4:
        a_name=input("enter the name")
        f=0
        for i in std:
            if a_name in std:
                std.remove(i)
                f=1
        if f==0:
            print("not available")
    elif ch==5:
        break