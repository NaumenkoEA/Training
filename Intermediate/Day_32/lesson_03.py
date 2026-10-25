class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,value):
        if value >= 0:
            self._balance = value
        else:
            print("Balance cannot be negative")

    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Amount less than 0")

    def withdraw(self,amount):
        if amount <= 0:
            print("Amount must be greater than 0")
        elif amount > self.balance:
            print("Not enough money")
        else:
            self.balance = self.balance - amount
        

account = BankAccount("Alex", 2000)

account.withdraw(500)
print(account.balance)

account.withdraw(3000)
print(account.balance)