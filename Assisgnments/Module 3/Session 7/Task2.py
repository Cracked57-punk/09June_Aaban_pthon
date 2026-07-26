class Payment:
    def pay (self,amount):
        print(f"Paying amount: {amount}")

class UPI(Payment):
    def pay(self,amount):
        print(f"Paying {amount} via UPI")

payment = Payment()
payment.pay(int(input("Enter Payment amount:")))

upi = UPI()
upi.pay(int(input("Enter Payment amount via UPI:")))