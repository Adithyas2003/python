
from reg import *
from display import *
from update import *
from delete import *
data=[{"id": "1", "name": "anu", "age": "22", "place": "kottayam"},
    {"id": "2", "name": "krish", "age": "23", "place": "alappuzha"},]
while True:
    print("1.Add \n2.Display \n3.Update \n4.Delete \n5.Exit")
    ch=int(input("Enter your choice : "))
    if ch == 1:
        register(data)
    elif ch == 2:
        display(data) 
    elif ch == 3:
        update(data)
    elif ch == 4:
        delete(data)
    elif ch == 5:
        print("You had exited")
        break
    else:
        ("Invalid input")

