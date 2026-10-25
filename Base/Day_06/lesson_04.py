numbers = [1,5,24,66,2,17,99]

def check_numbers(numberss):
    for number in numberss:
        if (number % 2 == 0 ):
            print(number ," Четное")
        else:
            print(number," Нечетное")

check_numbers(numbers)