names =[]
number = int(input("Сколько имён будешь вводить ? "))

for i in range(number,0,-1):
    name = input("Введите имя : ")
    names.append(name)

for name in names :
    print(name)