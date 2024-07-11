# f=open("new.txt","a")
# f.write("python program")
# f=open("new.txt","r")
# print(f.read())
# f=open("new.txt","r")
# print(f.read(5))
# print('_'*20)
# print(f.read(2))
# f=open("new.txt","r")
# print(f.readline(4))
# print('_'*20)
# print(f.readline(2))
# f=open("new.txt","r")
# print(f.readlines())
# print('_'*20)



# f=open("new.txt","r")
# l=len(f.readlines())
# f.seek(0)
# for i in range(l):
#     a=f.readline().strip()
#     print(a[::-1])

# f=open("new.txt","r")
# l=len(f.readlines())
# f.seek(0)
# word=0
# for i in range(l):
#     a=f.readline().strip()
#     for j in  a:
#         if j=='':
#             word+=1
#     print(a[::-1])
#     word+=1
# print(word)   


# f=open("new.txt","r")
# l=len(f.readlines())
# f.seek(0)
# word=0
# letters=0
# for i in range(l):
#     a=f.readline().strip()
#     for j in  a:
#         if j=='':
#               word+=1
#         else:
#                letters+=1
#     print(a[::-1])
#     word+=1
# print(word)
# print(letters)   

#capital and small letters:

f=open("new.txt","r")
l=len(f.readlines())
f.seek(0)
word=0
letters=0
cap=0
for i in range(l):
    a=f.readline().strip()
    for j in a:
        if j=='':
              word+=1
        else:
               letters+=1
               if j.isupper():
                    cap+=1
    print(a[::-1])
    word+=1
print(word)
print(letters) 
print(cap)
print(letters-cap)









