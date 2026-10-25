class Team :
    def __init__(self,players):
        self.players =players

    def __len__(self):
        return len(self.players)




players = ["Alex", "Max", "John"]

team = Team(players)

print(team.players)
print(len(team))