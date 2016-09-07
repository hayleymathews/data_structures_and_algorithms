"""python implementation of abstract class for ADT Tree"""

from abc import ABC, abstractmethod
from Queues.linked_queue import LinkedQueue

class Tree(ABC):
    """
    abstract class representing a tree structure
    """

    def __iter__(self):
        """
        generate an iteration of the tree's elements
        """
        for p in self.positions():
            yield p.element()

    @abstractmethod
    def __len__(self):
        """
        return total number of elements in tree
        """
        pass

    @abstractmethod
    def add_root(self, e):
        """
        add Element e as tree's root
        """
        pass

    @abstractmethod
    def root(self):
        """
        return Position representing tree's root or None if empty
        """
        pass

    @abstractmethod
    def parent(self, p):
        """
        return Position representing p's paren of None if p is root
        """
        pass

    @abstractmethod
    def num_children(self, p):
        """
        return number of children Position p has
        """
        pass

    @abstractmethod
    def children(self, p):
        """
        generate an iteration of Positions representing p's children
        """
        pass

    def is_root(self, p):
        """
        return True if Position p represents root of tree O(1)
        """
        return self.root() == p

    def is_leaf(self, p):
        """
        return True if Position p has no children O(1)
        """
        return self.num_children(p) == 0

    def is_empty(self):
        """
        return True if tree is empty
        """
        return len(self) == 0

    def depth(self, p):
        """
        return number of levels separating Position p from root
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def positions(self):
        """
        generate an iteration of the tree's positions
        """
        return self.preorder()

    def preorder(self):
        """
        generate a preorder iteration of positions in the tree
        """
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """
        generate a preorder iteration of positions in subtree rooted at p
        """
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        """
        generate a postorder iteration of positions in the tree
        """
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """
        genereate a postorder iteration of positions in subtree rooted at p
        """
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadth_first(self):
        """
        generate a breadth-first iteratorion of the positions of the tree
        """
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)

    def preorder_indent(self, T, p, d):
        """
        print preorder representation of subtree of T rooted at p at depth d
        """
        print(2*d*' ' + str(p.element()))
        for c in T.children(p):
            self.preorder_indent(T, c, d+ 1)
