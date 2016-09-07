"""python implementation of ADT Linked Binary Tree
use abstract Binary Tree class"""

from Trees._binary_tree_abstract import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """
    linked representation of binary tree structure
    """
    class _Node:
        """
        class for storing a node
        """
        __slots__ = '_element', '_left', '_right'

        def __init__(self, element,left=None, right=None):
            self._element = element
            self._left = left
            self._right = right

        def __repr__(self):
            return "Node\nelement: {}\nleft: {}\nright: {}".format(self._element,
                                                                         self._left,
                                                                         self._right)

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        """
        return the root Node of the tree or None if tree is empty O(1)
        """
        if self._root:
            return self._root
        else:
            return None

    # def parent(self, node):
    #     """
    #     return node's parent or None if p is root O(1)
    #     """
    #     node = self._validate(p)
    #     return self._make_position(node._parent)

    def left(self, node):
        """
        return node's left child or None if no left child O(1)
        """
        if node._left:
            return node._left
        else:
            return None

    def right(self, p):
        """
        return Position of p's right child or None if no right child O(1)
        """
        if
        node = self._validate(p)
        return self._make_position(node._right)

    def add_root(self, e):
        """
        place element e at root of empty tree and return new Position O(1)
        """
        if self._root is not None:
            raise ValueError('root exists')
        self._size = 1
        self._root = self._Node(e)
        self.Position(self, self._root)

    def add_left(self, p, e):
        """
        create a new left child for Position p storing element e O(1)
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("left child exists")
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def add_right(self, p, e):
        """
        create a new right child for Position p storing element e O(1)
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("right node exists")
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def num_children(self, p):
        """
        return number of children of Position p O(1)
        """
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _validate(self, p):
        """
        return associated node if position is valid
        """
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p dont not belong to this container")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """
        return Position instance for given node or None if no node
        """
        return self.Position(self, node) if node is not None else None

    def _replace(self, p, e):
        """
        replace the element at Position p with e, and return old element O(1)
        """
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """
        delete node at Position p, and repace it with its child if any O(1)
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        """
        attach trees t1 and t2 and left and right subtrees of external p O(1)
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
