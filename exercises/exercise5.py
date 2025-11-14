amount = int(input("Enter amount you would like to transfer: "))
if amount <= 0:
    print("Invalid amount entered")
elif amount <= 100:
    charge = 2
    final = amount - charge
    print("The recipient will receive GHS",final)
elif amount > 100 and amount <= 500:
    charge = 5
    final = amount - charge
    print("The recipient will receive GHS",final)
elif amount > 500:
    charge = 10
    final = amount - charge
    print("The recipient will receive GHS",final)