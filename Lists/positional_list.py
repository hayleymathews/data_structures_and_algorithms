"""python implementation of ADT Positional List using a Doubly Linked List"""

from doubly_linked_list import DoublyLinkedList

class PositionalList(DoublyLinkedList):
    """
    implementing a list that allows positional access
    """
    class Position:
        """
        represents the location of a single element
        """
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return self.node.value

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self.node

        def __ne__(self, other):
            return not self == other

    def _validate(self, p):
        """
        utility method
        return position's node or raise error
        """
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.next is None:
            raise ValueError('p is no longer valid')
        return p.node

    def _make_position(self, node):
        """
        utility method
        return position instance for given node
        """
        if node is self.header or node is self.trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        """
        return first Position in list (or None if list is empty)
        """
        return self._make_position(self.header.next)

    def last(self):
        """
        return last Position in list (or None if list is empty)
        """
        return self._make_position(self.trailer.prev)

    def before(self, p):
        """
        return Position just before Position p
        """
        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p):
        """
        return Position just after Position p
        """
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def insert_between(self, e, predecessor, successor):
        """
        override inherited version to return Position rather than node
        """
        node = super().insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """
        insert element at front of list and return new Position
        """
        return self.insert_between(e, self.header, self.header.next)

    def add_last(self, e):
        """
        insert element at back of list and return new Position
        """
        return self.insert_between(e, self.trailer.prev, self.trailer)

    def add_before(self, p, e):
        """
        insert element into list before Position p and return new Position
        """
        original = self._validate(p)
        return self.insert_between(e, original.prev, original)

    def add_after(self, p, e):
        """
        insert element into list after Position p and return new Position
        """
        original = self._validate(p)
        return self.insert_between(e, original, original.next)

    def delete(self, p):
        """
        remove and return element at Position p
        """
        original = self._validate(p)
        return self.delete_node(original)

    def replace(self, p, e):
        """
        replace element at Position p with e
        return element formerly at p
        """
        original = self._validate(p)
        old = original.value
        original.value = e
        return old
