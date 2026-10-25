users = [
    {"name": "alina", "age": 50, "city": "solik"},
    {"name": "evgen", "age": 23, "city": "solik"},
    {"name": "ronaldo", "age": 46, "city": "monaco"}
]

def get_users_older_than(users, age):
    older = []
    for user in users :
        if(user["age"] > age):
            older.append(user)
    if not older :
            print("No older than",age)

    return older

result = get_users_older_than(users,46)

for user in result:
    print("\tName -",user["name"],"\t Age -",user["age"],"\t City -",user["city"])

