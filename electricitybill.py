a=int(input("enter the number of unit"))
if a>=100:
    print("no charge")
elif 100<a >=200:
    charge=100*5
    print("Rs 5 per unit")
else:
    charge=200*10
    print("Rs 10 per unit")
    