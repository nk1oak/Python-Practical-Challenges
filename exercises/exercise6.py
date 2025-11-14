name = input("Enter your full name: ")
age = int(input("Enter your age: "))
nationality = input("What nationality are you? ").lower()
if age >= 18 and nationality == 'ghanaian':
    print(f"{name}, you are eligible to vote")
else:
    print(f"{name}, you are not eligible to vote")