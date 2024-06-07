class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_name, balance=0):
        super().__init__(account_number,account_name, balance)

        def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("insufficient balance")
