

class AgeError(Exception):
    pass

try:
    age = int(input("Enter age "))

    if age < 18 :
        raise AgeError("Младше 18 , отказ")

    print("Доступ разрешен")

except AgeError as error:
    print(error)

except ValueError:
    print("Не корректный текст")

finally:
    print("END")