import json
from datetime import date


process = True
categories = ["еда", "транспорт", "развлечения", "покупки", "другое"]


def load_data():
    try:
        with open("finance_data.json","r" ,encoding="utf-8") as file:
            data = json.load(file)
        balance = data["balance"]
        transactions = data["transactions"]
    except FileNotFoundError:
        balance = 0 
        transactions = []
    return balance , transactions
    
balance, transactions = load_data()

def save_data(balance , transactions):
    data ={
    "balance" : balance,
    "transactions": transactions
    }
    with open("finance_data.json","w" ,encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False, indent=4)

def show_balance(value):
    print(f"Текущий баланс: {value}")

def show_transactions(value):
    if value :
        print("История операций")
        for val in value :
            print(f"Тип: {val['type']} - Сумма: {val['amount']} - Категория :{val.get('category','Не указана')}")
    else:
        print("История оперций пуста! ")

def show_expense_statistics(transactions):
    total = 0
    for transaction in transactions:
        if(transaction["type"] == "Снятие"):
            total +=transaction["amount"]
    return total

def show_expense_by_category(transactions):
    expense={}
    for transaction in transactions:
        if(transaction["type"] == "Снятие"):
            category = transaction.get("category","не указана")
            amount = transaction["amount"]
            if(category in expense):
                expense[category] += amount
            else:
                expense[category] = amount
    return expense

def show_expenses_by_month(transactions):
    input_date = input("Введите месяц в формате ГГГГ-ММ :")
    total = 0
    if(len(input_date) == 7 and input_date[4] == "-" ):
        str1 , str2 = input_date.split("-")
        if((str1.isdigit() and int(str1) >= 2000) and (str2.isdigit() and int(str2) <=12 and int(str2) >= 1)):
            for transaction in transactions:
                if(transaction["type"] =="Снятие" and transaction["date"].startswith(input_date)):
                    total += transaction["amount"]
            return total ,input_date
        else:
            return total , None
    else:
        return total , None

def show_expenses_by_category_and_month(transactions):
    input_date = input("Введите месяц в формате ГГГГ-ММ :")
    expense={}
    if(len(input_date) == 7 and input_date[4] == "-" ):
        str1 , str2 = input_date.split("-")
        if((str1.isdigit() and int(str1) >= 2000) and (str2.isdigit() and int(str2) <=12 and int(str2) >= 1)):
            for transaction in transactions:
                if(transaction["type"] =="Снятие" and transaction["date"].startswith(input_date)):
                    category = transaction.get("category","не указана")
                    amount = transaction["amount"]
                    if(category in expense):
                        expense[category] += amount
                    else:
                        expense[category] = amount
            return expense
        else:
            return None
    else:
        return None
    

def deposit_money(value,transactions):
    try:
        deposit = int(input("Введите сумму пополнения : "))
    except ValueError:
        print("Ошибка: нужно ввести число!")
        return value ,False

    if(deposit > 0):
        today = date.today().isoformat()
        value += deposit
        transactions.append({"type":"Пополнение", "amount":deposit , "date":today})
        return value , True
    else:
        print("Ошибка, некорректная сумма! ")
        return value ,False

def withdraw_money(value,transactions):
    try:
        withdraw = int(input("Введите сумму которую хотите снять : "))
        category = input("Выберите категорию (Еда, Транспорт, Развлечения, Покупки, Другое) : ").strip().lower()
    except ValueError:
        print("Ошибка: нужно ввести число!")
        return value ,False

    if(withdraw <= 0):
        print("Ошибка, некорректная сумма! ")
        return value, False
    elif(withdraw > value):
        print("Недостаточно средств! ")
        return value, False
    elif(category not in categories):
        print("Не правильная категория! ")
        return value,False
    else:
        today = date.today().isoformat()
        value -= withdraw
        transactions.append({"type":"Снятие", "amount":withdraw , "category":category , "date":today})
        return value, True

while(process):
    print("\nФинансовый трекер")
    print("""    1.Посмотреть баланс
    2.Пополнить счет
    3.Снять деньги
    4.История операций
    5.Расходы
    6.Расходы по категориям
    7.Расходы за месяц
    8.Расходы по категориям за месяц
    0.Выход\n""")
    try:
        menu_choice = int(input("Выберите действие : "))
    except ValueError:
        print("Ошибка: нужно ввести число!")
        continue

    if menu_choice not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        print("Не правильно выбранно действие! ")

    elif(menu_choice == 1):
        show_balance(balance)

    elif(menu_choice == 2):
        balance , success = deposit_money(balance,transactions)
        if success:
            save_data(balance,transactions)

    elif(menu_choice == 3):
        balance, success = withdraw_money(balance,transactions)
        if success:
            save_data(balance,transactions)

    elif(menu_choice == 4):
        show_transactions(transactions)

    elif(menu_choice == 5):
        result = show_expense_statistics(transactions)
        if result:
            print("Общая сумма расходов: ",result)
        else:
            print("Расходов нет")

    elif(menu_choice == 6):
        result = show_expense_by_category(transactions)
        if result:
            print("Cумма расходов по категориям:")
            for category , amount in result.items():
                print(f"{category} : {amount} ")
        else:
            print("Расходов на эту категорию нет")

    elif(menu_choice == 7):
        result , month = show_expenses_by_month(transactions)
        if(month is not None):
            print(f"Cумма расходов за {month}: {result}")
        else:
            print("Неправильная дата")

    elif(menu_choice == 8):
        result = show_expenses_by_category_and_month(transactions)
        if result is None :
            print("Неправильная дата") 
        elif result:
            print("Cумма расходов по категориям за месяц:")
            for category , amount in result.items():
                print(f"{category} : {amount} ")
        else:
            print("За этот месяц расходов нет")

    elif(menu_choice == 0):
        process = False
