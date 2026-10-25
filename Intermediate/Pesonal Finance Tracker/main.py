
balance = 0
process = True

def show_balance(value):
    print(f"Текущий баланс: {value}")

def deposit_money(value):
    deposit = int(input("Введите сумму пополнения : "))
    if(deposit > 0):
        value += deposit
        return value
    else:
        print("Ошибка, некорректная сумма! ")
        return value

def withdraw_money(value):
    withdraw = int(input("Введите сумму которую хотите снять : "))
    if(withdraw <= 0 ):
        print("Ошибка, некорректная сумма! ")
        return value
    elif(withdraw > value):
        print("Недостаточно средств! ")
        return value
    else:
        value -= withdraw
        return value

while(process):
    print("\nФинансовый трекер")
    print("1.Посмотреть баланс \n2.Пополнить счет \n3.Снять деньги \n0.Выход\n")
    
    menu_choice = int(input("Выберите действие : "))
    if menu_choice not in [0, 1, 2, 3]:
        print("Не правильно выбранно действие! ")

    elif(menu_choice == 1):
        show_balance(balance)

    elif(menu_choice == 2):
        balance = deposit_money(balance)

    elif(menu_choice == 3):
        balance = withdraw_money(balance)

    elif(menu_choice == 0):
        process = False


