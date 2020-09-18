// An Iterative C# program to do DFS traversal from 
// a given source vertex. DFS(int s) traverses vertices
// reachable from s.
using System;
using System.Collections.Generic;

class GFG
{
	// This class represents a directed graph using adjacency
	// list representation
	public class Graph
	{
		public int V; // Number of Vertices

		public LinkedList<int>[] adj; // adjacency lists

		// Constructor
		public Graph(int V)
		{
			this.V = V;
			adj = new LinkedList<int>[V];

			for (int i = 0; i < adj.Length; i++)
				adj[i] = new LinkedList<int>();

		}

		// To add an edge to graph
		public void addEdge(int v, int w)
		{
			adj[v].AddLast(w); // Add w to v’s list.
		}

		// prints all not yet visited vertices reachable from s
		public void DFS(int s)
		{
			// Initially mark all vertices as not visited
			Boolean []visited = new Boolean[V];

			// Create a stack for DFS
			Stack<int> stack = new Stack<int>();

			// Push the current source node
			stack.Push(s);

			while(stack.Count > 0)
			{
				// Pop a vertex from stack and print it
				s = stack.Peek();
				stack.Pop();

				// Stack may contain same vertex twice. So
				// we need to print the popped item only
				// if it is not visited.
				if(visited[s] == false)
				{
					Console.Write(s + " ");
					visited[s] = true;
				}

				// Get all adjacent vertices of the popped vertex s
				// If a adjacent has not been visited, then push it
				// to the stack.
				foreach(int v in adj[s])
				{
					if(!visited[v])
						stack.Push(v);
				}

			}
		}
	}

	// Driver code
	public static void Main(String []args)
	{
		// Total 5 vertices in graph
		Graph g = new Graph(5);

		g.addEdge(1, 0);
		g.addEdge(0, 2);
		g.addEdge(2, 1);
		g.addEdge(0, 3);
		g.addEdge(1, 4);

		Console.Write("Following is the Depth First Traversal\n");
		g.DFS(0);
	}
}

// This code is contributed by Arnasb Kundu
