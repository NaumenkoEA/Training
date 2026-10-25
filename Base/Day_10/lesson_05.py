password = input("Введите пароль: ")

if (len(password) >= 8):
    print("Пароль достаточно длинный")
else:
    print("Пароль слишком короткий")