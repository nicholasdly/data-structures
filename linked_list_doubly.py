class DoublyLinkedList():

    class Node():

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

        def __repr__(self):
            return repr(self.data)

        def __str__(self):
            return str(self.data)

    def __init__(self, elements=None):
        self.head = None
        self.size = 0

        if elements != None:
            for element in elements:
                self.append(element)

    def __repr__(self):
        return " <-> ".join([str(node) for node in self])

    def __str__(self):
        return repr(self)

    def __iter__(self):
        node = self.head
        while node != None:
            yield node
            node = node.next

    def __len__(self):
        return self.size

    def append(self, element):
        if self.head == None:
            self.head = self.Node(element)
        else:
            node = None
            for n in self:
                node = n
            node.next = self.Node(element)
            node.next.prev = node
        self.size += 1

    def clear(self):
        self.head = None
        self.size = 0

    def count(self, element):
        counter = 0
        for node in self:
            if node.data == element:
                counter += 1
        return counter

    def extend(self, sll):
        for node in sll:
            self.append(node.data)

    def index(self, element):
        for index, node in enumerate(self):
            if node.data == element:
                return index

    def insert(self, index, element):
        if index < 0:
            raise IndexError("Unable to insert element at a negative index of a linked list.")

        # Insert element at end
        if index >= self.size:
            self.append(element)

        # Insert element at start
        elif index == 0:
            self.head.prev = self.Node(element)
            self.head.prev.next = self.head
            self.head = self.head.prev
            self.size += 1

        # Insert element inbetween
        else:
            node = self.head
            for _ in range(index):
                node = node.next
            node.prev.next = self.Node(element)
            node.prev.next.prev = node.prev
            node.prev.next.next = node
            node.prev = node.prev.next
            self.size += 1

    def remove(self, element):
        if self.head == None:
            raise ValueError(f"Unable to remove from an empty linked list.")

        # Remove element at start
        if self.head.data == element:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return

        # Remove element at non-starting position
        else:
            for node in self:
                if node.data == element:
                    node.prev.next = node.next
                    if node.next != None:
                        node.next.prev = node.prev
                    self.size -= 1
                    return

        raise ValueError(f"{repr(element)} not in linked list.")

    def pop(self, index):
        if self.size == 0:
            raise IndexError("Unable to pop from empty linked list.")        
        if index < 0 or index >= self.size:
            raise IndexError("Pop index out of range of linked list.")

        # Pop element at start
        if index == 0:
            popped = self.head
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return popped

        # Pop element at non-starting position
        else:
            for i, node in enumerate(self):
                if i == index:
                    node.prev.next = node.next
                    if node.next != None:
                        node.next.prev = node.prev
                    self.size -= 1
                    return node

    def reverse(self):
        if self.size <= 1:
            return

        node = self.head
        while node != None:
            node.prev, node.next = node.next, node.prev
            self.head = node
            node = node.prev