"""python implementaton of ADT Binary Search Tree"""

from Trees._binary_tree_abstract import BinaryTree

class BinarySearchTree(BinaryTree):
    """
    implementing ADT Binary Search Tree
    """
    class Node(BinaryTree.Node):
        """
        extend node for use in Binary Search Tree implementation
        """
        def add(self, value):
            """
            add value to correct place in tree O(logn)
            """
            if value <= self.value:
                self.left = self.add_to_subtree(self.left, value)
            elif value > self.value:
                self.right = self.add_to_subtree(self.right, value)

        def add_to_subtree(self, parent, value):
            """
            helper method to add
            """
            if parent is None:
                return BinarySearchTree.Node(value)
            parent.add(value)
            return parent

        def remove(self, value):
            """
            remove value from tree and correct subtree O(logn)
            """
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
            """
            helper method to remove
            """
            if parent:
                return parent.remove(value)
            return None

    def __len__(self):
        if self.root is None:
            raise ValueError("Binary Tree is empty")
            

    def __contains__(self, value):
        """
        finds value in tree O(log n)
        """
        node = self.root
        while node is not None:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True
        return False

    def add_root(self, value):
        """
        add root node to tree O(1)
        """
        self.root = BinarySearchTree.Node(value)

    def add(self, value):
        """
        add value to tree O(log n)
        """
        if self.root is None:
            self.root = BinarySearchTree.Node(value)
        else:
            self.root.add(value)

    def left(self, p):
        """
        return left child of p O(1)
        """
        return p.left

    def right(self, p):
        """
        return right child of p O(1)
        """
        return p.right

    def parent(self, p):
        pass

    def num_children(self, p):
        pass

    def remove(self, value):
        """
        remove value from tree O(log n)
        """
        if self.root is not None:
            self.root = self.root.remove(value)

    def get_min(self):
        """
        get minimum value from tree O(log n)
        """
        if self.root is None:
            raise ValueError("Binary Tree is empty")
        node = self.root
        while node.left:
            node = node.left
        return node.value

    def get_max(self):
        """
        get maximum value from tree O(log n)
        """
        if self.root is None:
            raise ValueError("Binary Tree is empty")
        node = self.root
        while node.right:
            node = node.right
        return node.value
