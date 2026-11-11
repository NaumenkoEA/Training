from database import (
    init_db,
    get_total_income,
    add_transaction,
    get_transactions,
    get_expenses,
    update_transaction,
    delete_transaction,
    get_transactions_sorted,
    get_last_transactions,
    get_total_expenses,
    get_expenses_by_category,
    get_expenses_by_month,
    get_expenses_by_category_and_month,
    get_income_by_month,
    count_expenses_by_category,
    get_average_expense
)
from datetime import date
from datetime import datetime

init_db()

process = True
categories = ["еда", "транспорт", "развлечения", "покупки", "другое"]



def show_balance():
    balance =  get_total_income() - get_total_expenses()
    print(f"Текущий баланс: {balance}")

def show_transactions():
    transactions = get_transactions()
    if transactions :
        print(f"{'№':<4} {'Тип':<15} {'Сумма':<12} {'Категория':<18} {'Дата':<12}")
        print("-" * 65)

        for index, val in enumerate(transactions, start=1):
            category = val[3] or "Без категории"
            print(f"{index:<4} {val[1]:<15} {val[2]:<12.2f} {category:<18} {val[4]:<12}")
    else:
        print("Транзакций нет")

def show_expense_statistics():
    return get_total_expenses()

def show_expense_by_category():
    return get_expenses_by_category()

def show_expenses_by_month():
    input_date = input("Введите месяц в формате ГГГГ-ММ :")
    total = 0
    
    if(len(input_date) == 7 and input_date[4] == "-" ):
        str1 , str2 = input_date.split("-")
        if((str1.isdigit() and int(str1) >= 2000) and (str2.isdigit() and int(str2) <=12 and int(str2) >= 1)):
            total = get_expenses_by_month(input_date)
            return total, input_date
        else:
            return total , None
    else:
        return total , None

def show_expenses_by_category_and_month():
    input_date = input("Введите месяц в формате ГГГГ-ММ: ")

    if len(input_date) == 7 and input_date[4] == "-":
        str1, str2 = input_date.split("-")

        if (
            str1.isdigit()
            and int(str1) >= 2000
            and str2.isdigit()
            and 1 <= int(str2) <= 12
        ):
            expenses = get_expenses_by_category_and_month(input_date)
            return expenses
        
    return  None

def remove_transaction():
    transactions = get_transactions()
    if transactions :
        for transaction in transactions:
            print(f"{transaction[0]}.{transaction[1]} \t {transaction[2]}")
        try:
            transaction_id = int(input("\nВведите ID транзакции: "))
            selected_transaction = None
            for transaction in transactions:
                if transaction[0] == transaction_id:
                    selected_transaction = transaction
                    break
            if selected_transaction is None:
                print("Транзакция не найдена")
                return False
            else:
                category = selected_transaction[3] or "Без категории"
                check = input("Удалить транзакцию Да/Нет: ").strip().lower()
                if( check == 'нет'):
                    print("Удаление отменено!")
                    return False
                elif(check == 'да'):
                    delete_transaction(transaction_id)
                    print(f"{selected_transaction[0]}. {selected_transaction[1]} \t {selected_transaction[2]} \t {category} \t {selected_transaction[4]}")
                    return True
                else:
                    print("Некорректное подтверждение!")
                    return False
        except ValueError:
            print("Некорректный ввод")
            return False
    else:
        print("Транзакций нет")
        return False

