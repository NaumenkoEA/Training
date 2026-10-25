from dataclasses import dataclass ,field


@dataclass
class Team:
    name: str
    players: list[str] = field(default_factory=list)
    

    def __len__(self) -> int:
        return len(self.players)


team1 = Team("Minsk")
team2 = Team("Gomel")

team1.players.append("Alex")

print(team1)
print(team2)