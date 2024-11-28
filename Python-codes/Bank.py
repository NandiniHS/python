class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds! Cannot withdraw more than the current balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def check_balance(self):
        print(f"Current balance of {self.account_holder}: {self.balance}")

    def transfer(self, amount, recipient_account):
        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds for transfer.")
        else:
            self.balance -= amount
            recipient_account.deposit(amount)  # Deposit into recipient account
            print(f"Transferred {amount} to {recipient_account.account_holder}. New balance is {self.balance}.")


if __name__ == "__main__":
    account1 = BankAccount("Nandini", 2000)
    account2 = BankAccount("Kavya", 600)
    account1.check_balance()
    account2.check_balance()
    account1.deposit(200)
    account1.withdraw(150)
    account1.transfer(300, account2)
    account1.check_balance()
    account2.check_balance()
