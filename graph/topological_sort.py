from graph_adjacency import GraphByAdjList

class GraphByAdjList(GraphByAdjList):
    '''
        Implement the Topological Sort in graph by Modified DFS approach.
    '''

    def __init__(self):
        super().__init__()
        self.visited = list()
        self.stack = list()

        # Variables Used for Khan's Algorithm
        self.in_degree = list()
        self.queue = list()
        self.result = list()


    def topo_recursive(self,v:int):
        self.visited[v]=True
        for adj in self.graph[v]:
            if self.visited[adj[0]]==False:
               self.topo_recursive(adj[0])
        self.stack.append(v)


    def topological_sort(self):
        self.visited = [False for vertice in self.graph.keys()]
        
        for v in self.graph:
            if self.visited[v]==False:
                self.topo_recursive(v)


    def print_order(self):
        print('<-------',self.stack[::-1],'--------->')


    def find_indegree(self):
        self.in_degree = [0 for vertice in self.graph.keys()]
        for vertice in self.graph:
            for v,w in self.graph[vertice]:
                self.in_degree[v]+=1


    def khans_algorithm(self):
        '''
            Implement the Khan's Algorithm.
            step 1: Find the indegree of all the verices.
            step 2: Find the vertices whose indegree is 0.
            step 3: Add all those vertices in queue.
            step 4: now decrement indegree of all adjacent vertices by 1 of popped element.
            step 5: Do step 4 until queue is not empty.
            step 6: Check if result==no.of vertices,else there must be a cycle so not able to find the topological sort.
        '''
        self.find_indegree()
        
        for v in self.graph:
            if self.in_degree[v]==0:
                self.queue.append(v)
        
        
        while self.queue:
            ele = self.queue.pop(0)
            self.result.append(ele)
            
            for v,w in self.graph[ele]:
            
                self.in_degree[v]-=1
                if self.in_degree[v]==0:
                    self.queue.append(v)

        if len(self.result)!=len(self.graph):
            print('Topological Order cannot be found ,may be graph contain cycle')
        else:
            print('<-------',self.result,'--------->')




if __name__ == '__main__':
    '''
        Must condition for the topological sort.
            1. Graph must be Directed Acyclic graph.
            2. At least one vertex with indegree 0.
    '''

    g = GraphByAdjList()

    g.add_vertices(0)
    g.add_vertices(1)
    g.add_vertices(2)
    g.add_vertices(3)
    g.add_vertices(4)
    g.add_vertices(5)
    
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    


    g.topological_sort()
    g.print_order()

    g.khans_algorithm()