"""python implementation of AA tree"""

class AATree:
    class Node:
        """
        node for AA tree
        """
        left = None
        right = None
        level = 1

        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __repr__(self):
            return 'AANode: key: {0}, value: {1}, level: {2}'.format(self.key, self.value, self.level)


    def insert(self, node, key, value):
        """
        insert node in AA tree
        """
        if node is None:
            return self.Node(key, value)
        if node.key == key:
            node.value = value
        elif key < node.key:
            node.left = self.insert(node.left, key, value)
        else:
            node.right = self.insert(node.right, key, value)
        node = self.skew(node)
        node = self.split(node)
        return node

    def skew(self, node):
        """
        right rotation of tree  to fix illegal states
        """
        if None in [node, node.left]:
            return node
        if node.left.level != node.level:
            return node
        left = node.left
        node.left = left.right
        left.right = node
        return left

    def split(self, node):
        """
        left rotation and level change to fix illegal states
        """
        if None in [node, node.right, node.right.right]:
            return node
        if node.right.right.level != node.level:
            return node
        right = node.right
        node.right = right.left
        right.left = node
        right.level += 1
        return right
