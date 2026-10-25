number =int(input("Введите число: "))

for number in range (number,0,-1):
    if(number % 2 == 0):
        print(number, "- четное")
    else:
        print(number, "- нечетное")