players = [
    {"name": "Alex", "age": 23},
    {"name": "Max", "age": 25},
    {"name": "John", "age": 21},
    {"name": "Mike", "age": 24}
]

# letter = input("Enter first letter in the name player: ").lower()
# find_age =int(input("Enter age : "))
min_age = int(input("Enter minimum age : "))
found = False
count = 0
for player in players :
    if (min_age <= player["age"]):
        print(player["name"], "-", player["age"])
        found = True
        count += 1

if found:
    print("Found players:", count)
else:
    print("No players found!")