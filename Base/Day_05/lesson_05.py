count =int(input("Сколько чисел вы хотите ввести ? "))

chetnye = 0
nechetnye = 0

numbers = []

for i in range(count):
    number = int(input("Введите число: "))
    numbers.append(number)

print("Все числа: ")
print(numbers)

print("Четные числа ")
for i in range(len(numbers)):
    if (numbers[i] % 2 == 0):
        print(numbers[i])
        chetnye = chetnye + 1


print("Нечетные числа ")
for i in range(len(numbers)):
    if (numbers[i] % 2 != 0):
        print(numbers[i])
        nechetnye = nechetnye + 1

print("Количество четных чисел : ", chetnye)
print("Количество нечетных чисел : ", nechetnye)
