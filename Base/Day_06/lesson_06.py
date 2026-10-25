massive=[1,2,3,4,5,6,7,8,9]

def count_even(numbers):
    even = 0
    for num in numbers :
        if(num % 2 == 0):
            
            even = even + 1
    return even

def count_odd(numbers):
    odd = 0
    for num in numbers :
        if(num % 2 != 0):
            
            odd = odd + 1
    return odd

print("Количество четных ", count_even(massive))
print("Количество нечетных " ,count_odd(massive))