from graph_adjacency import GraphByAdjList
import sys


class GraphByAdjList(GraphByAdjList):

    def getMinimumDistance(self,distance, sptSet):
        '''
            Get the minimum distance element.
        '''
        min = sys.maxsize
        index = 0
        for i, v in enumerate(distance):
            if v < min and sptSet[i]==False:
                min = v
                index = i
        return index

    def print_distance(self,distance):
        '''
            Print the distance of the each vertice from the Source Vertice.
        '''
        for index, value in enumerate(distance):
            print(index, value, sep='<-------->')

    def shortest_path(self, source=0):
        '''
            Find the Shortest path from the source vertice to all vertice in a graph.
        '''
        graphSize = len(self.graph)
        distance = [sys.maxsize]*graphSize
        sptSet = [False]*graphSize
        distance[source] = 0
        print('******************** SHORTEST PATH IS **************************')
        for sp in range(graphSize):
            minEle = self.getMinimumDistance(distance, sptSet)

            sptSet[minEle] =True
            for adj in self.graph[minEle]:
                if distance[minEle] + adj[1] < distance[adj[0]]:
                    distance[adj[0]] = distance[minEle] + adj[1]

        self.print_distance(distance)


if __name__ == '__main__':

    g = GraphByAdjList()

    g.add_vertices(0)
    g.add_vertices(1)
    g.add_vertices(2)
    g.add_vertices(3)
    g.add_vertices(4)
    g.add_vertices(5)
    g.add_vertices(6)
    g.add_vertices(7)
    g.add_vertices(8)

    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)

    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)

    g.add_edge(2, 3, 7)
    g.add_edge(2, 5, 4)
    g.add_edge(2, 8, 2)

    g.add_edge(3, 2, 7)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)

    g.add_edge(4, 3, 9)
    g.add_edge(4, 5, 10)

    g.add_edge(5, 2, 4)
    g.add_edge(5, 3, 14)
    g.add_edge(5, 4, 10)
    g.add_edge(5, 6, 2)

    g.add_edge(6, 5, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)

    g.add_edge(7, 0, 8)
    g.add_edge(7, 1, 11)
    g.add_edge(7, 6, 1)
    g.add_edge(7, 8, 7)

    g.add_edge(8, 2, 2)
    g.add_edge(8, 6, 6)
    g.add_edge(8, 7, 7)

    g.print_vertices()
    g.print_edges()
    g.shortest_path(0)
