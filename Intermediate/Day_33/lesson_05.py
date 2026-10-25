from dataclasses import dataclass,field


@dataclass
class Player:
    name: str
    age: int


@dataclass
class Team:
    name:str
    players: list[Player] = field(default_factory=list)

    def add_player(self,player):
        self.players.append(player)

    def remove_player(self, name):
        for player in self.players:
            if name == player.name:
                self.players.remove(player)

    def has_player(self,name):
        return any(player.name == name for player in self.players)

    def get_adult_players(self):
        return [player for player in self.players if player.age >=18]

    def find_player(self,name):
            for player in self.players:
                if(player.name == name):
                    return player
                
            return None

team = Team("Minsk")

team.add_player(Player("Alex", 23))
team.add_player(Player("Max", 16))
team.add_player(Player("John", 21))
team.add_player(Player("Mike", 17))


print(team)
print(team.has_player("Alex"))
print(team.has_player("Bob"))
print(team.get_adult_players())
print(team.find_player("John"))
print(team.find_player("Bob"))

team.remove_player("Max")

print(team)