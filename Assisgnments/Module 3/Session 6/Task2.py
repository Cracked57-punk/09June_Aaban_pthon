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

inf1 = Influencer()
inf1.printdata()