def edit_transaction():
    transactions = get_transactions()
    if transactions :
        for transaction in transactions:
            print(f"{transaction[0]}.{transaction[1]} \t {transaction[2]}")
        try:
            transaction_id = int(input("\nВведите ID транзакции: "))
            selected_transaction = None
            for transaction in transactions:
                if(transaction[0] == transaction_id):
                    selected_transaction = transaction
                    break
            if selected_transaction is None:
                print("Транзакция не найдена")
                return False
            else:
                category = selected_transaction[3] or "Без категории"
                print(f"{selected_transaction[0]}. {selected_transaction[1]} \t {selected_transaction[2]} \t {category} \t {selected_transaction[4]}")
                old_amount = selected_transaction[2]
                new_amount = int(input("Введите новую сумму "))
                if new_amount <= 0 :
                    print("Неверная сумма!")
                    return False
                else:
                    balance_ = get_total_income() - get_total_expenses()
                    transaction_type = selected_transaction[1]
                    if transaction_type == 'снятие':
                        new_balance = balance_ + old_amount - new_amount
                        if new_balance < 0 :
                            print("Недостаточно средств для изменения операции!")
                            return False
                        else:
                            update_transaction(selected_transaction[0], new_amount)
                            print(f"Сумма изменена: {old_amount} → {new_amount}")
                            return True
                    elif transaction_type == 'пополнение':
                        update_transaction(selected_transaction[0], new_amount)
                        print(f"Сумма изменена: {old_amount} → {new_amount}")
                        return True
                    else:
                        print("Неизвестный тип операции")
                        return False
        except ValueError:
            print("\nНекорректный ввод ")
            return False
    else:
        print("\nТранзакций нет")
        return False

def filter_transactions_by_type():
    transactions = get_transactions()
    if not transactions:
        print("Операций нет")
        return None
    else:
        filtr = input("Выберите тип операции (Пополнение/Снятие) : ").lower()
        if filtr not in ["пополнение","снятие"]:
            print("Некорректный тип операции!")
        else:
            filtered_transactions =[]
            for transaction in transactions :
                if transaction[1].lower() == filtr:
                    filtered_transactions.append(transaction)

            if not filtered_transactions:
                print("Операций данного типа нет")
            else:
                for item in filtered_transactions:
                    print(f"\n{item[1]} - {item[2]} - {item[4]}")

def filter_transactions_by_category():
    transactions = get_transactions()
    if not transactions:
        print("Операций нет")
        return None
    categories=[]
    filtered_transactions = []
    for transaction in transactions:
        if(transaction[1].lower() == "снятие"):
            categories.append((transaction[3] or " ").lower())
    unique_categories = set(categories)
    if not unique_categories:
        print("Нет категорий расходов")
        return None
    else:
        for item in unique_categories:
            print(item.capitalize())
        need_category = input("Выберите категорию: ").strip().lower()
            
        for transaction in transactions:
            if (transaction[1].lower() == "снятие" and (transaction[3] or "").lower() == need_category):
                filtered_transactions.append(transaction)
        if not filtered_transactions:
            print("Операций в этой категории нет")
            return None
        print(f"\n Категория : {need_category.capitalize()}")
        for item in filtered_transactions:    
            print(f"\n{item[1]} - {item[2]} - {item[4]}")

def filter_transactions_by_month():
    transactions =get_transactions()
    if not transactions:
            print("Операций нет")
            return None
    input_date = input("Введите месяц в формате ГГГГ-ММ :")
    filtered_transactions = []
    if(len(input_date) == 7 and input_date[4] == "-" ):
            str1 , str2 = input_date.split("-")
            if((str1.isdigit() and 2000 <= int(str1) <= date.today().year) and (str2.isdigit() and 1 <= int(str2) <= 12)):
                for transaction in transactions:
                    if(transaction[4].startswith(input_date)):
                        filtered_transactions.append(transaction)
            else:
                print("Некорректный формат даты")
                return  None
    else:
        print("Некорректный формат даты")
        return None
    if not filtered_transactions:
                print("Операций в выбраном месяце нет")
                return None
    print(f"\n Месяц : {input_date}")
    for item in filtered_transactions:    
        print(f"\n{item[1]} - {item[2]} - {item[4]}")
    
def show_income_by_month():
    input_date = input("Введите месяц в формате ГГГГ-ММ :")
    total = 0
        
    if(len(input_date) == 7 and input_date[4] == "-" ):
        str1 , str2 = input_date.split("-")
        if((str1.isdigit() and 2000 <= int(str1) <= date.today().year) and (str2.isdigit() and 1 <= int(str2) <= 12)):
            total = get_income_by_month(input_date)
            return total ,input_date
        else:
            return total , None
    else:
        return total , None

