users = [
    {"name": "Alina", "age": 20, "city": "Solik"},
    {"name": "Evgen", "age": 23, "city": "Solik"},
    {"name": "Ronaldo", "age": 46, "city": "Monaco"}
]

def find_users_older_than(users, age):
    result = []
    for user in users :
        if(user["age"] > age):
            result.append(user)
    return result

older_users = find_users_older_than(users,24)

print(older_users)