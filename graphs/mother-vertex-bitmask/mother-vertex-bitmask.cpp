// C++ code to find Mother
// Vertex using Bitmask
// from https://www.geeksforgeeks.org/find-a-mother-vertex-in-a-graph-using-bit-masking/?ref=rp

//#include <bits/stdc++.h>
#include <iostream>
#include <set>
#include <cmath>

using namespace std;

struct Graph {
	int V;

	// Store in descending order
	set<int, greater<int> >* adjList;
};

Graph* CreateGraph(int N)
{
	Graph* g = new Graph();
	g->V = N;
	g->adjList
		= new set<int, greater<int> >[N];
	return g;
}

void AddEdge(
	Graph* g, int src, int dest)
{

	g->adjList[src].insert(dest);
}

void PrintGraph(Graph* g)
{

	set<int, greater<int> >::iterator it;

	for (int i = 0; i < g->V; i++) {

		for (it = g->adjList[i].begin();
			it != g->adjList[i].end();
			it++) {
			cout << "There is an edge from "
				<< i << " to "
				<< *it << endl;
		}
	}
}

bool IsEdge(Graph* g, int src, int dest)
{
	if (g->adjList[src].find(dest)
		!= g->adjList[src].end()) {

		return true;
	}
	return false;
}

int MotherVertexUtil(
	Graph* g, int index,
	int* mask, int* m_vertex)
{

	// If mother vertex is already found
	// then simply return with existing
	// mask of the vertex index
	if (*m_vertex != -1) {

		return mask[index];
	}

	// if this vertex is already visited,
	// return the bit-mask
	// value of this vertex.
	if (mask[index] != 0) {
		return mask[index];
	}

	int tmpmask = 0;

	// Set the bit corresponding
	// to vertex index in tmpmask
	tmpmask |= (1 << index);

	for (int i = 0; i < g->V; i++) {
		if ((index != i)
			&& IsEdge(g, index, i)) {

			// Set bits corresponding to all
			// vertex which can be visite
			// by this vertex by ORing
			// the return value by util function

			// Vertex is not visited
			if (mask[i] == 0) {

				int retmask
					= MotherVertexUtil(
						g, i, mask, m_vertex);
				tmpmask |= retmask;
			}

			// Vertex is already visited
			else {
				tmpmask |= mask[i];
			}

			// Check if current vertex is
			// mother vertex or mother vertex
			// is already found
			if (tmpmask == (pow(2, g->V) - 1)) {

				// If all bits of a mask is set
				// it means current vertex
				// is mother vertex
				if (*m_vertex == -1) {
					*m_vertex = index;
				}
				return tmpmask;
			}
		}
	}

	// populate tmpmask as final
	// bit mask of the vertex
	mask[index] |= tmpmask;

	return mask[index];
}

int MotherVertex(Graph* g)
{

	int v = g->V;
	int* mask = new int(v);

	// Initially bit mask
	// for all vertex will be 0
	for (int i = 0; i < v; i++) {
		mask[i] = 0;
	}

	// DFS traversal is used to check
	// for the mother vertex
	// All set bits (of bitmask of a vertex)
	// represent the current vertex index
	// and index of vertices which could be
	// visited from the current vertex.

	/* Example:
	If a vertex index is 3
	then and vertex 5, 7 and 10
	can be visited from this vertex
	then final bit mask of this vertex
	would be
	00000000000000000000010010101000
	(bits 3, 5, 7 and 10 are set) */

	// tmpmask is used to store
	// the final bitmask of the vertex.
	int tmpmask = 0;

	// flag to check if
	// mother vertex is found
	int m_vertex = -1;

	for (int index = 0; index < v; index++) {

		// set the bit corresponding
		// to vertex index in tmpmask
		tmpmask = (1 << index);

		// mask for a vertex is 0
		// means it has not yet
		// visited so visit this vertex
		if (mask[index] == 0) {

			int retmask
				= MotherVertexUtil(
					g, index,
					mask, &m_vertex);

			// set bits corresponding to all
			// vertices which can be visited
			// from this vertex by ORing
			// the return value by util function
			tmpmask |= retmask;
		}

		// check if current vertex is
		// mother vertex or mother vertex
		// is already found
		// If all bits of a mask is set
		// it means current vertex
		// is mother vertex
		if (tmpmask == (pow(2, v) - 1)) {

			// current vertex is mother vertex
			if (m_vertex == -1) {
				m_vertex = index;
			}
			break;
		}

		// populate tmpmask as final bit
		// mask of the vertex
		mask[index] |= tmpmask;
	}

	return m_vertex;
}

// Driver code
int main()
{

	Graph* g = CreateGraph(7);
	AddEdge(g, 0, 2);
	AddEdge(g, 0, 1);
	AddEdge(g, 1, 3);
	AddEdge(g, 4, 1);
	AddEdge(g, 5, 2);
	AddEdge(g, 5, 6);
	AddEdge(g, 6, 0);
	AddEdge(g, 6, 4);
	PrintGraph(g);

	int m_vertex = MotherVertex(g);
	if (m_vertex == -1) {

		cout << "Mother vertex is not"
			<< " existing in this graph"
			<< endl;
	}
	else {
		cout << "Mother vertex is: "
			<< m_vertex << endl;
	}
	return 0;
}
