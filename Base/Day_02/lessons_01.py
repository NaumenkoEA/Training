money = int(input("Сколько денег на счету ? "))
want_take_money = int(input("Сколько хочешь снять ? "))


if want_take_money <= 0 :

        print("Некорректная сумма ")
elif money < want_take_money  :
    
    print("Недостаточно средств ")
else :
    print("Операция выполнена")
    print("Осталось: ", money - want_take_money)