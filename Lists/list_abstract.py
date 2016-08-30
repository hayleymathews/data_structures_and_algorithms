"""abstract class for ADT List"""

from abc import ABC, abstractmethod

class List(ABC):
    """
    abstract class representing List
    """

    @abstractmethod
    def __init__(self):
        self.head = None
        self.size = 0

    @abstractmethod
    def __iter__(self):
        """
        iterate through List
        """
        pass

    @abstractmethod
    def __repr__(self):
        """
        representation of List
        """
        pass

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
    def prepend(self, value):
        """
        add element to beginning of list
        """
        pass

    @abstractmethod
    def append(self, value):
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

    def find_nth_node_from_end(self, n):
        """
        find and return node that is n elements from end of list
        """
        if n < 0:
            return None
        temp = self.head
        count = 0
        # move temp n spaces from head
        while count < n and temp != None:
            temp = temp.next
            count += 1
        if temp is None:
            return None
        # set nth element to head
        # move nth and temp to next until end of list reached
        nth = self.head
        while temp.next != None:
            temp = temp.next
            nth = nth.next
        return nth

    def detect_cycle(self):
        """
        determine if there is a cycle in the list O(n)
        """
        fast = self.head
        slow = self.head
        while fast and slow:
            fast = fast.next
            if fast == slow:
                return True
            if fast is None:
                return False
            fast = fast.next
            if fast == slow:
                return True
            slow = slow.next

    def detect_cycle_start(self):
        """
        find beginning of cycle O(n)
        """
        if self.head is None or self.head.next is None:
            return None
        slow = self.head.next
        fast = slow.next
        while slow is not fast:
            slow = slow.next
            try:
                fast = fast.next.next
            except AttributeError:
                return None
        slow = self.head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow

    def find_loop_length(self):
        """
        find length of loop if one exists O(n)
        """
        if self.head is None or self.head.next is None:
            return 0
        slow = self.head.next
        fast = slow.next
        while slow is not fast:
            slow = slow.next
            try:
                fast = fast.next.next
            except AttributeError:
                return 0
        loop_length = 0
        slow = slow.next
        while slow is not fast:
            slow = slow.next
            loop_length += 1
        return loop_length
