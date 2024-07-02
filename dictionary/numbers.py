num={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
a=int(input("enter the number:"))
result=''
while a>0:
    d=a%10
    word=num[d]
    result=word+''+result
    a=a//10
    print(result)
