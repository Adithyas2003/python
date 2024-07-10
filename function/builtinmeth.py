#map:

# l=[1,2,3,4,5]
# data=map(lambda a:a**2,l)
# print(data)
# print(list(data))

# def fun1(a):
#     return a**2
# data1=map(fun1,l)
# print(list(data1))

#filter:

# l=[1,2,3,4,5]
# data=filter(lambda a:a%2==0,l)
# print(list(data))
# def fun1(a):
#     return a>=3
# data1=filter(fun1,l)
# print(list(data1))

# l=['apple','mango']
# def fun1(a):
#     return a[0]=='a'
# data1=filter(fun1,l)
# print(list(data1))

#reduce:

# import functools
# l=[1,2,3,4,5]
# data=functools.reduce(lambda total,value:total*value,l)
# print(data)

import functools
l=[1,2,3,4,5]
data=functools.reduce(lambda total,value:total+value,l)
print(data)
