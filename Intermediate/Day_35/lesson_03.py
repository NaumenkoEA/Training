numbers = [10, 20, 30, 40, 50]


def find_number(numbers , target):
    for number in numbers :
        if ( target == number):
            return number
    return None


result = find_number(numbers,30)

if result is None:
    print("Number is not find")
else:
    print(result)