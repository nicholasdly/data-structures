
class Stack:

    def __init__(self):
        self.stack = []

    def __repr__(self):
        return " < ".join(self.stack)

    def __str__(self):
        return repr(self)

    def empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def top(self):
        pass

    def push(self, element):
        pass

    def pop(self):
        pass

def main():
    pass

if __name__ == "__main__":
    main()
