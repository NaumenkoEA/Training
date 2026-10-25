user = {
    "name" : "Alina",
    "age": 22,
    "city" : "solihorsk"
}

change = input("Что ты хочешь изменить (name/age/city) ? ").lower()


if (change in user):
    user[change] = input("Введите новое значение :")
else:
    print("Такого ключа нет")

print(user)