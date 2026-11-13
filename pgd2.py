class BankAccount:
    def __init__(self, account_no, accountname, account_typ,account_balance=0):
        self.account_no = account_no
        self.accountname = accountname
        self.account_typ = account_typ
        self.account_balance = account_balance

    def deposite(self, amount):
        self.account_balance += amount
        print(f"deposited{amount}.new balance:{self.account_balance}")

    def withdraw(self, amount):
        if amount>self.account_balance:
            print("insufficient balance")
        else:
            self.account_balance -= amount
            print(f"withdrawn{amount}.new balance:{self.account_balance}")

acc=BankAccount(101,"anjali","savings",5000)
acc.deposite(2000)
acc.withdraw(1000)

