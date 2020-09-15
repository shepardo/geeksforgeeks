class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = [[0 for j in range(v)] for i in range(v)]
        self.degrees = [0 for j in range(v)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        # calculate degrees
        self.degrees[u] += 1

    def prune_vertices_below_k(self, k):
        # prune the nodes that have a degree less than k.
        v = self.v
        vertices_pruned = True
        while vertices_pruned:
            vertices_pruned = False
            for i in range(v):
                if self.degrees[i] < k and self.degrees[k] != 0:
                    for j in range(v):
                        vertices_pruned = True
                        self.graph[i][j] = 0
                        self.degrees[j] -= 1
                        self.degrees[i] -= 1
        return

    def print_graph(self):
        v = self.v
        for i in range(v):
            print()
            for j in range(v):
                print('{0} '.format(self.graph[i][j]), end='')
        print()

if __name__ == '__main__':
    v = int(input())
    e = int(input())
    k = int(input())
    g = Graph(v)
    while e > 0:
        u, v = map(int, input().split(' '))
        g.add_edge(u, v)
        # finding k-core implies non-directional edges
        g.add_edge(v, u)
        e -= 1
    g.prune_vertices_below_k(k)
    g.print_graph()
