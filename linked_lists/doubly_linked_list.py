
class LinkedList:
    
    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

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

    def __len__(self):
        l = 0
        for node in self:
            l += 1
        return l

    def add_first(self, element):
        if self.head is None:
            self.tail = self.head = self.Node(element)
        else:
            new_node = self.Node(element)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_last(self, element):
        if self.head is None:
            self.tail = self.head = self.Node(element)
        else:
            new_node = self.Node(element)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def add_after(self, element, index):
        pass

    def add_before(self, element, index):
        pass

    def remove(self, index):
        pass

    def peek(self, index):
        pass

    def clear(self):
        self.head = None
        self.tail = None

def main():
    llist = LinkedList()

if __name__ == "__main__":
    main()