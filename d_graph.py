# Course: CS261 - Data Structures
# Author: Jesse Zelaya
# Assignment: Assignment 6
# Description: Implements Graph


class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []#[[0,0,0],[0,0,0],[0,0,0]]

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
            Adds vertex to given graph and adjusts count
        """
        self.v_count +=1
        self.adj_matrix.append([])

        for n in range(len(self.adj_matrix)):
            li = self.adj_matrix[n]
            while len(li) < self.v_count:
                li.append(0)
        return self.v_count



    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
            Adds an edge between vertices
        """
        if weight < 1 or src == dst:
            return None

        try:
            self.adj_matrix[src][dst] = weight
        except:
            pass
        return None

    def remove_edge(self, src: int, dst: int) -> None:
        """
            Removes edge between two vertices
        """
        if src < 0 or dst < 0:
            return None
        try:
            if self.adj_matrix[src][dst] == 0:
                return None
            self.adj_matrix[src][dst] = 0
        except:
            pass
        return None
        

    def get_vertices(self) -> []:
        """
        Returns a list of vertices in graph
        """
        verts = []
        for i in range(self.v_count):
            verts.append(i)
        return verts

    def get_edges(self) -> []:
        """
            Returns a list of all the edges in graph
        """
        edges = []

        # iterate through vertices and append vertices and weight
        for i in range(self.v_count):
            for j in range(len(self.adj_matrix[i])):
                if self.adj_matrix[i][j] > 0:
                    edges.append((i,j,self.adj_matrix[i][j]))
        return edges


    def is_valid_path(self, path: []) -> bool:
        """
            Returns True/False if given path is valid in graph
        """
        flip = True

        if path == []:
            return True

        for i in range(len(path)-1):
            if self.adj_matrix[path[i]][path[i + 1]] == 0:
                return False

        return True

    def dfs_help(self, v_start, v_end, visited, graphStack):
        """DFS helper function"""
        if graphStack == [] or v_start == v_end:
            return visited

        # pop vertex from stack
        v_start = graphStack.pop()

        # push vertex neighbors onto stack
        if v_start not in visited:
            visited.append(v_start)

            try:
                tempNodes = []
                count = 0
                for we in self.adj_matrix[v_start]:
                    if we != 0:
                        tempNodes.append(count)
                    count += 1
                # sort reverse for dfs
                tempNodes.sort(reverse = True)
                if tempNodes:
                    for v in tempNodes:
                        graphStack.append(v)
            except:
                pass

        return self.dfs_help(v_start, v_end, visited, graphStack)

    def dfs(self, v_start, v_end=None) -> []:
        """
        Performs DFS of graph, given a vertex for start and end.
        Defaults no end vertex to None
        """
        # initialize visited list and graph stack for dfs
        visited = []
        graphStack = []

        startBool = False
        endBool = False

        # push vertex to stack and check if vertices are valid before calling help
        graphStack.append(v_start)

        if startBool <= self.v_count:
            startBool = True
        if endBool <= self.v_count:
            endBool = True

        if startBool == False:
            return []

        if endBool == False:
            v_end == None

        if v_start == v_end:
            return []
        return self.dfs_help(v_start, v_end, visited, graphStack)

    def bfs_help(self,v_start, v_end, visited, graphQueue):
        """Helper function for BFS function"""
        if graphQueue == [] or v_start == v_end:
            return visited

        # dequeue vertex
        v_start = graphQueue.pop(0)

        if v_start not in visited:
            visited.append(v_start)
            # queue vertices onto queue in sorted order
            try:
                tempNodes = []
                count = 0
                for we in self.adj_matrix[v_start]:
                    if we != 0:
                        tempNodes.append(count)
                    count += 1
                tempNodes.sort()
                if tempNodes:
                    for v in tempNodes:
                        graphQueue.append(v)
            except:
                pass

        return self.bfs_help(v_start, v_end, visited, graphQueue)

    def bfs(self, v_start, v_end=None) -> []:
        """
        Performs BFS given start vertex and end vertex
        """
        # initialize visited and queue for BFS
        visited = []
        graphQueue = []

        startBool = False
        endBool = False

        graphQueue.append(v_start)
        # check valid entries before calling helper function
        if startBool <= self.v_count:
            startBool = True
        if endBool <= self.v_count:
            endBool = True

        if startBool == False:
            return []

        if endBool == False:
            v_end == None

        if v_start == v_end:
            return []

        return self.bfs_help(v_start, v_end, visited, graphQueue)

    def get_neighbors(self, vert) -> []:
        """returns list of neighbors
           in sorted order"""
        graphRow = self.adj_matrix[vert]
        neighbors = []
        for i in range(self.v_count):
            if graphRow[i] > 0:
                neighbors.append(i)
        neighbors.sort()
        return neighbors


    def move_vertex(self, current, from_li, to_li):
        """moves vertex between lists"""
        # does not raise exception if not in white list
        try:
            from_li.remove(current)
        except:
            pass
        to_li.append(current)


    def cycle_dfs(self, v_curr, white, grey, black) -> bool:
        """dfs for detecting cycle"""
        # move current vertex from white to grey
        self.move_vertex(v_curr, white, grey)

        # get list of neighbors
        neighbors = self.get_neighbors(v_curr)

        # iterate through neighbors
        for node in neighbors:
            if node in black:
                continue
            if node in grey:
                return True
            if self.cycle_dfs(node, white, grey, black) == True:
                return True

        self.move_vertex(v_curr, grey, black)
        return False



    def has_cycle(self):
        """
        detects cycle in directed graph
        """

        # get all vertices and store in white list. initialize white/grey/black lists
        white, grey, black = [],[],[]
        verts = self.get_vertices()
        verts.sort(reverse=True)
        for v in verts:
            white.append(v)

        # run through each white vertex
        while white:
            v_curr = white.pop()
            if self.cycle_dfs(v_curr, white, grey, black) is True:
                return True
        return False


    def dijkstra(self, src: int) -> []:
        """
            Returns list of shortest distance to vertices from src
        """
        # initialize distance dictionary and add each distance
        distance = []
        visited = {}

        # Initialize an empty map/hash table representing visited vertices
        #visited[src] = 0

        # Initialize an empty priority queue, and insert vs into it with distance (priority) 0.
        priorityQ = []
        priorityQ.append((src, 0))
        minDist = []
        for i in range(self.v_count):
            minDist.append(float('inf'))
        minDist[src] = 0
        while priorityQ:
            # Remove the first element (a vertex) from the priority queue
            # and assign it to v. Let d be v’s distance (priority).
            vee, dee = priorityQ.pop(0)

            if dee > minDist[vee]:
                continue

            neighbors = self.get_neighbors(vee)
            for n in neighbors:
                distance = dee + self.adj_matrix[vee][n]
                # keep track if new distance is less than the current distance to that node
                if distance < minDist[n]:
                    minDist[n] = distance
                    priorityQ.append((n, distance))


        return minDist




       



