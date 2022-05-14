class Stack():

    class Node():

        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return repr(self.data)

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.top = None
        self.size = 0

    def __repr__(self):
        return ", ".join([str(node) for node in self])

    def __str__(self):
        return repr(self)

    def __iter__(self):
        node = self.top
        while node != None:
            yield node
            node = node.next

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, element):
        new_node = self.Node(element)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Unable to pop from empty stack.")
        popped = self.top
        self.top = self.top.next
        self.size -= 1
        return popped