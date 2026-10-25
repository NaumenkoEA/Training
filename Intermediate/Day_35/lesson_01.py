
try:
    age = int(input("Enter age "))

    if age < 18:
        raise ValueError("Отказано в доступе")

    print("Достпу разрешен")

except ValueError as error:
    print(error)

except :
    print("Не корректный возраст ")
    
finally: 
    print("Программа закончилась")
