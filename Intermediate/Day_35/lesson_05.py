players = [
    {"name": "Alex", "age": 23, "score": 85},
    {"name": "Max", "age": 16, "score": 72},
    {"name": "John", "age": 21, "score": 91},
    {"name": "Mike", "age": 17, "score": 60},
]


def get_adult_players(players):
    adults = [player for player in players if player["age"] >= 18]

    if not adults:
        return None

    return sorted(adults, key=lambda player: player["score"], reverse=True)


def get_top_adults(players):
    adults = [
        player
        for player in players
        if player["age"] >= 18 and player["score"] >= 80
    ]

    if not adults:
        return None

    sorted_players = sorted(
        adults,
        key=lambda player: player["score"],
        reverse=True
    )

    return list(map(lambda player: player["name"], sorted_players))