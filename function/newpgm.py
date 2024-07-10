# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b

# def div(a,b):
#     return a/b
# def numbers():
#     a=int(input("enter the frst number"))
#     b=int(input("enter the second number"))
#     return a,b
# while True:
#     print("1.add \n 2.sub \n 3.mul \n 4.div \n 5.exit \n")
#     ch=int(input("enter ur choice"))
#     if ch==1:
#         a,b= numbers()
#         print(add(a,b))
#     elif ch==2:
#         a,b= numbers()
#         print(sub(a,b))
#     elif ch==3:
#         a,b= numbers()
#         print(mul(a,b))
#     elif ch==4: a,b= numbers()
#         print(add(a,b))
#         a,b= numbers()
#         print(div(a,b))
#     elif ch==5:
#         break
#using lambda:
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
mul=lambda a,b:a*b
div=lambda a,b:a/b

def numbers():
    a=int(input("enter the frst number"))
    b=int(input("enter the second number"))
    return a,b
while True:
    print("1.add \n 2.sub \n 3.mul \n 4.div \n 5.exit \n")
    ch=int(input("enter ur choice"))
    if ch==1:
        a,b= numbers()
        print(add(a,b))
    elif ch==2:
       a,b= numbers()
       print(sub(a,b))
    elif ch==3:
        a,b= numbers()
        print(mul(a,b))
    elif ch==4: 
        a,b= numbers()
        print(div(a,b))
    elif ch==5:
        break
