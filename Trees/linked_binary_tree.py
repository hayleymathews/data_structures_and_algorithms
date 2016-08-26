"""python implementation of ADT Linked Binary Tree
use abstract Binary Tree class"""

from Trees.binary_tree_abstract import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """
    linked representation of binary tree structure
    """
    class _Node:
        """
        class for storing a node
        """
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """
        abstraction representing location of a single element
        """
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """
            return element stored at Position
            """
            return self._node._element

        def __eq__(self, other):
            """
            return True if other is a Position representing same location
            """
            return type(other) is type(self) and other._node is self._node

            
