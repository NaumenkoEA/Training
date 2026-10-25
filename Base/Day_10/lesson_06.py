password = input("Введите пароль: ")

numbers=["0","1","2","3","4","5","6","7","8","9"]
has_number = False


if (len(password) < 8):
    print("Пароль слишком короткий")
else :
    for number in numbers:
        if number in password:
            has_number = True
    if has_number == False:
        print("Добавь хотя бы одну цифру")
    else:
        print("Пароль подходит")

