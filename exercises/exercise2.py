score = int(input("Enter your score: "))
if score > 100 or score < 0:
    print('Invalid score entered. Try again')
elif score >=80:
    print("Your grade is A")
elif score >= 70:
    print("Your grade is B")
elif score >= 60:
    print("Your grade is C")
elif score >= 50:
    print("Your grade is D")
elif score >= 40:
    print("Your grade is E")
else:
    print("Your grade is F")