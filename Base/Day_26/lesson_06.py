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


def get_names_from_city(users,city):
    return list(map(lambda x : x["name"],filter(lambda x : x["city"] == city , users)))


def get_ages_from_city(users,city):
    return list(map(lambda x : x["age"],filter(lambda x : x["city"] == city , users)))


def get_names_older_than(users,age):
    return list(map(lambda x : x["name"],filter(lambda x : x["age"] > age , users)))


def get_users_from_city_older_than(users, city, age):
    return list(map(lambda x : x["name"],filter(lambda x : x["age"] > age and x["city"] == city, users)))


def get_average_age_from_city(users, city):
    ages = get_ages_from_city(users, city)
    return sum(ages) / len(ages)


def get_max_age_from_city(users, city):
    ages = get_ages_from_city(users, city)
    return max(ages)


def get_min_age_from_city(users, city):
    ages = get_ages_from_city(users, city)
    return min(ages)


def get_age_range_from_city(users, city):
    ages = get_ages_from_city(users, city)
    return max(ages) - min(ages)


def get_age_all_users(users):
    return list(map(lambda x : x["age"],users))


def get_average_age(users):
    ages = get_age_all_users(users)
    return sum(ages) / len(ages)


def get_average_age_v2(users):
    return get_total_age(users) / get_users_count(users)


def get_total_age(users):
    ages =get_age_all_users(users)
    return sum(ages)


def get_users_count(users):
    return len(users)


def get_average_age_from_city(users, city):
    age_city = get_users_from_city(users,city)
    return get_average_age_v2(age_city)


def get_age_stats(users):
    count_users = get_users_count(users)
    total_age = get_total_age(users)
    average_age = get_average_age_v2(users)
    return count_users , total_age , average_age


def get_city_stats(users, city):
    users_city = get_users_from_city(users,city)
    count_users = get_users_count(users_city)
    min_age = get_min_age_from_city(users,city)
    max_age = get_max_age_from_city(users,city)
    return count_users , min_age , max_age

def get_city_stats_dict(users, city):
    users_city = get_users_from_city(users,city)
    count_users = get_users_count(users_city)
    min_age = get_min_age_from_city(users,city)
    max_age = get_max_age_from_city(users,city)
    average_age = get_average_age_v2(users_city)
    stats ={
        "count" : count_users,
        "min_age" : min_age,
        "max_age" : max_age,
        "average_age" : average_age
    }
    return stats


def get_all_cities(users):
    cities = list(map(lambda x : x["city"],users))
    return list(set(cities))


def get_user_count_by_city(users):
    counts ={}
    for user in users:
        city = user["city"]
        if city in counts :
            counts[city] = counts[city] + 1
        else:
            counts[city] = 1
    return counts


counts = {
    "solik": 2,
    "brest": 1,
    "minsk": 1,
    "monaco": 1
}

def get_city_with_most_users(users):
    counts = get_user_count_by_city(users)
    max_count = 0
    best_city = None


    for city , count in counts.items() :
        if count > max_count:
            max_count = count
            best_city = city 
    return max_count , best_city


def get_city_with_least_users(users):
    counts = get_user_count_by_city(users)
    min_count = None
    best_city = None
    
    for city , count in counts.items() :
        if min_count is None or count <= min_count:
            min_count = count
            best_city = city 
    return min_count , best_city

count , city = get_city_with_least_users(users)

print(count)
print(city)

