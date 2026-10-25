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

yong = users[0]
for user in users:
    if(yong["age"] > user["age"]):
        yong = user
print(yong["name"] ," - "  ,yong["age"])
        