if __name__ == '__main__':
    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = DirectedGraph()
    # print(g)
    # for _ in range(5):
    #     g.add_vertex()
    # print(g)
    #
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # for src, dst, weight in edges:
    #     g.add_edge(src, dst, weight)
    # print(g)
    #
    # print(g.get_edges())
    #
    # print("\nPDF - method get_edges() example 1")
    # print("----------------------------------")
    # g = DirectedGraph()
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    #
    #
    # print("\nPDF - method is_valid_path() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    #
    # for path in test_cases:
    #     print(path, g.is_valid_path(path))
    # print('done')
    #
    # print("\nPDF - method dfs() and bfs() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    #
    # for start in range(5):
    #     print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)

    print('----')
    # g = DirectedGraph([(0, 1, 10), (1, 4, 15), (2, 1, 23), (3, 2, 7), (4, 3, 3)])
    # print(g)
    # g.has_cycle()
    # print("\nPDF - dijkstra() example 1")
    # print("--------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for i in range(5):
    #     print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    # g.remove_edge(4, 3)
    # print('\n', g)
    # for i in range(5):
    #     print(f'DIJKSTRA {i} {g.dijkstra(i)}')

    g = DirectedGraph([(4,0,12),(4,3,3),(3,1,5),(3,2,7),(2,1,23),(1,4,15),(0,1,10)])

    print(g)

    print(g.dijkstra(4))
