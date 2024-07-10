# a=20
# def fun1():
#     global b
#     b=10
#     print('welcome',b)
# fun1()
# print("outside",b)
# a=20
# def fun1():
#      global b
#      b=10
#      print('welcome',b)
#      c=25
#      return c,74
# c1,d1=fun1()
# print("outside",c1,d1)

#positional argumnt:

# def add(a,b):
#     return a+b
# print(add(10,20))
# print(add(10,30))
# print(add('asd','a2123'))

#default parameter:

# def add(name,age=23):
#     return name,age
# print(add('anu',22))
# print(add('sanu'))

#keyword argument:

# def add (name,age):
#     print("name:",name)
#     print("age:",age)
# add('anu',25)
# add(age=23,name='sanu')

#arbitary argument

# def add(*a):
#     return a
# print(add('anu',24))
# print(add())


def add(**a):
    return a
print(add(name='anu',age=23))
print(add())