class PaymentFailedError (Exception):
    def __init__(self, amount):
        super().__init__(f"'{amount}' is not valid for payment.")

def process_payment():
    paymnt = int(input("Enter amount of payment:"))
    if paymnt <=0 :
        raise PaymentFailedError(paymnt)
    else:
        print("Payment Successful")

try:
    process_payment()
except PaymentFailedError as e:
    print(e)
except ValueError as ve:
    print("Please enter a proper amount of payment.")