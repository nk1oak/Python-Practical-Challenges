num_of_bags = int(input("Enter number of bags harvested: "))
total_income = num_of_bags * 850
if num_of_bags > 100:
    total_income = (num_of_bags * 850) + 2000
    print("GHS",total_income)
else:
    print("Your total income is GHS",total_income)