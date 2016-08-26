"""python implementation of abstract class for ADT Tree"""

class Tree:
    """
    abstract class representing a tree structure
    """
    class Position:
        """
        abstraction representing location of a single element
        """
        def element(self):
            """
            return element stored at this Position
            """
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """
            return True if other Position represents same location
            """
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """
            return True if other does not represent same location
            """
            raise NotImplementedError('must be implemented by subclass')

    def root(self):
        """
        return Position representing tree's root or None if empty
        """
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """
        return Position representing p's paren of None if p is root
        """
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """
        return number of children Position p has
        """
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """
        generate an iteration of Positions representing p's children
        """
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """
        return total number of elements in tree
        """
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        """
        return True if Position p represents root of tree
        """
        return self.root() == p

    def is_leaf(self, p):
        """
        return True if Position p has no children
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
