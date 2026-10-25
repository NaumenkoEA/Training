money = int(input("Сколько денег на счету ? "))
want_take_money = int(input("Сколько хочешь снять ? "))


if (want_take_money > money):
    print("Недостаточно средств")
elif (want_take_money <= money):
    print("Операция выполнена")
    print("Осталось:", money - want_take_money)
