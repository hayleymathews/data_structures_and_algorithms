""" python implementation of ADT Stack
with python list (which is really a dynamic array)

note: this list is upside down in order to get O(1) performance
pushing and popping happen at the bottom/end of the list not the top/front
this is because adding/deleting to the top/front of a python list takes O(n)
to make the interface match with the LinkedStack class the iter method cheats
and reverses the list so that it doesn't appear upside down
"""

from Stacks.stack_abstract import Stack

class ArrayStack(Stack):
    """
    implementing ADT Stack
    """
    def __init__(self):
        self.items = []

    def __str__(self):
        return "Stack: " + str(self.items)

    def __iter__(self):
        """
        cheat to iterate through items in way matching LinkedStack
        from most recently added to least recently added
        """
        for item in reversed(self.items):
            yield item

    def __repr__(self):
        if self.is_empty():
            return 'ArrayStack: []'
        return 'ArrayStack: [{0:s}]'.format(', '.join(map(str, self)))

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
        add item to top(really the bottom, see note) of Stack O(1)
        """
        self.items.append(item)

    def pop(self):
        """
        remove item from top(really the bottom, see note) of Stack O(1)
        """
        return self.items.pop()

    def peek(self):
        """
        look at item at top(really the bottom, see note) of Stack O(1)
        """
        return self.items[len(self.items) - 1]
