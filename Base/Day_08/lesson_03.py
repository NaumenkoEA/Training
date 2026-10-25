user = {
    "name": "Alina",
    "age": 22,
    "city": "Solihorsk",
    "salary": 1500,
    "experience": 2
}

for key in user :
    if type(user[key]) == int :
        print(key , ":" , user[key])