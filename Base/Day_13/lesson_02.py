users = [
    {"name": "Alina", "age": 20, "city": "Solik"},
    {"name": "Evgen", "age": 23, "city": "Solik"},
    {"name": "Ronaldo", "age": 46, "city": "Monaco"}
]

def show_users_from_city(users,city):
    for user in users:
        if(user["city"] == city):
            print(user["name"])

show_users_from_city(users,"Monaco")