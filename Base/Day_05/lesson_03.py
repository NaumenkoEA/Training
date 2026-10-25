count = int(input("Сколько чисел? "))

numbers =[]

for i in range(count):
    num = int(input("Введите число: "))
    numbers.append(num)
print("Все числа: ", numbers)

has_even = False

print("Чётные числа: ")
for i in range(count):
    if (numbers[i] % 2 == 0):
        print (numbers[i])
        has_even = True
if has_even == False:
    print("Чётных чисел нет")
        