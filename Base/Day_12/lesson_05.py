users = [
    {
        "name": "Alina",
        "age": 20,
        "city" : "Solik"
    },
    {
        "name": "Evgen",
        "age": 23,
        "city" : "Solik"
    },
    {
        "name": "Ronaldo",
        "age": 46,
        "city" : "Monaco"
    }
]

oldest = users[0]
for user in users:
    if(oldest["age"] < user["age"]):
        oldest = user
print(oldest["name"] ," - "  ,oldest["age"])
        