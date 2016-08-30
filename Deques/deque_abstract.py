"""abstract class for ADT Deque"""

from abc import ABC, abstractmethod

class Deque(ABC):
    """
    abstract class representing Deque
    """

    @abstractmethod
    def is_empty(self):
        """
        check if deque is empty
        """
        pass

    @abstractmethod
    def insert_first(self, value):
        """
        insert item at front of deque
        """
        pass

    @abstractmethod
    def insert_last(self, value):
        """
        insert item at back of deque
        """
        pass

    @abstractmethod
    def delete_first(self):
        """
        remove and return item at front of deque
        """
        pass

    @abstractmethod
    def delete_last(self):
        """
        remove and return item at back of deque
        """
