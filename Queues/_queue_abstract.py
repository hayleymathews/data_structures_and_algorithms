"""abstract class for ADT Queue"""

from abc import ABC, abstractmethod

class Queue(ABC):
    """
    abstract class representing Queue
    """

    @abstractmethod
    def is_empty(self):
        """
        check if queue is empty
        """
        pass

    @abstractmethod
    def __len__(self):
        """
        return length of Queue
        """

    @abstractmethod
    def enqueue(self, element):
        """
        add element to back of Queue
        """
        pass

    @abstractmethod
    def dequeue(self):
        """
        remove and return element at front of Queue
        """
        pass
