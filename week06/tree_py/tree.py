class Node:

    def __init__(self, data):
        self.data = data
        self.next_els = []

    def __eq__(self, other):
        return self.data == other.data


class Tree:

    def __init__(self, root=0):
        self.root = Node(root)

    def add_child(self, parent, data):
        self.create_child(self.get_el(Node(parent), self.root.next_els,
                          self.root), data)

    def create_child(self, parent, data):
        parent.next_els.append(Node(data))

    def get_el(self, el, childs, parent, to_visit=[], visited=[]):
        if parent == el:
            return parent
        if parent in to_visit:
            to_visit.remove(parent)
        visited.append(parent)
        self.append_childs_to_visit(childs, to_visit)
        for child in childs:
            if child not in visited:
                return self.get_el(el, child.next_els, child, to_visit,
                                   visited.append(child))
        return self.get_el(el, to_visit[0].next_els, to_visit[0], to_visit,
                           visited.append(to_visit[0]))

    def append_childs_to_visit(self, childs, to_visit):
        for el in childs:
            to_visit.append(el)

    def remove_el_from_list(self, elem, li):
        for el in li:
            if el.data == elem.data:
                li.remove(el)
        return li

    def get_root(self):
        return self.root


def main():
    t = Tree(5)
    t.add_child(5, 3)
    t.add_child(5, 4)
    t.add_child(3, 2)
    t.add_child(4, 1)
    print(t.get_root().next_els[0].next_els[0].data)


if __name__ == "__main__":
    main()
