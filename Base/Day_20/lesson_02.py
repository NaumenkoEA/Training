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

def get_youngest_user(users):
    youngest = users[0]
    for user in users :
        if(youngest["age"] > user["age"]):
            youngest = user
    return youngest


def get_users_from_city(users,city):
    result = []
    for user in users :
        if(user["city"] == city):
                result.append(user)
    if not result :
                print("There are no users from this city." )

    return result


def get_users_older_than(users, age):
    older = []
    for user in users :
        if(user["age"] > age):
            older.append(user)
    if not older :
            print("No older than",age)

    return older

def show_user(user):
      print("\tName -",user["name"],"\t Age -",user["age"],"\t City -",user["city"])

def show_users(users):
     for user in users:
        print("\tName -",user["name"],"\t Age -",user["age"],"\t City -",user["city"])


def show_oldest_user(users):
    show_user(get_oldest_user(users))


def show_youngest_user(users):
     show_user(get_youngest_user(users))
     

def show_users_older_than(users,age):
     show_users(get_users_older_than(users,age))

def show_users_from_city(users,city):
     show_users(get_users_from_city(users,city))


# print("Search older than")
# show_users_older_than(users,23)

print("Search youngest ")
show_youngest_user(users)

# print("Search to the city\n")
# result_city = get_users_from_city(users,"solik")
# show_users(result_city)

# print("Search oldest user\n")
# result_oldest = get_oldest_user(users)
# show_oldest_user(result_oldest)


# print("Search to the city\n")
# show_users_from_city(users,"solik")

# print("Search oldest user\n")
# show_oldest_user(users)

