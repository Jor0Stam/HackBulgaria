import re


class Bill:

    def __init__(self, amount):
        try:
            self.check_amount(amount)
        except ValueError as e:
            print(e)

        self.amount = amount

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

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.__str__())

    def check_amount(self, amount):
        if amount < 0:
            raise ValueError("ValueError")

    def get_amount(self):
        return self.amount

    def check_if_int(self):
        if not isinstance(self.amount, int):
            raise TypeError("TypeError")


class BatchBill:

    def __init__(self, bills):
        self.bills = []
        self.bills.extend(bills)

    def __len__(self):
        return len(self.bills)

    def __str__(self):
        return str([el for el in self.bills])

    def __repr__(self):
        return str([el for el in self.bills])

    def total(self):
        return sum([bill.get_amount() for bill in self.bills])

    def get_bills(self):
        return self.bills


class CashDesk:

    def __init__(self):
        self.cash = {}
        self.total_cash = 0

    def take_money(self, money):
        print(isinstance(money, BatchBill))
        if isinstance(money, BatchBill):
            for bill in money.get_bills():
                if bill in self.cash:
                    self.cash[bill] += 1
                else:
                    self.cash[bill] = 1
                print(int("".join((re.findall("\d+", bill.__str__())))))
        elif isinstance(money, Bill):
            self.bill_is_in(money)
            self.cash[money] += 1
            self.total_cash += int("".join((re.findall("\d+",
                                                       money.__str__()))))
        else:
            print(money)

    def bill_is_in(self, bill):
        try:
            self.cash[bill]
        except KeyError:
            self.cash[bill] = 0

    def inspect(self):
        result = ""
        for key, value in self.cash.items():
            result += "\n{}$ bill - {} times\n".format(
                int("".join((re.findall("\d+", key)))), value)

        return result

    def total(self):
        return self.total_cash


def main():
    b = Bill(5)
    batch = BatchBill([b, Bill(10)])
    print(batch.total())
    kasa = CashDesk()
    kasa.take_money(BatchBill)


if __name__ == "__main__":
    main()
