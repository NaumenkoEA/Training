

numbers = [3, 8, 12, 5, 17, 20, 7]


result = list(map(lambda x : x * 2,filter(lambda x: x % 2 == 0,numbers)))
print(result)