"""python implementation of abstract class for ADT Binary Tree"""

from abc import ABC, abstractmethod
from Trees._tree_abstract import Tree

class BinaryTree(Tree, ABC):
    """
    abstract class representing binary tree structure
    """

    @abstractmethod
    def left(self, p):
        """
        return a Position representing p's left child or None if no left child
        """
        pass

    @abstractmethod
    def right(self, p):
        """
        return a Position representing p's right child or None if no right child
        """
        pass

    @abstractmethod
    def add_left(self, e):
        """
        add Element e as left child
        """
        pass

    @abstractmethod
    def add_right(self, e):
        """
        add Element e as right child
        """
        pass

    def sibling(self, p):
        """
        return a Position representing p's sibling or None if no sibling
        """
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """
        generate an iteration of Positions representing p's children
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    # override inherited version to make inorder the default
    def positions(self):
        """
        generate an iteration of the tree's positions
        """
        return self.inorder()

    def inorder(self):
        """
        generate an inorder iteration of positions in the tree
        """
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """
        generate an inorder iteration of positions in subtree rooted at p
        """
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
