class Player:
    def __init__(self, name, age,team):
        self.name = name
        self.age = age
        self.team = team

    def __eq__(self, value):
        if not isinstance(value, Player):
            return False
        return self.name == value.name and self.age == value.age and self.team == value.team



player1 = Player("Alex", 25, "Minsk")
player2 = Player("Alex", 25, "Minsk")

print(player1 == player2)
print(player1 == 10)
print(player1 == "Alex")