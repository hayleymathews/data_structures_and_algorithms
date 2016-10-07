"""abstract class for ADT Graph"""

from abc import ABC, abstractmethod

class Graph(ABC):
    """
    abstract class representing Graph
    """
    class Vertex:
        """
        vertex class for Graph
        """
        def __init__(self, value):
            self.value = value
            self.visited = False
            self.hash = None

        def __eq__(self, other):
            if not isinstance(other, Graph.Vertex):
                return False
            return self.value == other.value

        def __repr__(self):
            return "Vertex: " + str(self.value)

        def __hash__(self):
            if self.hash is None:
                try:
                    self.hash = hash(self.value)
                except TypeError as e:
                    raise e
            return self.hash

        def visit(self):
            """
            set visited flag to true and return previous value
            """
            old_visited = self.visited
            self.visited = True
            return old_visited

        def reset(self):
            """
            reset visited flag
            """
            self.visited = False

    class Edge:
        """
        edge class for Graph
        """
        def __init__(self, here, there, label=None, directed=False):
            self.here = here
            self.there = there
            self.label = label
            self.directed = directed
            self.visited = False
            self.hash = None

        def visit(self):
            """
            set visited flag to true and return previous value
            """
            old_visited = self.visited
            self.visited = True
            return old_visited

        def reset(self):
            """
            reset visited flag
            """
            self.visited = False

        def __eq__(self, other):
            if not isinstance(other, Graph.Edge):
                return False
            if (self.here == other.here) and (self.there == other.there):
                return True
            if not self.directed:
                if (self.here == other.there) and (self.there == other.here):
                    return True
            return False

        def __hash__(self):
            if self.hash is None:
                try:
                    self.hash = hash(self.here) + hash(self.there) + hash(self.label)
                except TypeError as e:
                    raise e
            return self.hash

        def __repr__(self):
            string = str(self.label) + ": "if self.label is not None else ""
            string += str(self.here)
            string += " <> " if not self.directed else " > "
            string += str(self.there)
            return string

    def __init__(self, directed=False):
        self.size = 0
        self.edge_count = 0
        self.directed = directed

    def __len__(self):
        return self.size

    @abstractmethod
    def add_vertex(self, vertex):
        """
        add vertex to Graph
        """
        pass

    @abstractmethod
    def delete_vertex(self, vertex):
        """
        delete vertex from Graph
        """
        pass

    @abstractmethod
    def get_vertex(self, vertex):
        """
        get value of vertex
        """
        pass

    @abstractmethod
    def add_edge(self, here, there, label):
        """
        add edge to Graph
        """
        pass

    @abstractmethod
    def delete_edge(self, here, there):
        """
        delete edge from Graph
        """
        pass

    @abstractmethod
    def get_edge(self, here, there):
        """
        get edge from here to there
        """
        pass

    @abstractmethod
    def __contains__(self, vertex):
        """
        check if vertex in graph
        """
        pass

    @abstractmethod
    def contains_edge(self, here, there):
        """
        check if edge from here to there exists
        """
        pass

    @abstractmethod
    def visit(self, vertex):
        """
        set visited flag on vertex
        """
        pass

    @abstractmethod
    def visit_edge(self, here, there):
        """
        set visited flag on edge
        """
        pass

    @abstractmethod
    def visited(self, vertex):
        """
        returns true if vertex has been visited
        """
        pass

    @abstractmethod
    def visited_edge(self, here, there):
        """
        returns true if edge has been visited
        """
        pass

    @abstractmethod
    def reset(self):
        """
        set all visited flags to False
        """
        pass

    @abstractmethod
    def degree(self, vertex):
        """
        return number of vertices adjacent to vertex
        """
        pass

    @abstractmethod
    def __iter__(self):
        """
        iterate across all vertices of graph
        """
        pass

    @abstractmethod
    def neighbors(self, value):
        """
        return all vertices adjacent to vertex
        """
        pass

    @abstractmethod
    def edges(self):
        """
        return all edges in Graph
        """
        pass

    @abstractmethod
    def clear(self):
        """
        remove all vertices from Graph
        """
        pass

    @abstractmethod
    def adjacent(self, vertex, other):
        """
        check if vertex and other have an edge between them
        """
        pass

    def is_empty(self):
        """
        check if Graph is empty
        """
        return self.size == 0

    def visitable(self, value):
        """
        return all vertices vistable from vertex with value value using DFS
        """
        visited, stack = set(), [value]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(set(self.neighbors(vertex)) - visited)
        return visited - set([value])
