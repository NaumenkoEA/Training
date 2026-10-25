users = [
    {"name": "alina", "age": 20, "city": "solik"},
    {"name": "evgen", "age": 23, "city": "solik"},
    {"name": "bob", "age": 5, "city": "brest"},
    {"name": "vova", "age": 15, "city": "minsk"},
    {"name": "ronaldo", "age": 46, "city": "monaco"}
]


def find_user_by_age(users,mode):
    if(mode == "oldest"):
        oldest = users[0]
        for user in users:
            if(oldest["age"] < user["age"]):
                oldest = user
        return oldest
            
    elif(mode == "youngest"):
        youngest = users[0]
        for user in users :
            if(youngest["age"] > user["age"]):
                youngest = user
        return youngest
    else:
        print("Enter correct mode")


def find_users_by_age(users,age,mode):
    if(mode == "older"):
        older = []
        for user in users :
            if(user["age"] > age):
                older.append(user)
        if not older :
            print("No older than",age)
        return older
    elif(mode == "younger"):
        youngest = []
        for user in users :
            if(user["age"] < age):
                youngest.append(user)
        if not youngest :
                print("No younger than",age)
        return youngest
    else:
            print("Enter correct mode")


def get_oldest_user(users):
    return find_user_by_age(users,"oldest")
    

def get_youngest_user(users):
    return find_user_by_age(users,"youngest")
    

def get_users_from_city(users,city):
    result = []
    for user in users :
        if(user["city"] == city):
                result.append(user)
    if not result :
                print("There are no users from this city." )

    return result


def get_users_older_than(users, age):
    return find_users_by_age(users,age,"older")


def get_users_younger_than(users, age):
    return find_users_by_age(users,age,"younger")
    
def show_user(user):
      print("\tName -",user["name"],"\t Age -",user["age"],"\t City -",user["city"])

def show_users(users):
     for user in users:
        show_user(user)


def show_oldest_user(users):
    show_user(get_oldest_user(users))


def show_youngest_user(users):
     show_user(get_youngest_user(users))
     

def show_users_older_than(users,age):
     show_users(get_users_older_than(users,age))

def show_users_from_city(users,city):
     show_users(get_users_from_city(users,city))



def get_youngest_from_list(users):
    youngest = users[0]
    for user in users :
        if(youngest["age"] > user["age"]):
            youngest = user
    return youngest


def get_oldest_from_list(users):
    oldest = users[0]
    for user in users :
        if(oldest["age"] < user["age"]):
            oldest = user
    return oldest


def sort_users_by_age(users):
    
    sort_list=[]
    while users:
        first_man = get_youngest_from_list(users)
        sort_list.append(first_man)
        users.remove(first_man)
    return sort_list


def sort_users_by_age_desc(users):
    sort_list=[]
    while users:
        first_man = get_oldest_from_list(users)
        sort_list.append(first_man)
        users.remove(first_man)
    return sort_list

# result = sort_users_by_age_desc(users)
# show_users(result)
# result = sorted(users, key=lambda x: x["age"] , reverse=True)
# result= list(filter( lambda x : x["city"] != "solik", users ))

result = list(map( lambda x : x["name"], users))
print(result)