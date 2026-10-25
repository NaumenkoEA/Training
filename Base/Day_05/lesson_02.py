numbers_name =int(input("Введите количество имен : "))
names = []
for i in range(numbers_name):
    name = input("Введите имя : ")
    names.append(name)

find_name = input("Какое имя вы хотите найти ? ") 


if (find_name in names):
    print("Имя найдено!")
else:
    print("Такого имени нет.")