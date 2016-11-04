# from cashdeck import Bill, BatchBill, CashDesk
# from fraction import Fraction
# from BankAccount import BankAccount
from derivatives import Polynom


def main():
    # money_holder = {}
    # my_bill = Bill(10)
    # # my_second_bill = Bill(10)

    # # money_holder[my_second_bill] = 1
    # # money_holder[my_bill] = 2

    # values = [10, 20, 50, 100, 100, 100]
    # bills = [Bill(value) for value in values]

    # my_money = BatchBill(bills)

    # desk = CashDesk()

    # desk.take_money(my_money)
    # desk.take_money(my_bill)

    # print(desk.inspect())

    # ratio = Fraction(3, 4)
    # ratio1 = Fraction(2, 4)
    # print(ratio + ratio1)
    # print(ratio - ratio1)
    # print(ratio * ratio1)
    # print(ratio / ratio1)

    # my_acc = BankAccount("Jorko", 257, "BGN")
    # your_acc = BankAccount("Vektor", 257, "EUR")

    # my_acc.withdraw(300)
    # my_acc.get_balance()
    # my_acc.transfer_to(your_acc, 2)
    # print(my_acc.__str__())
    # print(your_acc.__str__())
    # print(my_acc.history())
    poly = Polynom()
    # print(poly.get_diferential())


if __name__ == "__main__":
    main()
