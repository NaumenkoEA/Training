users = [
    {"name": "alina", "age": 20, "city": "solik"},
    {"name": "evgen", "age": 23, "city": "solik"},
    {"name": "bob", "age": 5, "city": "brest"},
    {"name": "vova", "age": 15, "city": "minsk"},
    {"name": "ronaldo", "age": 46, "city": "monaco"}
]


result= [user["city"] for user in users if user["age"] < 20]

print(result)