class GraphByAdjMatrix:
    
    '''
        Graph implementation by Adjacency Matrix Method:
    '''

    def __init__(self):
        self.vertices = []
        self.graph = []

    def vertice_col(self):
        for row in self.graph:
            row.append(0)
        
    def vertice_row(self):
        row = [0 for i in range(len(self.vertices))]
        self.graph.append(row)

    def add_vertices(self,v:int):
        if v in self.vertices:
            print('------- Vertices is already in graph-----')
            return None
        self.vertice_col()
        self.vertices.append(v)
        self.vertice_row()

    def add_edge(self,src:int,dest:int):
        if src not in self.vertices or dest not in self.vertices:
            print('-------Either Source or destination vertices are not in graph---------')
            return None
        self.graph[src][dest]=1
        self.graph[dest][src]=1

    def print_vertices(self):
        for i in self.vertices:
            print('vertice--->>>',i)

    def print_edges(self):
        print('Edges--->>>',self.graph)


g=GraphByAdjMatrix()
g.add_vertices(0)
g.add_vertices(1)
g.add_vertices(2)

g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(28, 0)

g.print_vertices()
g.print_edges()

g.add_vertices(3)
g.add_vertices(4)
g.add_vertices(5)
g.add_vertices(6)

g.add_edge(6, 2)
g.add_edge(5, 3)
g.print_vertices()
g.print_edges()




class GraphByAdjList:

    '''
        Graph implementing by Adjacency List method.
    '''

    def __init__(self):
        self.graph = dict()

    def add_vertices(self,v:int):
        if v in self.graph:
            print('---------- Vertice already exist in the graph------------')
            return None
            
        self.graph.update({
            v:[],
        })

    def add_edge(self,src:int,dest:int):
        if src not in self.graph or dest not in self.graph:
            print('-------Either Source or destination vertices are not in graph---------')
            return None

        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def print_edges(self):
        print('----EDGES-------',self.graph)

    def print_vertices(self):
        for vertice in self.graph.keys():
            print('-------Vertices  >>>>>>',vertice)




print('=====================================================')
g=GraphByAdjList()
g.add_vertices(0)
g.add_vertices(1)
g.add_vertices(2)

g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(28, 0)

g.print_vertices()
g.print_edges()

g.add_vertices(3)
g.add_vertices(4)
g.add_vertices(5)
g.add_vertices(6)

g.add_edge(6, 2)
g.add_edge(5, 3)
g.print_vertices()
g.print_edges()