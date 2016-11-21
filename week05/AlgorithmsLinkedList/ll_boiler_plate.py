class Node:

    def __init__(self, data):
        self.data = data
        self.next_el = None

    def __str__(self):
        return "{}".format(self.data)

    def __repr__(self):
        return "{}".format(self.data)


class LinkedList:

    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None

    def add_element(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp = Node(data)
            self.tail.next_el = temp
            self.tail = temp
        self._size += 1

    def index(self, index_new):
        # curr = self.head
        # for i in range(index_new):
        #     curr = curr.next_el
        return self.index_recursion(self.head, index_new)

    def index_recursion(self, curr, ind):
        if ind == 0:
            return curr
        else:
            return self.index_recursion(curr.next_el, ind - 1)

    def size(self):
        return self._size

    def remove(self, index_new):
        curr = self.head
        if index_new == 0:
            self.head = self.head.next_el
        elif index_new == self.size() - 1:
            curr = self.index(index_new - 1)
            self.tail = curr
        else:
            curr = self.index(index_new)
            temp = curr.next_el.next_el
            curr.next_el = None
            curr.next_el = temp
        self._size -= 1

    def pprint(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.__str__() + "->")
            curr = curr.next_el
        return "".join(result)[:-2]

    def to_list(self):
        result = []
        for i in range(self.size()):
            result.append(self.index(i).data)
        return result

    def add_at_index(self, index_new, data):
        if index_new == 0:
            self.add_first(data)
        elif index_new == self.size() - 1:
            temp = self.tail
            self.tail = Node(data)
            temp.next_el = self.tail
            self._size += 1
        else:
            curr = self.index(index_new - 1)
            temp = curr.next_el
            curr.next_el = Node(data)
            curr.next_el.next_el = temp
            self._size += 1

    def add_first(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next_el = temp
        self._size += 1

    def add_list(self, data_list):
        for el in data_list:
            self.add_element(el)

    def add_linked_list(self, data_Linkedlist):
        for el in data_Linkedlist.to_list():
            self.add_element(el)

    def ll_from_to(self, start_index, end_index):
        new_ll = LinkedList()
        for i in range(start_index, end_index + 1):
            new_ll.add_element(self.index(i).data)
        return new_ll

    def pop(self):
        temp = self.index(self.size() - 1)
        self.tail = self.index(self.size() - 2)
        return temp

    def reduce_to_unique(self):
        new_ll = LinkedList()
        data_stored = []
        for el in self.to_list():
            if el not in data_stored:
                data_stored.append(el)
        for i in range(len(data_stored)):
            new_ll.add_element(data_stored[i])
        return new_ll

    def get_uniques(self, ll):
        pass


class DoubleNode(Node):

    def __init__(self, data):
        super().__init__(data)
        self.prev_el = None

    def __str__(self):
        return "{}".format(self.data)

    def __repr__(self):
        return "{}".format(self.data)


class DoubleLinkedList(LinkedList):

    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None

    def add_element(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp = Node(data)
            temp.prev_el = self.tail
            self.tail.next_el = temp
            self.tail = temp
        self._size += 1

    def remove(self, index_new):
        curr = self.head
        if index_new == 0:
            self.head = self.head.next_el
        elif index_new == self.size() - 1:
            curr = self.index(index_new - 1)
            curr.prev_el = None
            self.tail = curr
        else:
            curr = self.index(index_new)
            temp = curr.next_el.next_el
            curr.next_el.prev_el = None
            curr.next_el.next_el = None
            curr.next_el = temp
        self._size -= 1

    def pop(self):
        temp = self.index(self.size() - 1)
        self.tail = temp.prev_el
        temp.prev_el = None
        return temp

    def pprint(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.__str__() + "<->")
            curr = curr.next_el
        return "".join(result)[-2:]

    def add_last(self, data):
        pass

    def remove_last(self, data):
        pass


def main():
    ll = LinkedList()
    ll.add_element(4)
    ll.add_element(5)
    ll.add_element(6)
    ll.add_element(7)
    ll.add_element(8)
    print(ll.pprint())


if __name__ == "__main__":
    main()
