# 14 Aug 2025
# Graphs

# --------------------------------L1 : Graphs --------------------------------

class Graph:
    def __init__(self, num_vertices):
        self.graph = [[False for _ in range (num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True

    # don't touch below this line

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]

# --------------------------------L2 : Graph review --------------------------------

# False

# --------------------------------L3 : Graph review --------------------------------

# Slightly less than n, where n is the number of vertices (wrong)
# Slightly less than half of n^2, where n is the number of vertices

# --------------------------------L4 : Graph review --------------------------------

# 1, 3, 6

# --------------------------------L5 : Adjecency list --------------------------------

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph :
            self.graph[u] = {v} 
        else :
            # if v not in self.graph[u] :
                self.graph[u].add(v)
        if v not in self.graph :
            self.graph[v] = {u}
        else :
            # if u not in self.graph[v] :
                self.graph[v].add(u)

    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False

# --------------------------------L6 : Representing Graphs --------------------------------

# The node's list will not contain a reference to nodes that it doesn't share an edge with

# --------------------------------L7 : Representing Graphs --------------------------------

# A dictionary of vertices that map to set of vertices

# --------------------------------L8 : Adjacent Nodes --------------------------------

class Graph:
    def adjacent_nodes(self, node):
        return self.graph[node]

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}


# --------------------------------L9 : Unconected Vertices--------------------------------

class Graph:
    def unconnected_vertices(self):
        uv = []
        # if self.graph == {} :
        #     return uv
        for vex in self.graph :
            if not self.graph[vex]  :
                uv.append(vex)
        return uv

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()