def deposit_money():
    try:
        deposit = int(input("Введите сумму пополнения : "))
    except ValueError:
        print("Ошибка: нужно ввести число!")
        return False

    if(deposit > 0):
        today = date.today().isoformat()
        add_transaction('пополнение', deposit, None, today)
        return  True
    else:
        print("Ошибка, некорректная сумма! ")
        return False

def withdraw_money():
    balance_ = get_total_income() - get_total_expenses()
    try:
        withdraw = int(input("Введите сумму которую хотите снять : "))
        category = input("Выберите категорию (Еда, Транспорт, Развлечения, Покупки, Другое) : ").strip().lower()
    except ValueError:
        print("Ошибка: нужно ввести число!")
        return False

    if(withdraw <= 0):
        print("Ошибка, некорректная сумма! ")
        return  False
    elif(withdraw > balance_):
        print("Недостаточно средств! ")
        return False
    elif(category not in categories):
        print("Не правильная категория! ")
        return False
    else:
        today = date.today().isoformat()
        add_transaction('снятие', withdraw, category, today)
        return True

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
    9.Пополнения за месяц
    0.Выход\n""")
    try:
        menu_choice = int(input("Выберите действие : "))
        print("")
    except ValueError:
        print("Ошибка: нужно ввести число!")
        continue

    if menu_choice not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("Не правильно выбранно действие! ")

    elif(menu_choice == 1):
        show_balance()

    elif menu_choice == 2:
        success = deposit_money()
        if success:
            print("Пополнение успешно сохранено!")

    elif(menu_choice == 3):
        success = withdraw_money()
        if success:
            print("Снятие успешно сохранено!")

    elif(menu_choice == 4):
        process_choice = True
        show_transactions()
        while(process_choice):
            print("\nВыберите действие :")
            print("""\n    1.Удалить транзакцию
    2.Редактировать транзакцию
    3.Фильтр транзакций по типу
    4.Фильтр транзакций по категории
    5.Фильтр транзакций по месяцу
    0.Выход\n""")
            try:
                menu_transaction_choice = int(input("Выберите действие : "))
            except ValueError:
                print("Ошибка: нужно ввести число!")
                continue
            
            if menu_transaction_choice not in [0, 1, 2, 3, 4, 5]:
                print("Не правильно выбранно действие! ")

            elif(menu_transaction_choice == 1):
                success = remove_transaction()
                if success:
                    print("Транзакция удалена! ")

            elif(menu_transaction_choice == 2):
                success = edit_transaction()
                if success:
                    print("Успешно изменено! ")

            elif(menu_transaction_choice == 3):
                filter_transactions_by_type()

            elif(menu_transaction_choice == 4):
                filter_transactions_by_category()

            elif(menu_transaction_choice == 5):
                filter_transactions_by_month()

            elif(menu_transaction_choice == 0):
                process_choice = False
            
    elif(menu_choice == 5):
        result = show_expense_statistics()
        if result:
            print("Общая сумма расходов: ",result)
        else:
            print("Расходов нет")

    elif(menu_choice == 6):
        result = show_expense_by_category()
        if result:
            print("Cумма расходов по категориям: ")
            for category , amount in result.items():
                print(f"{category} : {amount} ")
        else:
            print("Расходов на эту категорию нет")

    elif(menu_choice == 7):
        result , month = show_expenses_by_month()
        if(month is not None):
            print(f"Cумма расходов за {month}: {result}")
        else:
            print("Неправильная дата")

    elif(menu_choice == 8):
        result = show_expenses_by_category_and_month()
        if result is None :
            print("Неправильная дата") 
        elif result:
            print("Cумма расходов по категориям за месяц: ")
            for category , amount in result.items():
                print(f"{category} : {amount} ")
        else:
            print("За этот месяц расходов нет")

    elif(menu_choice == 9):
            result , month = show_income_by_month()
            if(month is not None):
                print(f"Cумма пополнений за {month}: {result}")
            else:
                print("Неправильная дата")

    elif(menu_choice == 0):
        process = False
