"""abstract class for ADT List"""

from abc import ABC, abstractmethod, abstractproperty

class List(ABC):
    """
    abstract class representing List
    """

    @abstractmethod
    def is_empty(self):
        """
        check if list is empty
        """
        pass

    @abstractmethod
    def __len__(self):
        """
        return length of list
        """
        pass

    @abstractmethod
    def prepend(self):
        """
        add element to beginning of list
        """
        pass

    @abstractmethod
    def append(self):
        """
        add element to end of list
        """
        pass
        
    @abstractmethod
    def delete_first(self):
        """
        delete element at front of list
        """
        pass


    @abstractmethod
    def delete_last(self):
        """
        delete element at end of list
        """
        pass
