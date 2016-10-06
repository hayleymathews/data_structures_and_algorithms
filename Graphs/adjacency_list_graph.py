"""python implementation of Graph using adjacency list"""

from Graphs._graph_abstract import Graph

class AdjacencyListGraph(Graph):
    """
    implementing adjacency list graph
    """
    class Vertex(Graph.Vertex):
        """
        vertex for Graph
        """
        def __init__(self, value):
            super().__init__(value)
            self.adjacencies = []

        def add_edge(self, edge):
            """
            add edge to vertex
            """
            if not self.contains_edge(edge):
                self.adjacencies.append(edge)

        def remove_edge(self, edge):
            """
            remove edge from vertex
            """
            return_value = None
            for adjacent_edge in self.adjacencies:
                if adjacent_edge == edge:
                    return_value = adjacent_edge
                    break
            if return_value:
                self.adjacencies.remove(return_value)
            return return_value

        def contains_edge(self, edge):
            """
            check if edge is adjacent to vertex
            """
            return edge in self.adjacencies

        def get_edge(self, edge):
            """
            return edge from adjacencies equal to edge
            """
            for adjacent_edge in self.adjacencies:
                if adjacent_edge == edge:
                    return adjacent_edge

        @property
        def degree(self):
            """
            return number of adjacent edges to vertex
            """
            return len(self.adjacencies)

        def adjacent_vertices(self):
            """
            iterate over adjacent vertices
            """
            for edge in self.adjacencies:
                if edge.here != self.value:
                    yield edge.here
                else:
                    yield edge.there

    def __init__(self, vertices=None, edges=None, directed=False):
        self.directed = directed
        self.vertex_dict = {}
        self.size = 0
        self.edge_count = 0
        if vertices:
            for vertex in vertices:
                self.add_vertex(vertex)
        if edges:
            for edge in edges:
                if len(edge) == 2:
                    self.add_edge(edge[0], edge[1])
                elif len(edge) == 3:
                    self.add_edge(edge[0], edge[1], edge[2])
                else:
                    raise KeyError("Incorrect parameters")

    def __len__(self):
        return self.size

    def __repr__(self):
        pass

    def __contains__(self, value):
        """
        check if vertex with value value in Graph
        """
        return value in self.vertex_dict

    def add_vertex(self, value):
        if value not in self:
            vertex = self.Vertex(value)
            self.vertex_dict[value] = vertex
            self.size += 1

    def delete_vertex(self, value):
        if value in self:
            target = self.vertex_dict[value]
            target.adjacencies = []
            for vertex in self.vertex_dict.values():
                if target in list(vertex.adjacencies):
                    vertex.adjacencies.remove(target)
            self.size -= 1
        else:
            return "Vertex not in Graph"

    def get_vertex(self, value):
        """
        get vertex with value value
        """
        if value in self:
            return self.vertex_dict[value]

    def add_edge(self, here, there, label=None):
        self.add_vertex(here)
        self.add_vertex(there)
        here_vertex = self.vertex_dict[here]
        there_vertex = self.vertex_dict[there]
        new_edge = self.Edge(here_vertex.value, there_vertex.value, label, directed=self.directed)
        here_vertex.add_edge(new_edge)
        if not self.directed:
            there_vertex.add_edge(new_edge)
        self.edge_count += 1

    def delete_edge(self, here, there):
        if self.contains_edge(here, there):
            here_vertex = self.vertex_dict[here]
            there_vertex = self.vertex_dict[there]
            edge = self.Edge(here_vertex.value, there_vertex.value, directed=self.directed)
            old_edge = here_vertex.delete_edge(edge)
            if not self.directed:
                there_vertex.delete_edge(edge)
            self.edge_count -= 1
            return old_edge.value
        else:
            return "Edge not in Graph"

    def get_edge(self, here, there):
        """
        get edge from here to there
        """
        pass

    def degree(self, value):
        if value in self:
            return self.vertex_dict[value].degree

    def __iter__(self):
        for vertex in self.vertex_dict:
            yield vertex

    def contains_edge(self, here, there):
        if here in self and there in self:
            here_vertex = self.vertex_dict[here]
            there_vertex = self.vertex_dict[there]
            if not self.directed:
                if there not in here_vertex.adjacencies:
                    return False
            return here in there_vertex.adjacencies
        return False

    def adjacent(self, value, other):
        if value in self:
            vertex = self.vertex_dict[value]
            return other in vertex.adjacencies

    def clear(self):
        self.vertex_dict = {}
        self.size = 0
        self.edge_count = 0

    def is_empty(self):
        return self.size == 0
