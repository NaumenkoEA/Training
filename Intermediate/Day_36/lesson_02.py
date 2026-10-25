from typing import Callable, TypedDict

class Player(TypedDict):
    name : str
    age : int
    score : int

players = [
    {"name": "Alex", "age": 23, "score": 85},
    {"name": "Max", "age": 16, "score": 72},
    {"name": "John", "age": 21, "score": 91},
    {"name": "Mike", "age": 17, "score": 60}
]


def get_top_players (players : list[Player])->list[Player]:
    score_players = [
        player 
        for player in  players 
        if player["score"] >=80 and player["age"] >= 18
        ]
    return sorted(score_players, key=lambda player: player["score"] , reverse= True)

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b


def apply_operation(a : int , b : int ,operation : Callable[[int, int],int]) -> int:
    return operation(a,b)

apply_operation(10, 3, subtract)
apply_operation(10, 3, multiply)