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












if __name__ == '__main__':