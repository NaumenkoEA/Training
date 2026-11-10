import sqlite3
from pathlib import Path
from contextlib import closing

DB_PATH = Path(__file__).parent / "finance.db"

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    return connection

def init_db():
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT,
                date TEXT NOT NULL
                )
        """)   

def add_transaction(transactions_type,amount,category,date):
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO transactions (type, amount, category, date)
                VALUES (?, ?, ?, ?)
    """,(transactions_type,amount,category,date))

def get_transactions():
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM transactions")
            transactions = cursor.fetchall()
    return transactions
    
def get_expenses():
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * FROM transactions
                WHERE type = 'снятие'
            """)
            expenses = cursor.fetchall()
    return expenses

def update_transaction(transaction_id, new_amount):
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE transactions
                SET amount = ?
                WHERE id = ?
            """, (new_amount, transaction_id))

def delete_transaction(transaction_id):
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM transactions
                WHERE id = ?
        """,(transaction_id,)) 

def get_transactions_sorted():
    with closing(get_connection()) as connection :
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT * FROM transactions
                ORDER BY date DESC
        """)
            transactions = cursor.fetchall()
    return transactions

def get_last_transactions(limit):
    with closing(get_connection()) as connection :
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                    SELECT * FROM transactions
                    ORDER BY date DESC
                    LIMIT ?
            """,(limit,))
            transactions = cursor.fetchall()  
    return transactions

def get_total_expenses():
    with closing(get_connection()) as connection :
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT SUM(amount) 
                FROM transactions
                WHERE type = 'снятие'
            """,)
            total_expenses = cursor.fetchone()[0] or 0
    return total_expenses

def get_expenses_by_category():
    with closing(get_connection()) as connection :
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT category , SUM(amount) 
                FROM transactions
                WHERE type = 'снятие'
                GROUP BY category
                ORDER BY SUM(amount) DESC
            """,)
            expenses = cursor.fetchall()
    return dict(expenses)

def get_expenses_by_month(month):
    with closing(get_connection()) as connection :
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT SUM(amount) 
                FROM transactions
                WHERE type = 'снятие'
                AND date LIKE ?
            """,(month + "%",))
            expenses = cursor.fetchone()[0] or 0
    return expenses

def get_income_by_month(month):
    with closing(get_connection()) as connection :
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT SUM(amount) 
                FROM transactions
                WHERE type = 'пополнение'
                AND date LIKE ?
            """,(month + "%",))
            expenses = cursor.fetchone()[0] or 0
    return expenses

def count_expenses_by_category():
    with closing(get_connection()) as connection :
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT category , COUNT(*) 
                FROM transactions
                WHERE type = 'снятие'
                GROUP BY category
            """,)
            expenses = cursor.fetchall()
    return expenses    

def get_average_expense():
    with closing(get_connection()) as connection :
        with connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT AVG(amount)
                FROM transactions
                WHERE type = 'снятие'
            """,)
            average = cursor.fetchone()[0] or 0 
    return average

def get_total_income():
    with closing(get_connection()) as connection :
            with connection:
                cursor = connection.cursor()
                cursor.execute("""
                    SELECT SUM(amount)
                    FROM transactions
                    WHERE type = 'пополнение'
                """,)
                total_income = cursor.fetchone()[0] or 0 
    return total_income

init_db()