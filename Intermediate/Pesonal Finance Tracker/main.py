import json
process = True

try:
    with open("finance_data.json","r" ,encoding="utf-8") as file:
        data = json.load(file)
    balance = data["balance"]
    transactions =data["transactions"]
except FileNotFoundError:
    balance = 0 
    transactions = []


def show_balance(value):
    print(f"Текущий баланс: {value}")

def show_transactions(value):
    if value :
        print("История операций")
        for val in value :
            print(f"Тип: {val['type']} - Сумма: {val['amount']}")
    else:
        print("История оперций пуста! ")

def deposit_money(value,transactions):
    try:
        deposit = int(input("Введите сумму пополнения : "))
    except ValueError:
        print("Ошибка: нужно ввести число!")
        return value

    if(deposit > 0):
        value += deposit
        transactions.append({"type":"Пополнение", "amount":deposit})

        return value
    else:
        print("Ошибка, некорректная сумма! ")
        return value

def withdraw_money(value,transactions):
    try:
        withdraw = int(input("Введите сумму которую хотите снять : "))
    except ValueError:
        print("Ошибка: нужно ввести число!")
        return value

    if(withdraw <= 0 ):
        print("Ошибка, некорректная сумма! ")
        return value
    elif(withdraw > value):
        print("Недостаточно средств! ")
        return value
    else:
        value -= withdraw
        transactions.append({"type":"Снятие", "amount":withdraw})
        return value

while(process):
    print("\nФинансовый трекер")
    print("1.Посмотреть баланс \n2.Пополнить счет \n3.Снять деньги \n4.История операций \n0.Выход\n")
    try:
        menu_choice = int(input("Выберите действие : "))
    except ValueError:
        print("Ошибка: нужно ввести число!")
        continue

    if menu_choice not in [0, 1, 2, 3, 4]:
        print("Не правильно выбранно действие! ")

    elif(menu_choice == 1):
        show_balance(balance)

    elif(menu_choice == 2):
        balance = deposit_money(balance,transactions)

    elif(menu_choice == 3):
        balance = withdraw_money(balance,transactions)

    elif(menu_choice == 4):
        show_transactions(transactions)

    elif(menu_choice == 0):
        process = False


data ={
    "balance" : balance,
    "transactions": transactions
}

with open("finance_data.json","w" ,encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False, indent=4)