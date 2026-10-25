users = [
    {"name": "Alina", "age": 20, "city": "Solik"},
    {"name": "Evgen", "age": 23, "city": "Solik"},
    {"name": "Ronaldo", "age": 46, "city": "Monaco"}
]

def find_users_by_city(users,city):
    result = []
    for user in users:
        if(user["city"] == city):
            result.append(user)
    return result

solik_users = find_users_by_city(users,"Solik")

print(solik_users)