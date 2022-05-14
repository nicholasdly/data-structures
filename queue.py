class Queue:

    class Node():

        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return repr(self.data)

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def __repr__(self):
        return ", ".join([str(node) for node in self])

    def __str__(self):
        return repr(self)

    def __iter__(self):
        node = self.front
        while node != None:
            yield node
            node = node.next

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, element):
        if self.size == 0:
            self.front = self.Node(element)
            self.back = self.front
        else:
            self.back.next = self.Node(element)
            self.back = self.back.next
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Unable to dequeue from empty queue.")
        if self.size == 1:
            self.back = None
        popped = self.front
        self.front = self.front.next
        self.size -= 1
        return popped