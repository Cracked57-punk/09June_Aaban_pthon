class ZomatoOrder:
    def add_item(self,item,quantity=1):
        print(f"Added {quantity}x{item} to the order")



order = ZomatoOrder()
order.add_item("Pizza")        
order.add_item("Burger", 3)
