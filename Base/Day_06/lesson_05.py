massive=[1,2,3,4,5,6,7,8,9]

def count_even(numbers):
    even = 0
    for num in numbers :
        if(num % 2 == 0):
            
            even = even + 1
    return even

print(count_even(massive))