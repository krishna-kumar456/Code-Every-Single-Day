""" Output eulerian path.
"""

import graphfromlinks as G


if __name__ == "__main__":

	g = { 	  "a" : ["d"],
		      "b" : ["c"],
		      "c" : ["b", "c", "d", "e"],
		      "d" : ["a", "c"],
		      "e" : ["c"],
		      "f" : []
        }

	graph = G.Graph(g)

	vertex_graph = graph.get_degree()

	count_of_even_vertices = 0
	count_of_odd_vertices = 0

	for k, v in vertex_graph.items():

		if v % 2 == 0:
			count_of_even_vertices += 1

		if v % 2 == 1:
			count_of_odd_vertices += 1


	if count_of_even_vertices == len(vertex_graph.keys()):
		print('Euler cycle and path found in Graph')

	else:
		print('No Euler cycle found in Graph')

	if count_of_odd_vertices == 2 and count_of_even_vertices == len(vertex_graph.keys()) - 2:
		print('Euler path found in Graph')
	else:
		print('No Euler path found in Graph')











