user = {
    "name": "Evgen",
    "age": 23,
    "city": "solik"
}

for key , value in user.items():
    if( type(value) != str):
        print(key)