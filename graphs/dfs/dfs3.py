
# This implementation uses a adjecency matrix

'''
Typical input
4
6
1
0 1
0 2
1 2
2 0
2 3
3 3

'''

from array import *

class Graph():
  def __init__(self, n):
    self.n = n
    self.nodes = []
    for i in range(n):
      self.nodes.insert(0, [])

  def addEdge(self, a, b):
    self.nodes[a].append(b)
    self.nodes[b].append(a)

  # Implements depth first search (travel)
  def do_dfs_from(self, start_node, visit_callback):
    n = self.n
    visited = [0] * n
    q = []
    q.append(start_node)
    while len(q) > 0:
      x = q.pop()
      if visited[x] == 0:
        visit_callback(x)
      visited[x] = 1
      # travel "children" and add it to list to visit
      for i in reversed(self.nodes[x]):
        if visited[i] == 0:
          q.append(i)

  def dump(self):
    n = self.n
    for i in range(n):
        for j in self.nodes[i]:
            print('{0} '.format(j), end='')
        print()

def visit(x):
  print('visited {0}'.format(x))

# main
if __name__ == '__main__':
  n = int(input())
  e = int(input())
  start_node = int(input())
  g = Graph(n)
  while e > 0:
    line = input()
    data = line.split(' ')
    g.addEdge(int(data[0]), int(data[1]))
    e -= 1
  g.dump()
  print('***')
  g.do_dfs_from(start_node, visit)
