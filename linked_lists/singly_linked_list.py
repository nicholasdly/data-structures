
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
            self.head = new_node

    def add_last(self, element):
        if self.head is None:
            self.tail = self.head = self.Node(element)
        else:
            self.tail.next = self.Node(element)
            self.tail = self.tail.next

    def add_after(self, element, index):
        if self.head is None:
            raise Exception("Linked list is empty")
        
        i = 0
        for node in self:
            if i == index:
                new_node = self.Node(element)
                new_node.next = node.next
                node.next = new_node
                return
            i += 1
        raise Exception("Index out of bounds")

    def add_before(self, element, index):
        if self.head is None:
            raise Exception("Linked list is empty")

        if index == 0:
            new_node = self.Node(element)
            new_node.next = self.head
            self.head = new_node
            return

        i = 1
        for node in self:
            if i == index:
                new_node = self.Node(element)
                new_node.next = node.next
                node.next = new_node
                return
            i += 1
        raise Exception("Index out of bounds")

    def remove(self, index):
        if self.head is None:
            raise Exception("Linked list is empty")

        if index == 0:
            self.head = self.head.next
            return

        i = 1
        for node in self:
            if i == index:
                if node.next is None:
                    raise Exception("Index out of bounds")
                node.next = node.next.next
                return
            i += 1
        raise Exception("Index out of bounds")

    def peek(self, index):
        if self.head is None:
            raise Exception("Linked list is empty")

        i = 0
        for node in self:
            if i == index:
                return node.data
            i += 1
        raise Exception("Index out of bounds")

    def clear(self):
        self.head = None
        self.tail = None

def main():
    llist = LinkedList()

if __name__ == "__main__":
    main()