import re


class Bill:

    def __init__(self, amount):
        try:
            self.check_amount(amount)
        except ValueError as e:
            print(e)

        self.amount = amount

    def check_amount(self, amount):
        if amount < 0:
            raise ValueError("ValueError")

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        try:
            self.check_if_int()
        except TypeError:
            print(TypeError)

        return self.amount

    def check_if_int(self):
        if not isinstance(self.amount, int):
            raise TypeError("TypeError")

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.__str__())


class BatchBill:

    def __init__(self, bills):
        self.bills.append(bills)

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum([bill.amount for bill in self.bills])

    def get_bills(self):
        return self.bills


class CashDesk:

    def __init__(self):
        self.cash = {}
        self.total_cash = 0

    def take_money(self, money):
        if not isinstance(money, Bill):
            for bill in money.get_bills():
                self.bill_is_in(bill.__str__())
                self.cash[bill.__str__()] += 1
                self.total_cash += int("".join((re.findall("\d+", bill.__str__()))))
        else:
            self.bill_is_in(money.__str__())
            self.cash[money.__str__()] += 1
            self.total_cash += int("".join((re.findall("\d+", money.__str__()))))

    def bill_is_in(self, bill):
        try:
            self.cash[bill]
        except KeyError:
            self.cash[bill] = 0

    def inspect(self):
        result = ""
        for key, value in self.cash.items():
            result += "\n{}$ bill - {} times\n".format(int("".join((re.findall("\d+", key)))), value)

        return result

    def total(self):
        return self.total_cash


def main():
    b = Bill(-5)


if __name__ == "__main__":
    main()
