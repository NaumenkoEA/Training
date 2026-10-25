correct_password ="123"
password = input("Введите пароль ")

stop = 1

while (stop):
    if(password != correct_password):
        print("Неверный пароль! ")
        password = input("Введите пароль еще раз ")
    elif(password == correct_password):
        print("Доступ разрешен!")
        stop = False

