# numbers = [1, 2, 3, 4, 5]

# result = {number : number *10 for number in numbers}

# print(result)


users = [
    {"name": "alina", "age": 20, "city": "solik"},
    {"name": "evgen", "age": 23, "city": "solik"},
    {"name": "bob", "age": 5, "city": "brest"},
    {"name": "vova", "age": 15, "city": "minsk"},
    {"name": "ronaldo", "age": 46, "city": "monaco"}
]

# result = {user["name"] : user["age"]  for user in users if user["age"] > 20}

# result = {user["city"] for user in users if user["age"] > 20}


def get_age_groups(users):
    result = {user["name"] :"adults" if user["age"] >=18 else "child" for user in users }
    
    return result

def get_adult_names(users):
    result = [user["name"] for user in users if user["age"] >= 18]
    return result

def get_adult_count(users):
    result = [user for user in users if user["age"] >= 18]
    return len(result)

res = get_adult_count(users)

print(res)