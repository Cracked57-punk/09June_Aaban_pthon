#bmi_calc.py

import math


class bmi_calc:
    def __init__(self) :
        while True:
            try:
                self.height = float(input("Enter your height in meters: "))
                if self.height<=0:
                    raise ValueError("Your height should be positive.")
                else : 
                    break
            except ValueError:
                print("Invalid input! Please enter a valid positive number for height.")
        while True:
            try:
                self.weight = float(input("Enter your weight in kgs: "))
                if self.weight<=0:
                    raise ValueError("Your weight should be positive.")
                else :
                    break
            except ValueError:
                print("Invalid input! Please enter a valid positive number for weight.")    
        result = self.weight/math.pow(self.height,2)
        print(f"Your bmi is:{result:.2f}")



user=bmi_calc()
