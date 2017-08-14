""" Check for node connectedness.
"""

import graphfromlinks as G



if __name__ == '__main__':

	g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
		}


	graph = G.Graph(g)

	degrees = graph.get_degree()
	connected = True

	for k,v in degrees.items():
			if v == 0:
				connected = False


	if not connected:
		print('Not all nodes connected')
	else:
		print('All nodes connected')

