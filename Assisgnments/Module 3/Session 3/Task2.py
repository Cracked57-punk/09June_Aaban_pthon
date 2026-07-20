try:
    price = int(input("Enter the price of the item:"))
    quantity = int(input("Enter the quantity of the item:"))
    total=price*quantity
    print(f"The total cost of the item is:{total}")
    
except ValueError:
    print("Please enter numeric values.")