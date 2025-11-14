litres = float(input("How many litres of fuel do you need? "))
unit_price = 12.50
if litres > 50:
    total_cost = (litres*unit_price)*0.95
    print(f"Your total price is {total_cost}")
else:
    if litres < 0:
        print("Invalid value entered")
    else:
        total_cost = litres*unit_price
        print(f"Your total price is {total_cost}")