
# Python program to count all possible paths between two vertices
# from https://www.geeksforgeeks.org/count-possible-paths-two-vertices/
from collections import defaultdict

class Graph:
    def __init__(self, v):
        self.adj = [[] for i in range(v)]
        self.v = v

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def count_all_paths(self, x, y):
        v = self.v
        visited = [False] * v
        # an array of lists of edges per level
        nodes_per_level = defaultdict(list)
        # all the paths found
        paths = []
        # the current path
        path = []
        current_level = 0
        nodes_per_level[current_level].append(x)
        while current_level > 0:
            # How to detect when we are finishing with the children of a node?
            if len(nodes_per_level[current_level]) > 0:
                current = nodes_per_level[current_level].pop()
                if current == y:
                    paths.append(path.copy())
                elif not visited[current]:
                    path.append(current)
                    visited[current] = True
                    for node in self.adj[current]:
                        if not visited[node]:
                            q.append(node)
            else:
                current_level -= 1
        pass

if __name__ == '__main__':
    n = int(input())
    g = Graph(n)
    x, y = map(int, input().split(' '))
    e = int(input())
    while e > 0:
        u, v = map(int, input().split(' '))
        g.add_edge(u, v)
        e -= 1
    paths = g.count_all_paths(x, y)
    print(paths)
