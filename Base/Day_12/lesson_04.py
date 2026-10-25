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


for user in users:
    if(user["city"] == "Solik"):
        print(user["name"] + " - " + user["city"])
        