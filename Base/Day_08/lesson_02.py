user = {
    "name": "Alina",
    "age": 22,
    "city": "Solihorsk",
    "job": "teacher"
}

for key in user :
    if type(user[key]) == str :
        print(key , " : " , user[key])