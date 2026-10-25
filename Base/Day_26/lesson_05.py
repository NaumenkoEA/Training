users = [
    {"name": "alina", "age": 20, "city": "solik"},
    {"name": "evgen", "age": 23, "city": "solik"},
    {"name": "bob", "age": 5, "city": "brest"},
    {"name": "vova", "age": 15, "city": "minsk"},
    {"name": "ronaldo", "age": 46, "city": "monaco"}
]

result = list(map(lambda x : x["name"] + " - " + str(x["age"]) ,filter(lambda x :x["city"] == "solik" ,users)))
print(result)