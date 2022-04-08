
class LinkedList:
    
    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return str(self.data)

        def __str__(self):
            return repr(self)

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        return " -> ".join(str(node) for node in self)

    def __str__(self):
        return repr(self)

    def append(self, element):
        new_node = self.Node(element)
        if self.head is None:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def clear(self):
        self.head = None
        self.tail = None

    def copy(self):
        new_llist = LinkedList()
        for node in self:
            new_llist.append(node.data)
        return new_llist

    def count(self, element):
        c = 0
        for node in self:
            if node.data == element:
                c += 1
        return c

    def extend(self, elements):
        for val in elements:
            self.append(val)

    def index(self, element):
        i = 0
        for node in self:
            if node.data == element:
                return i
            i += 1
        raise ValueError(f"{repr(element)} is not in LinkedList")

    def insert(self, pos, element):
        pass

    def pop(self, pos):
        pass

    def remove(self, element):
        pass

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # def sort(self):
    #     pass

def main():
    llist = LinkedList()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    llist.extend(nums)
    print(llist)

if __name__ == "__main__":
    main()