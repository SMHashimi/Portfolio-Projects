print("Welcome to the Tip Calculator")
bill = float(input("The bill: "))
tip = int(input("How much tip? 10, 12, or 15: "))
people = int(input("How many people to split the bill with? "))

def tip_calc():
    tip_amount = (tip / 100) * bill
    total_bill = round(((tip_amount + bill) / people), 2)
    print(f"Each Individual Should Pay: {total_bill}")

tip_calc()












