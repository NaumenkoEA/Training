users = [
    {"name": "Alina", "age": 20, "city": "Solik"},
    {"name": "Evgen", "age": 23, "city": "Solik"},
    {"name": "Ronaldo", "age": 46, "city": "Monaco"}
]

def show_users(users):
    for user in users:
        if(user["age"] > 22):
            print(user["name"])


show_users(users)