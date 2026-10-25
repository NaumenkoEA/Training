user = {
    "name": "Alina",
    "age": 22,
    "city": "Solihorsk",
    "salary": 1500,
    "experience": 2
}

for key in user:
    if type(user[key]) == str :
        print("Текст :", key , "=" , user[key])
    elif type(user[key]) == int :
        print("Число :", key , "=" , user[key])