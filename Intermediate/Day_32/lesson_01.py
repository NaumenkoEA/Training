numbers = [12, 5, 8, 21, 44, 17, 30, 3, 26, 11]

count_more = 0
sum_more = 0

count_less = 0
sum_less = 0

for number in numbers:
    if(number > 20 ):
        
        count_more += 1
        sum_more  += number
    else:
        
        count_less += 1
        sum_less += number
   
print("Even numbers count -",count_more ," sum -", sum_more,"avg -",sum_more / count_more)
print("Odd numbers count -",count_less ," sum -", sum_less,"avg -",sum_less / count_less)
