count =int(input("Сколько чисел вы хотите ввести ? "))

numbers = []

for i in range(count):
    number = int(input("Введите число: "))
    numbers.append(number)
print(numbers)

print("Четные числа ")
for i in range(len(numbers)):
    if (numbers[i] % 2 == 0):
        print(numbers[i])

print("Нечетные числа ")
for i in range(len(numbers)):
    if (numbers[i] % 2 != 0):
        print(numbers[i])