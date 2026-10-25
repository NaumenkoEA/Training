users = [
    {"name": "Alina", "age": 20, "city": "Solik"},
    {"name": "Evgen", "age": 23, "city": "Solik"},
    {"name": "Ronaldo", "age": 46, "city": "Monaco"}
]


def find_oldest_user(users):
    oldest = users[0]

    for user in users:
        if(oldest["age"] < user["age"]):
            oldest = user
    print(oldest["name"] ," - "  ,oldest["age"])

find_oldest_user(users)