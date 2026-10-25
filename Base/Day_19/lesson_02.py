users = [
    {"name": "alina", "age": 20, "city": "solik"},
    {"name": "evgen", "age": 23, "city": "solik"},
    {"name": "ronaldo", "age": 46, "city": "monaco"}
]

def get_oldest_user(users):
    oldest = users[0]
    for user in users:
        if(oldest["age"] < user["age"]):
            oldest = user
    return oldest

result = get_oldest_user(users)

print(result["name"])
print(result["age"])
print(result["city"])