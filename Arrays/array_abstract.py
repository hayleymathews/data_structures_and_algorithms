"""abstract class for ADT Array"""

from abc import ABC, abstractmethod

class Array(ABC):
    """
    abstract class representing Array
    """

    @abstractmethod
    def __len__(self):
        """
        return length of Array
        """
        pass

    @abstractmethod
    def __iter__(self):
        """
        iterate through Array
        """
        pass

    @abstractmethod
    def __repr__(self):
        """
        representation of Array
        """
        pass

    @abstractmethod
    def __getitem__(self, index):
        """
        return item at index
        """
        pass

    @abstractmethod
    def __setitem__(self, index, value):
        """
        set value of item at index to value
        """
        pass
