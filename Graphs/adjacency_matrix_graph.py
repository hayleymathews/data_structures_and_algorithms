"""python implementation of Graph using adjacency matrix"""

from Graphs._graph_abstract import Graph

class AdjacencyMatrixGraph(Graph):
    """
    implementing adjacency matrix graph
    """
    class Vertex(Graph.Vertex):
        """
        vertex class for matrix Graph
        """
        def __init__(self, value, index):
            """
            override with index property
            """
            super().__init__(value)
            self.index = index

    def __init__(self, vertices=None, edges=None, directed=False):
        super().__init__(directed)
        self.capacity = 0
        self.matrix = []
        self.vertex_dict = {}
        self.free = set()
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

    def __iter__(self):
        for vertex in self.vertex_dict:
            yield vertex

    def __repr__(self):
        string = ""
        for vertex in self.vertex_dict:
            string += "\n" + str(vertex) + ": "
            index = self.vertex_dict[vertex].index
            edges = [x for x in self.matrix[index] if x is not None]
            string += str(edges)
        return string

    def __contains__(self, value):
        """
        check if vertex with value value in Graph
        """
        return value in self.vertex_dict

    def contains_edge(self, here, there):
        """
        check if edge from here to there in Graph
        """
        if here in self and there in self:
            here_vertex = self.vertex_dict[here]
            there_vertex = self.vertex_dict[there]
            return self.matrix[here_vertex.index][there_vertex.index]
        return False

    def degree(self, value):
        """
        return number of vertices adjacent to vertex with value value
        """
        if value in self:
            vertex = self.vertex_dict[value]
            row = self.matrix[vertex.index]
            count = len([edge for edge in row if edge is not None])
            return count

    def neighbors(self, value):
        """
        return all vertices adjacent to vertex with value value
        """
        return self.Neighbors(self, value)

    def edges(self):
        """
        return all edges in Graph
        """
        return self.Edges(self)

    def adjacent(self, value, other):
        """
        check if vertices with value value and other have an edge between them
        """
        if value in self:
            vertex = self.vertex_dict[value]
            row = self.matrix[vertex.index]
            for edge in [edge for edge in row if edge is not None]:
                if edge.here == other or edge.there == other:
                    return True
        return False

    def add_vertex(self, value):
        """
        add vertex with value value to Graph
        """
        if value not in self:
            if len(self.free) != 0:
                index = self.free.pop()
            else:
                index = len(self)
                self.capacity += 1
                for there in self.matrix:
                    there.append(None)
                self.matrix.append([None] * self.capacity)
            self.size += 1
            vertex = self.Vertex(value, index)
            self.vertex_dict[value] = vertex

    def delete_vertex(self, value):
        """
        delete vertex with value value from Graph
        """
        if value in self:
            index = self.vertex_dict[value].index
            count = 0
            for x in range(len(self.matrix[index])):
                if self.matrix[index][x]:
                    count += 1
                    self.matrix[index][x] = None
            self.edge_count = self.edge_count - count
            count = 0
            for there in self.matrix:
                if there[index]:
                    count += 1
                    there[index] = None
            if self.directed:
                self.edge_count = self.edge_count - count
            self.size -= 1
            del self.vertex_dict[value]
        else:
            return "Vertex not in Graph"

    def get_vertex(self, value):
        """
        get vertex with value value
        """
        if value in self:
            return self.vertex_dict[value]

    def add_edge(self, here, there, label=None):
        """
        add edge from here to there to Graph
        add vertices here and there in not in Graph
        """
        if not here in self:
            self.add_edge(here)
        if not there in self:
            self.add_edge(there)
        here_vertex = self.vertex_dict[here]
        there_vertex = self.vertex_dict[there]
        new_edge = self.Edge(here_vertex.value, there_vertex.value, label, directed=self.directed)
        if not self.contains_edge(here, there):
            self.edge_count += 1
        self.matrix[here_vertex.index][there_vertex.index] = new_edge
        if not self.directed:
            self.matrix[there_vertex.index][here_vertex.index] = new_edge

    def delete_edge(self, here, there):
        """
        delete edge from here to there from Graph
        """
        if self.contains_edge(here, there):
            here_vertex = self.vertex_dict[here]
            there_vertex = self.vertex_dict[there]
            old_edge = self.matrix[here_vertex.index][there_vertex.index]
            self.matrix[here_vertex.index][there_vertex.index] = None
            if not self.directed:
                self.matrix[there_vertex.index][here_vertex.index] = None
            self.edge_count -= 1
            return old_edge.label
        else:
            return "Edge not in Graph"

    def get_edge(self, here, there):
        """
        get edge from here to there
        """
        if self.contains_edge(here, there):
            here_vertex = self.vertex_dict[here]
            there_vertex = self.vertex_dict[there]
            return self.matrix[here_vertex.index][there_vertex.index]

    def visit(self, value):
        """
        visit vertex with value value
        """
        if value in self:
            vertex = self.vertex_dict[value]
            return vertex.visit()

    def visited(self, value):
        """
        check if vertex had been visited
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
            edge = self.matrix[here_vertex.index][there_vertex.index]
            return edge.visit()

    def visited_edge(self, here, there):
        """
        check if edge from here to there has been visited
        """
        if here in self and there in self:
            here_vertex = self.vertex_dict[here]
            there_vertex = self.vertex_dict[there]
            edge = self.matrix[here_vertex.index][there_vertex.index]
            return edge.visited

    def reset(self):
        """
        reset visited flag on all edges and vertices
        """
        for value in self.vertex_dict:
            vertex = self.vertex_dict[value]
            vertex.reset()
            row = self.matrix[vertex.index]
            for edge in [e for e in row if e is not None]:
                edge.reset()

    def clear(self):
        """
        clear Graph of contents
        """
        self.size = 0
        self.capacity = 0
        self.edge_count = 0
        self.matrix = []
        self.vertex_dict = {}
        self.free = set()

    class Neighbors:
        """
        iterable for neighbors of vertex
        """
        def __init__(self, target, value):
            self.target = target
            self.value = value

        def __iter__(self):
            g = self.target
            if self.value in g:
                vertex = g.vertex_dict[self.value]
                row = g.matrix[vertex.index]
                for edge in [e for e in row if e is not None]:
                    if edge.here != self.value:
                        yield edge.here
                    else:
                        yield edge.there

        def __len__(self):
            return self.target.degree(self.value)

    class Edges:
        """
        iterable for edges in Graph
        """
        def __init__(self, target):
            self.target = target

        def __iter__(self):
            vertices = self.target.vertex_dict.values()
            for here in vertices:
                row = self.target.matrix[here.index]
                for there in vertices:
                    if self.target.directed or (there.index >= here.index):
                        edge = row[there.index]
                        if edge:
                            yield edge

        def __len__(self):
            return self.target.edge_count
