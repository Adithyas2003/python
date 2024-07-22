# class A:
#     def __init__(s,name,age):
#         print("A class display method")
#     def s1(s):
#         print("A class s1")
# class B(A):
#     def __init__(s,name,age):
#         print(name,age)
#         print("B class display method")
#         super().__init__(name,age)
#     def d1(s):
#         print("B class d1")
# obj=B('akhil',25)


# abstract method:


# from abc import ABC,abstractmethod
# class animal(ABC):
#     @abstractmethod
#     def make_sound(s):
#         print('sound')
# class birds(animal):
#     def fly(s):
#         print('fly')
#     def make_sound(s):
#         print('bird sound')
# class cat(animal):
#     def run(s):
#         print('run')
#     def make_sound(s):
#         print('cat sound')
# b1=birds()
# b1.fly()
# b1.make_sound()
# print('cat')
# c1=cat()
# c1.run()



# regularexpression:


# a='welcome'
# import re

# print(re.sub('w','W',a))
# print(re.split('e',a))
# print(re.split('e',a,1))
# print(re.sub('welcome','python',a))

# b='hai3'
# import re
# print(re.sub('hai','hai hello',b))
# print(re.search('a',b))
# print(re.search('z',b))
# if re.search('z',b):
#     print("yes")
# else:
#     print("no")

# if re.search('l',b):
#     print("yes")
# else:
#     print("no")

# print(re.search('[a-z]',b))
# print(re.search('[0-9]',b))

#dot:
# a='Hello2'
# import re
# print(re.search('e.',a))

# #star:
# print(re.search("h.*",a))
# # plus:
# print(re.search('l.+',a))
# # ?:
# print(re.search('o.?',a))

# print(re.search('[a-z]',a))
# print(re.search('[A-Z]',a))
# print(re.search('[0-9]',a))
# print(re.search('[a-z].',a))
# print(re.search('[a-z]..',a))
# print(re.search('[a-z].?',a))


# import re
# a='HAIhello32'
# print(re.search('[a-z]',a))
# print(re.search('[a-z][0-9]',a))
# print(re.search('[a-z][0-9]',a))
# print(re.search('[A-Z][a-z][0-9][0-9]',a))
# print(re.search('[A-Z].*[a-z][0-9][0-9]',a))


# import re
# b='welcome45'
# print(re.search('[A-Za-z0-9]',b))
# print(re.search('[0-9]$',b))
# print(re.search('5$',b))
# print(re.search('welcome45$',b))

#phone number validation:
# import re
# a=input("enter number")
# if len(a)==10 and a.isdigit() and re.search('[6-9].{9}',a):
#     print("valid")
# else:
#     print("invalid")

#email validation:
import re
a=input("enter your email Id")
pattern="[a-z].*@gmail.com"
if re.search(pattern,a):
    print("valid")
else:
    print("invalid")


