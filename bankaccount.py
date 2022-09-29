class BankAccount:
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        return self


    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f'Balance: {self.balance}')
        return self
    
    def yield_interest(self):
        self.balance += self.int_rate * self.balance

account1 = BankAccount(0.01, 0)
account1.deposit (300).withdraw(350).withdraw(90).yield_interest()
account1.display_account_info()
account2 = BankAccount(0.01, 0)
account2.deposit(100).withdraw(30).yield_interest()