user = {
    "name": "Alina",
    "age": 22,
    "city": "Solihorsk",
    "salary": 1500,
    "experience": 2
}
string = 0
integer = 0
for key in user:
    
    
    if type(user[key]) == str :
        
        string = string + 1
        print("Текст :", key , "=" , user[key])
    elif type(user[key]) == int :
        
        integer = integer + 1
        print("Число :", key , "=" , user[key])

print("Количество текстовых значений:", string)
print("Количество числовых значений:", integer)