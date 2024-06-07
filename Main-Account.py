class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

        def deposit(self, amount):
            self.balance += amount

            def withdraw(self, amount):
                self.amount


class SavingsAccount(BankAccount):
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


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_name, balance=0):
        super().__init__(account_number, account_name, balance)

        def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount

            else:
                print("insufficient balance")


class ChildrensAccount(BankAccount):
    def __init__(self, account_number, account_name, balance=0):
        super().__init__(account_number, account_name, balance)

        def withdraw(self, amount):
            print("withdrawal not allowed")

        def add_interest(self):
            interest = 0.14 / 100 * self.balance
            self.deposit(interest)


class StudentAccount(BankAccount):
    def __init__(self, account_number, account_name, balance=0):
        super().__init__(account_number, account_name, balance)

        def withdraw(self, amount):
            if amount <= 2000 and amount <= self.balance:
                self.balance -= amount
            else:
                print("withdrawal limit exceeded")

                def deposit(self, amount):
                    if amount <= 100000:
                        super().deposit(amount)
                    else:
                        print("Deposit limit exceeded")
