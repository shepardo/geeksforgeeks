// C# program to print count of nodes
// at given level.
// from https://www.geeksforgeeks.org/count-number-nodes-given-level-using-bfs/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

// This class represents
// a directed graph
// using adjacency
// list representation
class Graph {

    // No. of vertices
    private int _V;

    LinkedList<int>[] _adj;

    public Graph(int V)
    {
    	_adj = new LinkedList<int>[V];

    	for(int i = 0; i < _adj.Length; i++)
    	{
    		_adj[i] = new LinkedList<int>();
    	}
    	_V = V;
    }

    public void AddEdge(int v, int w)
    {

    	// Add w to v’s list.
    	_adj[v].AddLast(w);
    }

    public int BreadthFirstSearch(int s,int l)
    {

    	// Mark all the vertices
    	// as not visited
    	bool[] visited = new bool[_V];
    	int[] level = new int[_V];

    	for(int i = 0; i < _V; i++)
    	{
    		visited[i] = false;
    		level[i] = 0;
    	}

    	// Create a queue for BFS
    	LinkedList<int> queue = new LinkedList<int>();

    	// Mark the current node as
    	// visited and enqueue it
    	visited[s] = true;
    	level[s] = 0;
    	queue.AddLast(s);

    	while(queue.Any())
    	{

    		// Dequeue a vertex from
    		// queue and print it
    		s = queue.First();

    		// Console.Write( s + " " );
    		queue.RemoveFirst();

    		LinkedList<int> list = _adj[s];

    		foreach(var val in list)
    		{
    			if (!visited[val])
    			{
    				visited[val] = true;
    				level[val] = level[s] + 1;
    				queue.AddLast(val);
    			}
    		}
    	}

    	int count = 0;
    	for(int i = 0; i < _V; i++)
    		if (level[i] == l)
    			count++;

    	return count;
    }
}

// Driver code
class GFG {

    static void Main(string[] args)
    {

    	// Create a graph given
    	// in the above diagram
    	Graph g = new Graph(6);

    	g.AddEdge(0, 1);
    	g.AddEdge(0, 2);
    	g.AddEdge(1, 3);
    	g.AddEdge(2, 4);
    	g.AddEdge(2, 5);

    	int level = 2;

    	Console.WriteLine(g.BreadthFirstSearch(0, level));
    }
}

// This code is contributed by anvudemy1
