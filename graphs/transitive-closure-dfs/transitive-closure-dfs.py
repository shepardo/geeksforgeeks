
# from https://www.geeksforgeeks.org/transitive-closure-of-a-graph-using-dfs/
# Transitive closure using DFS
# This solution is O( V(E+2V) ), which proportional to V ** 2, unless the E >> V,
#  then it is probably better the Floyd-Warshall algorithm which is O(V ** 3).

class Graph():
    def __init__(self, v):
        self.v = v
        self.nodes = []
        self.tc = []
        for i in range(v):
            self.nodes.insert(0, [0] * v)
            self.tc.insert(0, [0] * v)

    def add_edge(self, u, v):
        self.nodes[u][v] = 1

    def print_transitive_closure(self):
        for i in range(self.v):
            print()
            for j in range(self.v):
                print('{0} '.format(self.tc[i][j]), end='')
        print()

    def solve_transitive_closure(self):
        v = self.v
        while v > 0:
            visited = [0] * self.v
            q = []
            q.append(self.v - v)
            while len(q) > 0:
                x = q.pop(0)
                visited[x] = 1
                for i in range(self.v):
                    if self.nodes[x][i] == 1 and visited[i] == 0:
                        q.append(i)
            for i in range(self.v):
                self.tc[self.v - v][i] = visited[i]
            v -= 1

if __name__ == "__main__":
    v = int(input())
    e = int(input())
    g = Graph(v)
    while e > 0:
        line = input()
        u, v = map(int, line.split(' '))
        g.add_edge(u, v)
        e -= 1
    g.solve_transitive_closure()
    g.print_transitive_closure()
