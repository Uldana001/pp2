class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited amount {amount}. New balance: {self.balance}")
        else:
            print("Deposited amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Withdrawal denied.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"


acc = Account("Alice",100)

print(acc)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)
acc.withdraw(-10)
