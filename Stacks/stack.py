""" python implementation of ADT Stack
with python list (which is really a dynamic array)"""

class Stack:
    """
    implementing ADT Stack
    """
    def __init__(self):
        self.items = []

    def __str__(self):
        return "Stack: " + str(self.items)

    def __len__(self):
        """
        get length of Stack O(1)
        """
        return len(self.items)

    def is_empty(self):
        """
        check if stack is empty O(1)
        """
        return self.items == []

    def push(self, item):
        """
        add item to top of Stack O(1)
        """
        self.items.append(item)

    def pop(self):
        """
        remove item from top of Stack O(1)
        """
        return self.items.pop()

    def peek(self):
        """
        look at item at top of Stack O(1)
        """
        return self.items[len(self.items) - 1]
