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
            iterate over adjacent vertices O(E)
            """
            for edge in self.adjacencies:
                if edge.here != self.value:
                    yield edge.here
                else:
                    yield edge.there

    def __init__(self, vertices=None, edges=None, directed=False):
        super().__init__(directed)
        self.vertex_dict = {}
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

    def __repr__(self):
        string = ""
        for value in self.vertex_dict:
            string += "\n" + str(value) + ": "
            edges = self.vertex_dict[value].adjacencies
            string += str(edges)
        return string

    def __iter__(self):
        """
        iterate over vertices in Graph O(V)
        """
        for vertex in self.vertex_dict:
            yield vertex

    def __contains__(self, value):
        """
        check if vertex with value value in Graph O(1)
        """
        return value in self.vertex_dict

    def contains_edge(self, here, there):
        """
        check if edge from here to there exists O(1)
        """
        if here in self and there in self:
            here_vertex = self.vertex_dict[here]
            there_vertex = self.vertex_dict[there]
            if not self.directed:
                if here not in there_vertex.adjacent_vertices():
                    return False
            return there in here_vertex.adjacent_vertices()
        return False

    def degree(self, value):
        """
        return number of vertices adjacent to vertex with value value O(1)
        """
        if value in self:
            return self.vertex_dict[value].degree

    def neighbors(self, value):
        """
        return all vertices adjacent to vertex with value value O(E)
        """
        if value in self:
            vertex = self.vertex_dict[value]
            return vertex.adjacent_vertices()

    def edges(self):
        """
        return all edges in Graph O(VE)
        """
        return self.Edges(self)

    def adjacent(self, value, other):
        """
        check if vertices with value value and other have an edge between them O(E)
        """
        if value in self:
            vertex = self.vertex_dict[value]
            return other in vertex.adjacenct_vertices()

    def add_vertex(self, value):
        """
        add vertex with value value to Graph O(1)
        """
        if value not in self:
            vertex = self.Vertex(value)
            self.vertex_dict[value] = vertex
            self.size += 1

    def delete_vertex(self, value):
        """
        delete vertex with value value from Graph O(VE)
        """
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
        get vertex with value value O(1)
        """
        if value in self:
            return self.vertex_dict[value]

    def add_edge(self, here, there, label=None):
        """
        add edge from here to there to Graph O(1)
        """
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
        """
        delete edge from here to there from graph O(1)
        """
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
        if self.contains_edge(here, there):
            pass

    def visit(self, value):
        """
        visit vertex with value value O(1)
        """
        if value in self:
            vertex = self.vertex_dict[value]
            return vertex.visit()

    def visited(self, value):
        """
        check if vertex had been visited O(1)
        """
        if value in self:
            vertex = self.vertex_dict[value]
            return vertex.visited

    def visit_edge(self, here, there):
        """
        visit edge from here to there
        """
        if here in self and there in self:
            here_vertex = self.vertex_dict[here]
            there_vertex = self.vertex_dict[there]
            edge = self.Edge(here_vertex.value, there_vertex.value, directed=self.directed)
            return edge.visit()

    def visited_edge(self, here, there):
        """
        check if edge from here to there has been visited
        """
        if here in self and there in self:
            here_vertex = self.vertex_dict[here]
            there_vertex = self.vertex_dict[there]
            edge = self.Edge(here_vertex.value, there_vertex.value, directed=self.directed)
            return edge.visited

    def reset(self):
        """
        reset visited flag on all edges and vertices
        """
        for value in self.vertex_dict:
            vertex = self.vertex_dict[value]
            vertex.reset()
            for edge in vertex.adjacencies:
                edge.reset()

    def clear(self):
        """
        clear Graph of contents
        """
        self.vertex_dict = {}
        self.size = 0
        self.edge_count = 0

    class Edges:
        """
        iterable for edges in Graph
        """
        def __init__(self, target):
            self.target = target

        def __iter__(self):
            for vertex in self.target:
                for edge in vertex.adjacencies:
                    if self.target.directed or edge.here is vertex.value:
                        yield edge

        def __len__(self):
            return self.target.edge_count()
