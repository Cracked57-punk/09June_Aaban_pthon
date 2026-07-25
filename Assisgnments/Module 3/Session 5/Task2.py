class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def show_order(self):
        print(f"Restaurant: {self.restaurant_name}")
        print("Items ordered: ")
        for i in self.items :
            print(f"- {i}")
        print(f"Total Price: ₹{self.total_price}")

order1 = FoodOrder("Domino's Pizza", ["Margherita Pizza", "Garlic Bread", "Coke"], 549)
order1.show_order()