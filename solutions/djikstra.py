""" Djikstra's Algorithm
	
	1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty.
	2) Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first.
	3) While sptSet doesn’t include all vertices
	  a) Pick a vertex u which is not there in sptSetand has minimum distance value.
	  b) Include u to sptSet.
	  c) Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex v, if sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v.
"""

import sys

class Graph():

	def __init__(self, vertices):
		""" Constructor for Graph class, consumes count 
			of vertices and initializes a matrix repres-
			entation of the n*n graph.
		"""
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					  for row in range(vertices)]


	def printSolution(self, dist):
		""" Display function to print the distance of a
			vertex from the source vertex.
		"""
		print("Vertex tDistance from Source")
		for node in range(self.V):
			print(node, dist[node])


	def minDistance(self, dist, sptSet):
		""" Utility function to find the minimum distace
			vertex in the remaining vertices not in sptSet.
		"""
		minimum = sys.maxint

		for v in range(self.V):
			if dist[v] < minimum and sptSet[v] == False:
				minimum = dist[v]
				min_index = v

		return min_index

	def dijkstra(self, src):
		""" First select the source vertex, insert it into
			the sptSet. Then loop across the vertices, and
			compare the distances and non existence in 
			sptSet. Followed by addition of distances.
		"""

		dist = [sys.maxint] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			u = self.minDistance(dist, sptSet)

			sptSet[u] = True

			for v in range(self.V):
				if self.graph[u][v] > 0 and sptSet[v] == False
					and dist[v] > dist[u] + self.graph[u][v]:
					dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist)

 



if __name__ == '__main__':

	g  = Graph(9)
	g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
	           [4, 0, 8, 0, 0, 0, 0, 11, 0],
	           [0, 8, 0, 7, 0, 4, 0, 0, 2],
	           [0, 0, 7, 0, 9, 14, 0, 0, 0],
	           [0, 0, 0, 9, 0, 10, 0, 0, 0],
	           [0, 0, 4, 14, 10, 0, 2, 0, 0],
	           [0, 0, 0, 0, 0, 2, 0, 1, 6],
	           [8, 11, 0, 0, 0, 0, 1, 0, 7],
	           [0, 0, 2, 0, 0, 0, 6, 7, 0]
	          ];
	 
	g.dijkstra(0);
