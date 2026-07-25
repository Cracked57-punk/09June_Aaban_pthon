class USER:
    def __init__(self):
        self.username = input("Enter your username:")
        self.email = input ("Enter your email:")

    def printdata(self):
        print(f"Username:{self.username}")


class Influencer(USER):
    def __init__(self):
        super().__init__()
        self.followers = int(input("Enter your followers:"))

    def printdata(self):
        super().printdata()



class VerifiedInfluencer(Influencer):
    def __init__(self):
        super().__init__()
        answer = input("Is this user verified? (yes/no): ")
        self.badge = answer.lower() == "yes"

    def helper(self):
        if self.followers >= 1_000_000:
            return f"{self.followers / 1_000_000:.1f}M"
        elif self.followers >= 1_000:
            return f"{self.followers / 1_000:.1f}K"
        else:
            return str(self.followers)                

    def display_info(self):
        print("-----User Info-----")
        super().printdata()
        print(f"Followers {self.helper()}")
        if self.badge:
            print("Badge: Verified!")
        else: 
            print("Badge: Not Verified!")

verinf1 = VerifiedInfluencer()
verinf1.display_info()

