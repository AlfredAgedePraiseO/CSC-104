class SavingsAccount(Account):
    def __init__(self, account_number, account_name, balance=0):
        super().__init__(account_number, account_name, balance)

        def withdraw(self, amount):
            if amount <= 500000 and amount <= self.balance:
                self.balance -= amount
            else:
                print("withdrawal limit exceeded")

                def add_interest(self):
                    interest = 2.5 / 100 * self.balance
                    self.deposit(interest)