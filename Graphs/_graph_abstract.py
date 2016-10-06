"""abstract class for ADT Graph"""

from abc import ABC, abstractmethod

class Graph(ABC):
    """
    abstract class representing Graph
    """
    @property
    def edges(self):
        pass

    @property
    def vertices(self):
        pass

    @abstractmethod
    def __getitem__(self, vertex):
        """
        get value of vertex
        """
        pass

    @abstractmethod
    def __setitem__(self, vertex, value):
        """
        set value of vertex
        """
        pass

    @abstractmethod
    def add_edge(self, edge):
        """
        add edge to Graph
        """
        pass

    @abstractmethod
    def add_vertex(self, vertex):
        """
        add vertex to Graph
        """
        pass

    @abstractmethod
    def delete_edge(self, edge):
        """
        delete edge from Graph
        """
        pass

    @abstractmethod
    def delete_vertex(self, vertex):
        """
        delete vertex from Graph
        """
        pass

    @abstractmethod
    def is_empty(self):
        """
        check if Graph is empty
        """
        pass

    @staticmethod
    def adjacent(vertex, other):
        """
        check if vertex and other have an edge between them
        """
        pass
