from functools import reduce
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

    def all_adults(self):
        return all(player.age >=18 for player in self.players)

    def get_players_sorted_by_age(self):
        return sorted(self.players , key = lambda player : player.age)

    def get_players_sorted_by_name(self):
        return sorted(self.players , key = lambda player : player.name , reverse=True)

    def get_young_players(self):
        young_players = [player for player in self.players if player.age <18]
        return sorted(young_players , key = lambda player : player.age)

team = Team("Minsk")

team.add_player(Player("Alex", 23))
team.add_player(Player("Max", 16))
team.add_player(Player("John", 21))
team.add_player(Player("Mike", 17))

total_age =reduce(lambda a, b: a + b , map(lambda player: player.age , team.players))
max_age =reduce(lambda a, b: a if a>b else b , map(lambda player: player.age , team.players))



players_map_filter = list(
    map(
        lambda player : (player.name, player.age),
        filter(lambda player : player.age >= 18, team.players)
        )
    )

players_map_sorted = list(
    map(
        lambda player : (player.name , player.age),
        sorted(team.players , key = lambda player : player.age ,reverse= True)
    )
)

print(players_map_sorted)