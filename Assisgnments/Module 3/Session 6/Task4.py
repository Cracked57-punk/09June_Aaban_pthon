class USER:
    def __init__(self):
        self.username = input("Enter your username:")
        self.email = input ("Enter your email:")

    def printdata(self):
        print(f"Username: {self.username}\nEmail:{self.email}")

class Influencer(USER):
    def __init__(self):
        super().__init__()
        self.followers = int(input("Enter your followers:"))

    def printdata(self):
        super().printdata()
        print(f"Followers:{self.followers}")

class Brand:
    def __init__(self):
        self.brand_name = input("Enter your brand name: ")
    def printdata(self):
        print(f"Brand name is:{self.brand_name}")

class BrandPartner(Brand,Influencer):
    def __init__(self):
        Influencer.__init__(self)
        Brand.__init__(self)

    def printdata(self):
        Influencer.printdata(self)
        Brand.printdata(self)
        
        

Brndprtnr =BrandPartner()
Brndprtnr.printdata()