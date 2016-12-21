class Bill:

    def __init__(self, amount):
        self.amount = self.is_negative(amount)

    def __int__(self):
        return self.amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return "A {}$ bills".format(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

    def __lt__(self, other):
        return self.amount < other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def is_negative(self, amount):
        if not isinstance(amount, int):
            raise TypeError
        if amount < 0:
            raise ValueError
        return amount


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, index):
        return self.bills[index]

    def total(self):
        return sum([int(el) for el in self.bills])


class CashDesk:

    def __init__(self):
        self.bills = []

    def take_money(self, money):
        if isinstance(money, Bill):
            self.bills.append(money)
            return True
        if isinstance(money, BatchBill):
            self.bills.extend(money)
            return True
        return False

    def total(self):
        return sum([int(el) for el in self.bills])

    def inspect(self):
        hist = {}
        for el in self.bills:
            if el in hist.keys():
                hist[el] += 1
            else:
                hist[el] = 1
        res = "We have a total of {total}$ in the desk\nWe have the following count of bills, sorted in ascending order:{hist}". \
            format(total=self.total(), hist=self.format_hist(hist))
        return res

    def format_hist(self, hist):
        res = ""
        for key in sorted(hist.keys()):
            res += "\n{key}$ bills - {value}".format(key=int(key),
                                                     value=hist[key])
        return res


def main():
    batch = BatchBill([Bill(1), Bill(2), Bill(3)])
    for el in batch:
        print(el)
    print(batch.total())
    print(CashDesk().take_money(batch).inspect())


if __name__ == "__main__":
    main()
