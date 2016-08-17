"""python implementaton of ADT Binary Search Tree"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            self.left = self.add_to_subtree(self.left, value)
        elif value > self.value:
            self.right = self.add_to_subtree(self.right, value)

    def add_to_subtree(self, parent, value):
        if parent is None:
            return Node(value)
        parent.add(value)
        return parent

    def remove(self, value):
        if value < self.value:
            self.left = self.remove_from_parent(self.left, value)
        elif value > self.value:
            self.right = self.remove_from_parent(self.right, value)
        else:
            if self.left is None:
                return self.right
            child = self.left
            while child.right:
                child = child.right
            child_key = child.value
            self.left = self.remove_from_parent(self.left, child_key)
            self.value = child_key
        return self

    def remove_from_parent(self, parent, value):
        if parent:
            return parent.remove(value)
        return None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __contains__(self, value):
        node = self.root
        while node is not None:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True
        return False

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.root.add(value)

    def remove(self, value):
        if self.root is not None:
            self.root = self.root.remove(value)
