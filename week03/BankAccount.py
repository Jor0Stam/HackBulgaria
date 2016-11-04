import messgs

class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        try:
            self.is_positive(balance)
            self.balance = balance
        except ValueError:
            print("Your balance should be positive integer")
            self.balance = 0
        self.currency = currency
        self.history_of_acc = ["Account was created!"]

    def __int__(self):
        return self.balance

    def __str__(self):
        return messgs.TO_STRING.format(
            name = self.name, amount = self.balance, currency = self.currency)

    def is_positive(self, balance):
        if balance < 0:
            raise ValueError

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        self.history_of_acc.append(messgs.CHECK_BALANCE.format(
            balance=self.balance, currency=self.currency))
        return self.balance

    def withdraw(self, amount):
        status = False

        try:
            self.is_positive(self.balance - amount)
        except ValueError:
            print(messgs.SOME_PHYLOSOPHY_ON_NOT_BEING_ABLE_TO_WITHDRAW)
            self.history_of_acc.append(messgs.WHITDRAW_FAILED.format(amount=amount))
            return status

        self.balance -= amount
        status = True
        self.history_of_acc.append(messgs.WHITDRAW_SUCCEEDED.format(amount=amount))

        return status

    def transfer_to(self, account, amount):
        status = False
        try:
            self.check_currency(self.currency, account.currency)
        except TypeError:
            print(messgs.SOME_PHYLOSPHY_ON_CURENCIES)
            self.history_of_acc.append(messgs.TRANSFER_FAILED.format(
                currency=self.currency, amount=amount, account=account.name))
            return status

        self.withdraw(amount)
        account.deposit(amount)
        status = True
        self.history_of_acc.append(messgs.TRANSFER_SUCCEDED.format(
            currency=self.currency, amount=amount, account=account.name))

        return status

    def check_currency(self, my_curr, other_account_curr):
        if my_curr != other_account_curr:
            raise TypeError

    def history(self):
        return self.history_of_acc
