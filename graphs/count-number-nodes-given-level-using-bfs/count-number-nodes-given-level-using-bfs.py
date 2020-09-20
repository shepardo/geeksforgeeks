# BFS for counting all the vertexes in a level
# from https://www.geeksforgeeks.org/count-number-nodes-given-level-using-bfs/

class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(v)]

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def count_per_level(self, level, starter):
        visited = [False for i in range(self.v)]
        levels = [-1] * self.v
        levels[starter] = 0
        queue = []
        queue.append(starter)
        while len(queue) > 0:
            x = queue.pop(0)
            visited[x] = True
            for node in self.adj[x]:
                if not visited[node]:
                    if levels[node] == -1:
                        levels[node] = levels[x] + 1
                    queue.append(node)
        lvl_cnt = 0
        for i in range(self.v):
            if levels[i] == level:
                lvl_cnt += 1
        return lvl_cnt

if __name__ == '__main__':
    n = int(input())
    level = int(input())
    g = Graph(n)
    while True:
        line = ''
        try:
            line = input()
        except EOFError:
            break
        u, v = map(int, line.split(' '))
        g.add_edge(u, v)
    cnt = g.count_per_level(level, 0)
    print(cnt)
