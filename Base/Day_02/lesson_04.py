money = int(input("Сколько денег на счету ? "))
price = int(input("Сколько стоит товар ? "))
discont = (input("Есть ли у тебя скидочная карта? (да/нет) ")).lower()


if(money >= price):
    print("Покупка совершена!")
    print("Осталось денег: ", money - price)
elif(money < price and discont == "да"):
    print("У тебя есть скидка, но денег всё равно недостаточно")
elif(money < price and discont =="нет"):
    print("Недостаточно денег")