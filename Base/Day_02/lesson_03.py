login = input("Введите логин: ").lower()
password = input("Введите пароль: ")

if (login == "admin" and password == "12345"):
    print("Добро пожаловать, администратор!")
elif (login == "manager" and password == "55555"):
    print("Добро пожаловать, менеджер!")
elif (login == "user" and password == "11111"):
    print("Добро пожаловать, пользователь!")
else:
    print("Неверный логин или пароль")