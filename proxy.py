# Real subject class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


# Proxy class
class BankAccountProxy:
    def __init__(self, account):
        self.account = account

    def deposit(self, amount):
        if amount < 0:
            print("Invalid deposit amount")
        else:
            self.account.deposit(amount)

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid withdrawal amount")
        else:
            self.account.withdraw(amount)


# Client code
account = BankAccount(1000)
proxy = BankAccountProxy(account)

proxy.deposit(500)  # Deposited 500. New balance: 1500
proxy.withdraw(200)  # Withdrew 200. New balance: 1300
proxy.deposit(-100)  # Invalid deposit amount
proxy.withdraw(-50)  # Invalid withdrawal amount