def register(data):
    name=input("enter the name")
    age=int(input("enter the age"))
    id=input("enter the id")
    place=input("enter the place")
    data.append({'name':name,'age':age,'id':id,'place':place})