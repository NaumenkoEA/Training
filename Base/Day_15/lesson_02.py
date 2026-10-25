users = [
    {"name": "alina", "age": 20, "city": "solik"},
    {"name": "evgen", "age": 23, "city": "solik"},
    {"name": "ronaldo", "age": 46, "city": "monaco"}
]

def show_users(users):
    print("\nAll users\n")
    for user in users :
        print("\tName -",user["name"].capitalize(),"\t Age -",user["age"],"\t City -",user["city"].capitalize())

def find_users_from_city(users,city):
    print("\nUsers from this city - ",city, "\n")
    result = []
    has_users = False
    for user in users:
        if(user["city"] == city):
            result.append(user)
            has_users = True
    if(has_users == False):
            print("There are no users from this city." )
    for user in result :
        print("\tName -",user["name"],"\t Age -",user["age"],"\t City -",user["city"])
    

def find_users_older_than(users,age):
    print("\nOlder than ",age, "\n")
    result = []
    has_users = False
    for user in users:
        if(user["age"] > age):
            result.append(user)
            has_users = True
    if(has_users == False):
        print("No older than",age)
    for user in result :
           print("\tName -",user["name"],"\t Age -",user["age"],"\t City -",user["city"])
    

def find_oldest_user(users):
    print("\nOlder Man\n")
    oldest = users[0]
    for user in users:
        if(oldest["age"] < user["age"]):
            oldest = user
    print("\tName -",oldest["name"],"\t Age -",oldest["age"],"\t City -",oldest["city"])


def add_user(users,name,age,city):
    user = {
        "name" : name,
        "age" : age,
        "city" : city
    }
    users.append(user)
    
def delete_user(users,name):
    has_user = True
    for user in users:
        if(user["name"] == name):
            users.remove(user)
            has_user = False
            break
    if has_user:
         print("User not found")

def change_user(users,name,age,city):
    has_user = True
    for user in users:
            if(user["name"] == name):
                user["name"] = name
                user["age"] = age
                user["city"] = city
                has_user = False
                break
    if has_user:
             print("User not found")



has_work = True

while(has_work):
    print("\nMenu:\n" \
    "1.Show all users\n" \
    "2.Find users from city\n" \
    "3.Find users older than age\n" \
    "4.Find oldest user\n" \
    "5.Add user\n" \
    "6.Delete user\n" \
    "7.Change user\n" \
    "0.Exit\n")

    choice = input("Select an action : ")
    if(choice == "1"):
        show_users(users)
    elif (choice == "2"):
        choice_city = input("Enter the city (Solik/Monaco/Minsk) ").lower()
        find_users_from_city(users,choice_city)
    elif(choice == "3"):
        entered_age = int(input("Enter age "))
        find_users_older_than(users,entered_age)
    elif(choice == "4"):
        find_oldest_user(users)
    elif(choice == "5"):
        name = input("Enter name: ").lower()
        age = int(input("Enter age: "))
        city = input("Enter city: ")
        add_user(users,name,age,city)
    elif(choice == "6"):
            name = input("Enter name to delete: ").lower()
            delete_user(users,name)
    elif(choice == "7"):
            name = input("Enter name: ").lower()
            age = int(input("Enter age: "))
            city = input("Enter city: ")
            change_user(users,name,age,city)
    elif(choice == "0"):
        has_work =False
    else:
        print("Input error")
        has_work = False