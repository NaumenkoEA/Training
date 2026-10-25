players = [
    {"name": "Alex", "age": 23, "score": 85},
    {"name": "John", "age": 21, "score": 91},
    {"name": "Mike", "age": 17, "score": 60},
]

result_all = all(player["score"] >= 50 for player in players)
result_any = any(player["score"] >= 90 for player in players)

print(result_any)