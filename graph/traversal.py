from graph_adjacency import GraphByAdjList


class GraphByAdjList(GraphByAdjList):

    def __init__(self):
        self.bfs_visited_vertices = list()
        self.dfs_visited_vertices = list()
        self.queue = list()
        self.stack = list()
        super().__init__()

    def BfsTraversal(self, startNode: int):
        '''
            Breadth-first search traversal.
        '''
        self.bfs_visited_vertices = [False for vertice in self.graph.keys()]
        self.bfs_visited_vertices[startNode] = True
        self.queue.append(startNode)
        print('-------BFS Traversal------')
        while self.queue:
            ele = self.queue.pop(0)
            print(ele, end='-->')
            for adj in self.graph[ele]:
                if not self.bfs_visited_vertices[adj[0]]:
                    self.queue.append(adj[0])
                    self.bfs_visited_vertices[adj[0]] = True
        print()

    def DfsTraversal(self, startNode: int):
        '''
            Depth-first search traversal.
        '''
        self.dfs_visited_vertices = [False for vertice in self.graph.keys()]
        self.dfs_visited_vertices[startNode] = True
        self.stack.append(startNode)
        print('---------DFS Traversal--------')
        while self.stack:
            ele = self.stack.pop()
            print(ele, end=' ---> ')
            for adj in self.graph[ele]:
                if not self.dfs_visited_vertices[adj[0]]:
                    self.stack.append(adj[0])
                    self.dfs_visited_vertices[adj[0]] = True
        print()


if __name__ == '__main__':
    g = GraphByAdjList()
    g.add_vertices(0)
    g.add_vertices(1)
    g.add_vertices(2)

    g.add_edge(1, 2, weight=6)
    g.add_edge(2, 0, weight=5)

    g.BfsTraversal(0)
    g.DfsTraversal(0)

    g.add_vertices(3)
    g.add_vertices(4)
    g.add_vertices(5)
    g.add_vertices(6)

    g.add_edge(6, 2, weight=1)
    g.add_edge(5, 3, weight=3)
    g.add_edge(3, 6, weight=7)
    g.add_edge(4, 0, weight=8)

    g.BfsTraversal(0)
    g.DfsTraversal(0)
