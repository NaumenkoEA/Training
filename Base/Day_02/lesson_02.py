login = input("Введите логин: ").lower()
password = input("Введите пароль: ")

if (login == "admin" and password == "12345"):
    print("Добро пожаловать!")
else:
    print("Неверный логин или пароль")