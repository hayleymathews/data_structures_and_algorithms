"""python implementation of ADT Binary Tree"""

class BinaryTree:
    """
    implementing ADT Binary Tree
    """
    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, node):
        if self.left_child == None:
            self.left_child = BinaryTree(node)
        else:
            tree = BinaryTree(node)
            tree.left_child = self.left_child
            self.left_child = tree

    def insert_right(self, node):
        if self.right_child == None:
            self.right_child = BinaryTree(node)
        else:
            tree = BinaryTree(node)
            tree.right_child = self.right_child
            self.right_child = tree

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root
