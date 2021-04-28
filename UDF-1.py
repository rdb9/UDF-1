#Given code:
def grocery(item,price):
    print("Item:",item)
    print("Price:",price)
grocery(item="sugar",price=50)
grocery(item="oil",price="80")

#my code:
def grocery(item,price=80):      #Here i made a change
    print("\nitem:",item)
    print("price:",price)
grocery(item="sugar",price=50)
grocery(item="oil")