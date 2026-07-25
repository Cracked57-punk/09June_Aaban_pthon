class USER:
    def __init__(self):
        self.username = input("Enter your username:")
        self.email = input ("Enter your email:")

    def printdata(self):
        print(f"Username: {self.username}\nEmail:{self.email}")

userinfo=USER()
userinfo.printdata()