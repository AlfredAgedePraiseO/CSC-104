class StudentAccount(Account):
    def __init__(self, account_number, account_name, balance=0):
         super().__init__(account_number,account_name, balance)

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
