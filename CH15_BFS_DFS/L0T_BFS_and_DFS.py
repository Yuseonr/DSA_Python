# 15 Aug 2025
# BFS and DFS

# --------------------------------L1 : Breadth First Search (BFS) --------------------------------

class Graph:
    def breadth_first_search(self, v):
        visited_ver = []
        list_of_ver_queue = []
        list_of_ver_queue.append(v)
        while list_of_ver_queue :
            queue_pop = list_of_ver_queue.pop(0)
            visited_ver.append(queue_pop)
            sorted_nbr = sorted(self.graph[queue_pop])
            for vertex in sorted_nbr :
                if vertex not in list_of_ver_queue and vertex not in visited_ver :
                    list_of_ver_queue.append(vertex)
        return visited_ver

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

# --------------------------------L2 : Complete Graph --------------------------------

# 15

# --------------------------------L3 : Complete Graph --------------------------------

# edges connecting each pair of vertices

# --------------------------------L4 : Depth First Search (DFS) --------------------------------

class Graph:
    def depth_first_search(self, start_vertex):
        visited_ver = []
        self.depth_first_search_r(visited_ver, start_vertex)
        return visited_ver

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        neighboors = sorted(self.graph[current_vertex])
        for neighboor in neighboors :
            if neighboor not in visited :
                self.depth_first_search_r(visited,neighboor)

        # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

# --------------------------------L5 : DFS VS BFS --------------------------------

# BFS

# --------------------------------L6 : DFS VS BFS --------------------------------

# BFS

# --------------------------------L7 : DFS VS BFS --------------------------------

# DFS