route = input("Enter your travel route: ")
passengers = input("How many passengers are boarding: ")
if route == 'Accra to Madina':
    fare = passengers * 5
    print(f"Your total fare is GHS{fare}")
elif route == 'Accra to Kasoa':
    fare = passengers * 10
    print(f"Your total fare is GHS{fare}")
elif route == 'Accra to Tema':
    fare = passengers * 8
    print(f"Your total fare is GHS{fare}")
else:
    print('Enter a valid route')