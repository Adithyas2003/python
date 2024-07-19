# for i in range(1,6):
#     for j in range(i):
#         print((i+j)%2,end='')
#     print()
        
# pattern2:
for i in range(1,6):
    for j in range(i):
        if i%2==0:
            print('+',end='')
        else:
            print('#',end='')
    print()