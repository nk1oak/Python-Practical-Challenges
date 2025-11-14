teams = [
    {"name": "Kotoko", "points": 25},
    {"name": "Hearts", "points": 23},
    {"name": "Aduana Stars", "points": 18}
]
for team in teams:
    selected_team = input("Which team info do you want to change? ").lower()
    new_point = int(input("Enter number of points: "))
    if team["name"].lower() == selected_team:
        team["points"] = new_point
        break
print(teams)