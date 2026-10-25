user = {
    "name" : "Alina",
    "age": 22,
    "city" : "solihorsk"
}

print("Текущий профиль : ")
print(user)

change = input("Что ты хочешь изменить? ").lower()

if(change in user):
    user[change] = input("Введите новое значение :")
else:
    print("Такого ключа нет")

print(user)
