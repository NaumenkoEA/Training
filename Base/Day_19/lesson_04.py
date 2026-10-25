users = [
    {"name": "alina", "age": 50, "city": "solik"},
    {"name": "evgen", "age": 23, "city": "solik"},
    {"name": "ronaldo", "age": 46, "city": "monaco"}
]

def get_users_from_city(users,city):
    result = []
    for user in users :
        if(user["city"] == city):
                result.append(user)
    if not result :
                print("There are no users from this city." )

    return result

result = get_users_from_city(users,"solik")

for user in result:
    print("\tName -",user["name"],"\t Age -",user["age"],"\t City -",user["city"])