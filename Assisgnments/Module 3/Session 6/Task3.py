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

class VerifiedInfluencer(Influencer):
    def __init__(self):
        super().__init__()
        answer = input("Is this user verified? (yes/no): ")
        self.badge = answer.lower() == "yes"                #very good use of == operator comparing strings to get an answer in bool.

    def printdata(self):
        super().printdata()
        if self.badge:
            print("Verified!")
        else: 
            print("Not Verified!")

verinf1 = VerifiedInfluencer()
verinf1.printdata()