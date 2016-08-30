"""abstract class for ADT Stack"""

from abc import ABC, abstractmethod

class Stack(ABC):
    """
    abstract class representing Stack
    """

    @abstractmethod
    def __iter__(self):
        """
        iterate through Stack
        """
        pass

    @abstractmethod
    def __repr__(self):
        """
        representation of Stack
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        check if stack is empty
        """
        pass

    @abstractmethod
    def push(self, value):
        """
        add item to top of stack
        """
        pass

    @abstractmethod
    def pop(self):
        """
        remove and return item at top of stack
        """
        pass

    @abstractmethod
    def peek(self):
        """
        return item at top of stack
        """
        pass
