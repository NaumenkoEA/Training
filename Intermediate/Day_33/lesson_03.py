from dataclasses import dataclass, field

@dataclass
class Team:
    name: str
    players: list[str] = field(default_factory=list)

    def add_player(self, name_players):
        # добавляет игрока в players
        self.players.append(name_players)

    def remove_player(self, name_players):
        if(name_players in self.players):
            self.players.remove(name_players)
            

    def has_player(self, name_players):
        return name_players in self.players

    def get_player_count(self):
        return len(self.players)

team = Team("Minsk")

team.add_player("Alex")
team.add_player("Max")
team.add_player("John")

print(team)
print(team.has_player("Max"))

team.remove_player("Max")

print(team)
print(team.has_player("Max"))

print(team.get_player_count())