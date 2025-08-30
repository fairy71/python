class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. Balance left = {self.balance}")
        else:
            print("Not enough balance!")

acc = BankAccount("Farah", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(1500)
