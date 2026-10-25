correct_password ="123"
password = input("Введите пароль ")
tried = 3

while (tried > 0):
    if(password != correct_password):
        print("Неверный пароль! ")
        
        tried = tried -1
        
        print("Осталось попыток: ", tried)
        
        if tried > 0:
            print("Доступ заблокирован!")
            password = input("Введите пароль еще раз ")

    elif(password == correct_password):
        print("Доступ разрешен!")
        tried = 0

