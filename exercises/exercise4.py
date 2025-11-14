market_women = {'Akosua':'200','Ama':'150','Adwoa':300}
name = input("Enter the name whose price you want to update: ")
amount = int(input("Enter new amount: "))
if name in market_women:
    if amount < 0:
        print("Invalid amount entered")
    else:
        market_women[name] = amount
        print(market_women)
else:
    print("Sorry, name doesn't exist in the system.")