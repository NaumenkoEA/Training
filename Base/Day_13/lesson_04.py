users = [
    {"name": "Alina", "age": 20, "city": "Solik"},
    {"name": "Evgen", "age": 23, "city": "Solik"},
    {"name": "Ronaldo", "age": 46, "city": "Monaco"}
]

def find_youngest_user(users):
    young = users[0]
    for user in users:
        if(young["age"]> user["age"]):
            young = user
    return young

youngest = find_youngest_user(users)

print(youngest["name"], " - ",youngest["age"])