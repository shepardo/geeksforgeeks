# DFS iterative using adjacency list
# from https://www.geeksforgeeks.org/iterative-depth-first-traversal/

class Graph:
    def __init__(self, v):
        self.graph = [[] for i in range(v)]
        self.v = v

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, cb):
        for i in range(self.v):
            if not visited[i]:
                self.do_dfs_one(i, visited, cb)

    def dfs_one(self, start, cb):
        visited = [False] * self.v
        self.do_dfs_one(start, visited, cb)

    def do_dfs_one(self, start, visited, cb):
        stack = []
        stack.append(start)
        while len(stack) > 0:
            current = stack.pop()
            if not visited[current]:
                cb(current)
                visited[current] = True
            for i in reversed(self.graph[current]):
                if not visited[i]:
                    stack.append(i)

def mycallback(v):
    print('{0} '.format(v), end='')

if __name__ == '__main__':
    v = int(input())
    e = int(input())
    starter = int(input())
    g = Graph(v)
    while e > 0:
        u, w = map(int, input().split(' '))
        g.add_edge(u, w)
        e -= 1
    #g.dfs(mycallback)
    g.dfs_one(starter, mycallback)
    print()
