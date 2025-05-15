print("Welcome to XYZ Super Market")
total_amount = 0

while True:
    name = input("Enter your name: ")
    while True:
        itemName = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        item_quantity = int(input("Enter item quantity: "))
        total_amount += item_price * item_quantity
        
        repeat = input("Do you want to add more items? ")
        if (repeat == "N" or repeat == "n"):
            break
    print("Total amount due for", name, "is", total_amount)
    
    repeat = input("Do you want to add another bill? ")
    total_amount = 0
    if (repeat == "N" or repeat == "n"):
        break