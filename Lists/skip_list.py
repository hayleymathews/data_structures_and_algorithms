"""python implementation of ADT skip list"""

import math
from random import random
from functools import total_ordering


class SkipList():
    """
    implementing ADT Skip List
    """
    class Node:
        """
        node for skip list
        """
        def __init__(self, value, next=None, width=None):
            self.value = value
            self.next = next
            self.width = width

        def __repr__(self):
            return str(self.value)

    @total_ordering
    class End:
        """
        sentinel object to compare greater
        """
        def __eq__(self, other):
            return False

        def __gt__(self, other):
            return True

        def __lt__(self, other):
            return False

    def __init__(self, expected_size=100):
        self.size = 0
        self.max_levels = int(1 + math.log(expected_size, 2))
        self.head = self.Node('HEAD')
        self.tail = [self.Node(self.End())] * self.max_levels
        self.head.next = self.tail
        self.head.width = [1] * self.max_levels

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head.next[0]
        while node.next:
            yield node.value
            node = node.next[0]

    def __repr__(self):
        if self.head.next is None:
            return 'SkipList: []'
        return 'SkipList: [{0:s}]'.format(', '.join(map(str, self)))

    def __getitem__(self, index):
        """
        find item at index O(logn)
        """
        node = self.head
        index += 1
        for level in reversed(range(self.max_levels)):
            while node.width[level] <= index:
                index -= node.width[level]
                node = node.next[level]
        return node.value

    def insert(self, value):
        """
        insert value in skip list O(logn)
        """
        tower = [None] * self.max_levels
        steps_at_level = [0] * self.max_levels
        node = self.head
        for level in reversed(range(self.max_levels)):
            while node.next[level].value <= value:
                steps_at_level[level] += node.width[level]
                node = node.next[level]
            tower[level] = node
        d = min(self.max_levels, 1 - int(math.log(random(), 2.0)))
        node = self.Node(value, [None] * d, [None] * d)
        steps = 0
        for level in range(d):
            prev = tower[level]
            node.next[level], prev.next[level] = prev.next[level], node
            node.width[level] = prev.width[level] - steps
            prev.width[level] = steps + 1
            steps += steps_at_level[level]
        for level in range(d, self.max_levels):
            tower[level].width[level] += 1
        self.size += 1

    def remove(self, value):
        """
        delete value from skip list O(logn)
        """
        tower = [None] * self.max_levels
        node = self.head
        for level in reversed(range(self.max_levels)):
            while node.next[level].value < value:
                node = node.next[level]
            tower[level] = node
        if value != tower[0].next[0].value:
            raise KeyError('Not Found')
        d = len(tower[0].next[0].next)
        for level in range(d):
            prev = tower[level]
            prev.width[level] += prev.next[level].width[level] - 1
            prev.next[level] = prev.next[level].next[level]
        for level in range(d, self.max_levels):
            tower[level].width[level] -= 1
        self.size -= 1
