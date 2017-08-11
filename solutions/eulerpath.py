""" Output eulerian path.
"""

import graphfromlinks as G


def is_connected(g):
	""" A method to check if the vertices
		of the graph are connected.
	"""
	for k, v in g:
		if len(v) > 0:
			return True






if __name__ == "__main__":

	g = { 	  "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }

	graph = G.Graph(g)





