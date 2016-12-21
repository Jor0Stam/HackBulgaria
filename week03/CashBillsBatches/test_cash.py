import unittest


from CashBillsBatches import *


class TestCash(unittest.TestCase):

    def setUp(self):
        self.bill = Bill(5)

    def test_bill_equality(self):
        self.assertEqual(self.bill, Bill(5))

    def test_hash(self):
        billz = {self.bill: 1}
        billz[Bill(6)] = 5
        self.assertEqual(billz[self.bill], 1)

    # def test_negative_number(self):
    #     self.assertRaises(ValueError, Bill(-5))


class TestBatch(unittest.TestCase):

    def setUp(self):
        self.batch = BatchBill([Bill(5), Bill(10), Bill(12)])

    def test_indexing(self):
        self.assertTrue(self.batch[1])


class TestDesk(unittest.TestCase):

    def setUp(self):
        self.desk = CashDesk()

    def test_take_money(self):
        self.assertTrue(self.desk.take_money(Bill(5)))
        self.assertTrue(self.desk.take_money(BatchBill([Bill(5), Bill(10),
                                                        Bill(12)])))

    def test_total(self):
        self.desk.take_money(BatchBill([Bill(5), Bill(10), Bill(12)]))
        self.assertEqual(self.desk.total(), 27)


if __name__ == "__main__":
    unittest.main()
