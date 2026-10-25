players = [
    {"name": "Alex", "age": 23},
    {"name": "Max", "age": 25},
    {"name": "John", "age": 21},
    {"name": "Mike", "age": 24}
]


for number,player in enumerate(players,start=1):
    player["age"] += 1
    print(player["name"], "-",player["age"])