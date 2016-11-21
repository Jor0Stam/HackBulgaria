import unittest
from ll_boiler_plate import LinkedList, DoubleLinkedList


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_adding_element(self):
        self.ll.add_element(4)
        self.assertEqual(self.ll.size(), 1)

    def test_index(self):
        self.ll.add_element(4)
        self.assertEqual(self.ll.index(0).data, 4)
        self.ll.add_element(6)
        self.ll.add_element(5)
        self.assertEqual(self.ll.index(1).data, 6)

    def test_remove_element(self):
        self.ll.add_element(4)
        size = self.ll.size()
        self.ll.remove(0)
        size2 = self.ll.size()
        self.assertFalse(size == size2)

    def test_to_list(self):
        for i in range(4):
            self.ll.add_element(i)
        self.assertEqual(self.ll.to_list(), [0, 1, 2, 3])

    def test_add_at_index(self):
        self.ll.add_element(6)
        self.ll.add_element(5)
        self.ll.add_element(4)
        self.ll.add_element(3)
        self.ll.add_at_index(self.ll.size() - 1, 7)
        self.assertEqual(self.ll.to_list(), [6, 5, 4, 3, 7])
        self.ll.add_at_index(3, 8)
        self.assertEqual(self.ll.to_list(), [6, 5, 4, 8, 3, 7])

    def test_add_first(self):
        self.ll.add_element(6)
        self.ll.add_element(5)
        self.ll.add_first(7)
        self.assertEqual(self.ll.to_list(), [7, 6, 5])

    def test_pop(self):
        self.ll.add_element(6)
        self.ll.add_element(5)
        self.ll.add_element(7)
        self.assertEqual(self.ll.pop().data, 7)

    def test_ll_from_to(self):
        self.ll.add_element(0)
        self.ll.add_element(1)
        self.ll.add_element(2)
        self.ll.add_element(3)
        self.ll.add_element(4)
        self.ll.add_element(5)
        self.assertEqual(self.ll.ll_from_to(2, 4).to_list(), [2, 3, 4])

    def test_reduce_to_unique(self):
        self.ll.add_element(1)
        self.ll.add_element(2)
        self.ll.add_element(2)
        self.ll.add_element(3)
        self.ll.add_element(3)
        self.ll.add_element(0)
        self.assertEqual(self.ll.reduce_to_unique().to_list(), [1, 2, 3, 0])

    def test_add_list(self):
        self.ll.add_element(0)
        self.ll.add_element(1)
        self.ll.add_element(2)
        self.ll.add_element(3)
        self.ll.add_element(4)
        self.ll.add_list([5, 6])
        self.assertEqual(self.ll.to_list(), [0, 1, 2, 3, 4, 5, 6])

    def test_add_linked_list(self):
        self.ll.add_element(0)
        self.ll.add_element(1)
        self.ll.add_element(2)
        ll1 = LinkedList()
        ll1.add_element(3)
        ll1.add_element(4)
        self.ll.add_linked_list(ll1)
        self.assertEqual(self.ll.to_list(), [0, 1, 2, 3, 4])


class TestDoubleList(unittest.TestCase):

    def setUp(self):
        self.dll = DoubleLinkedList()

    def test_adding_element(self):
        self.dll.add_element(4)
        self.assertEqual(self.dll.size(), 1)

    def test_index(self):
        self.dll.add_element(4)
        self.assertEqual(self.dll.index(0).data, 4)
        self.dll.add_element(6)
        self.dll.add_element(5)
        self.assertEqual(self.dll.index(1).data, 6)

    def test_remove_element(self):
        self.dll.add_element(4)
        size = self.dll.size()
        self.dll.remove(0)
        size2 = self.dll.size()
        self.assertFalse(size == size2)


if __name__ == '__main__':
    unittest.main()
