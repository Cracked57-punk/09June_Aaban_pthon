
Coupons =['ZOMATO50','FLAT100','FRISTORDER','WEEKEND10']\


class InvalidCouponCode(Exception):
    def __init__(self,coupon) :
        self.coupon= coupon
        super().__init__(f"'{coupon}' is not valid coupon!\n")



def applycouponcode():
    coupon = input("Enter Coupon code here:").upper().replace(" ","")
    #replace(" ","") this is to make no space in between the whole  input

    if coupon not in Coupons:
        raise InvalidCouponCode(coupon)
    else :
        print(f"The coupon '{coupon}' is applied !!")


try:
    applycouponcode()
except InvalidCouponCode as e:
    print(e)