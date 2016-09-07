"""python implementation of ADT Binary Tree"""

from Trees._binary_tree_abstract import BinaryTree

class BinaryTree:
    """
    implementing ADT Binary Tree
    """
    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, node):
        """
        insert node to left O(n)
        """
        if self.left_child is None:
            self.left_child = BinaryTree(node)
        else:
            tree = BinaryTree(node)
            tree.left_child = self.left_child
            self.left_child = tree

    def insert_right(self, node):
        """
        insert node to right O(n)
        """
        if self.right_child is None:
            self.right_child = BinaryTree(node)
        else:
            tree = BinaryTree(node)
            tree.right_child = self.right_child
            self.right_child = tree

    def get_left_child(self):
        """
        get left child O(1)
        """
        return self.left_child

    def get_right_child(self):
        """
        get right child O(1)
        """
        return self.right_child

    def set_root(self, root):
        """
        set root of tree O(1)
        """
        self.root = root

    def get_root(self):
        """
        get root of tree O(1)
        """
        return self.root
