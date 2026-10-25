users = [
    {"name": "alina", "age": 50, "city": "solik"},
    {"name": "evgen", "age": 23, "city": "solik"},
    {"name": "ronaldo", "age": 46, "city": "monaco"}
]

def get_youngest_user(users):
    youngest = users[0]
    for user in users :
        if(youngest["age"] > user["age"]):
            youngest = user
    return youngest

result = get_youngest_user(users)

print(result["name"])
print(result["age"])
print(result["city"])