# Course: Data Structures
# Author: Jesse Zelaya
# Assignment: Assignment 6
# Description: Implements undirected graph

class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
            This method adds a vertex to the adjacency list
        """

        self.adj_list[v] = []
        
    def add_edge(self, u: str, v: str) -> None:
        """
        Checks if initial vertex is in adjacency list
        If it's in the list then it adds edge to next vertex.
        It then adds edge from the second vertex back to the first.
        """
        # if vertices are not in list, then add them and then proceed to add edges
        if u == v:
            return None
        if u not in self.adj_list:
            self.add_vertex(u)
        if v not in self.adj_list:
            self.add_vertex(v)

        v_edge = self.adj_list.get(u)
        if v not in v_edge:
            v_edge.append(v)

        v_edge = self.adj_list.get(v)
        if u not in v_edge:
            v_edge.append(u)

    def remove_edge(self, v: str, u: str) -> None:
        """
        removes edge connection between two vertices
        """



        if v in self.adj_list and u in self.adj_list:
            try:
                edgeBeGone = self.adj_list.get(v)
                edgeBeGone.remove(u)
                edgeBeGone = self.adj_list.get(u)
                edgeBeGone.remove(v)
            except:
                pass

    def remove_vertex(self, v: str) -> None:
        """
        Removes vertex and any edge associated with it
        """



        if v is not None and v in self.adj_list:
            edgesBeGone = self.adj_list.get(v)

            # store initial value of edges length to use in loop
            edgelength = len(edgesBeGone)

            # pop each value and call remove edge and then pop off the vertex
            for i in range(0, edgelength):
                edge = edgesBeGone.pop()
                self.remove_edge(edge, v)
                # edges.append(vert)
            # for vert in edges:
            #     self.remove_edge(vert, v)
            self.adj_list.pop(v)
        

    def get_vertices(self) -> []:
        """
        Adds keys to vertex_list and returns it
        """
        vertex_list = []
        for key in self.adj_list:
            vertex_list.append(key)
        return vertex_list

    def get_edges(self) -> []:
        """
        Keeps a list of unique (already used) edge points.
        Saves main vertex and vertex it's connected to to edge_list

        """
        edge_list = []
        vertex_unq = []

        # get each list from each key and save to edge list as tuple
        for key in self.adj_list:
            vertex_unq.append(key)

            # gets list for each key
            key_lst = self.adj_list[key]
            for vert in key_lst:
                if vert not in vertex_unq:
                    edge_list.append((key, vert))
        return edge_list

    def is_valid_path(self, path: []) -> bool:
        """
        Checks if path is empty. If not then it
        Checks for a single value in path and if it is in adjacency list.
        Checks for each path edge in while loop and returns false if there is
        no edge.
        """

        valid_path = True

        if path == [] or (len(path) == 1 and path[0] in self.adj_list):
            return True
        elif (len(path) == 1 and path[0] not in self.adj_list):
            return False

        count = 0   # checks count of path
        while count < len(path) - 1:

            try:
                if path[count +1] not in self.adj_list[path[count]]:
                    return False
            except:
                pass

            count += 1

        return valid_path

    def dfs_help(self, v_start, v_end = None, stackGraph = [], visited = []):
        """ Helper function for dfs, contains
            visited list, and current stack for dfs
            used for recursive calling"""

        # push direct successors onto stack
        if v_start not in visited:
            v_sucs = self.adj_list.get(v_start)
            v_sucs.sort(reverse=True)
            for v in v_sucs:
                if v not in visited:
                    stackGraph.append(v)

            visited.append(v_start)

        # check if stack is empty and return visited list if so
        if stackGraph == []:
            return visited
        # pop next vertex
        v_start = stackGraph.pop()

        if v_start == v_end:
            visited.append(v_start)
            return visited

        return self.dfs_help(v_start, v_end, stackGraph, visited)

    def dfs(self, v_start, v_end=None) -> []:
        """
            uses stack to perform depth first search
        """

        # check starting vertex and end
        # checked to see how to treat end and if v_start is in adj_list
        try:
            if v_start not in self.adj_list:
                return []
        except:
            pass

        try:
            if v_end not in self.adj_list:
                v_end = None
        except:
            pass
        if v_start == v_end:
            return [v_start]

        # initialize set of visited vertices
        visited = []

        # initialize stack
        stackGraph = []

        # add v_start to stack
        stackGraph.append(v_start)

        # call helper function
        return self.dfs_help(v_start, v_end, stackGraph, visited)

    def bfs_help(self, v_start, v_end, visited, queueGraph):
        """
            helper function for breadth first search
        """

        if v_start not in visited:
            v_succ = self.adj_list.get(v_start)
            v_succ.sort()
            for v in v_succ:
                queueGraph.append(v)
            visited.append(v_start)

        # # check if q is empty
        if queueGraph == [] :
            return visited
        # pop next vertex
        v_start = queueGraph.pop(0)

        if v_start == v_end:
            visited.append(v_end)
            return visited

        return self.bfs_help(v_start, v_end, visited, queueGraph)

    def bfs(self, v_start, v_end=None) -> []:
        """
            uses breadth first search to return visited list of vertices
        """
        if v_start == v_end:
            return [v_start]
        # initialize queue
        queueGraph = []

        # initialize visited
        visited = []

        # check if v_start is in adjacency list
        try:
            if v_start not in self.adj_list:
                return []
        except:
            pass

        # check if v_end is in the adjacency list, if not v_end is None
        try:
            if v_end not in self.adj_list:
                v_end = None
        except:
            pass

        # append v_start to the queue and call helper function
        #queueGraph.append(v_start)

        return self.bfs_help(v_start, v_end, visited, queueGraph)

    def count_connected_components(self):
        """
        counts how many connected isolated components there are in the graph
        """
        vees = self.get_vertices()
        visited = []
        count = 0

        for v in vees:
            if v not in visited:
                temp = self.bfs(v)
                for u in temp:
                    visited.append(u)
                count += 1

        return count


    def has_cycle(self):
        """
        detects if udgraph has a cycle which leads to a circular rotation of nodes
        """

        vees = self.get_vertices()
        ends = []
        visited = []
        cStack = []
        parent = None
        count =  0
        for v in vees:
            cStack = []
            if self.adj_list[v] != [] and v not in visited:
                v_start = v
                #break

                cStack.append((v_start,-1))
                count = 0
                while cStack:
                    #parent = v_start
                    v_start, parent= cStack.pop()


                    # v_start neighbors
                    temps = self.adj_list[v_start]
                    temps.sort(reverse = True)

                    # add v_start to visited
                    visited.append(v_start)

                    for v in temps:
                        if v not in visited:
                            cStack.append((v,v_start))
                            if len(self.adj_list[v]) == 1:
                                ends.append(v)
                        elif v != parent:
                            return True
        print(parent, v_start)
        return False





   


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)


    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    print(g)
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'D')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)


    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))

    #
    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    print("my test DFS")
    print(g.dfs('K'))

    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')

    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    print('************')
    edges = ['DJ', 'DA', 'DC', 'DB', 'IJ', 'AD', 'CD', 'CB', 'CF', 'BD', 'BC', 'EK', 'KE', 'FC']
    g = UndirectedGraph(edges)
    print(g)
    print("my test DFS")
    print('hi', g.dfs('k'))


    print('************')

    print('************')
    edges = ['GJ', 'GD', 'GK', 'JG', 'JD', 'HC', 'HA', 'CH', 'CK', 'DG', 'DJ', 'KG', 'KC', 'AH']
    g = UndirectedGraph(edges)
    print(g)
    print(g.get_vertices())
    print("my test DFS")
    print('hi', g.dfs('k'))

    print('************')
    #
    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print(g.count_connected_components(), end=' ')
    # print()
    # print('-----')
    # edges = ['JE', 'JK', 'EJ', 'EK', 'CA', 'AC', 'AG', 'BI', 'BF', 'BD', 'BG',
    #          'IB','GA','GB','FB','KJ','KE','DB']
    # g = UndirectedGraph(edges)
    # print(g)
    # print(g.count_connected_components())
    # #
    # #
    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())

    #g = UndirectedGraph(['AE','AC','EF','EA','CD','CA','BH','BD','DC','DB','HB','QG'])
    g = UndirectedGraph(['GE','EG','EI','IE','HJ','HC','JH','JC','BC','CB','CH','CJ','DK','DA','KD','AD'])
    print(g)

    print(g.dfs('A'))
    print(g.has_cycle())