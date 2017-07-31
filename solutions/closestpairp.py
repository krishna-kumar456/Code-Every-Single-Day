"""
Closest Pair Problem.

Brute-Force Algorithm:
1. Find distances between adjacent points
2. If distance is minimum, update minimum distance

Planar Case Algorithm:
1.Sort points according to their x-coordinates.
2.Split the set of points into two equal-sized subsets by a vertical line x=xmid.
3.Solve the problem recursively in the left and right subsets. This yields the
left-side and right-side minimum distances dLmin and dRmin, respectively.
4.Find the minimal distance dLRmin among the set of pairs of points in which one
point lies on the left of the dividing vertical and the other point lies to the right.
5.The final answer is the minimum among dLmin, dRmin, and dLRmin.
"""

import math

INF = 9999999

metricSpace = [[1,2],[3,4],[1,5],[2,6],[6,3],[4,7],[6,4],[2,9],[5,5],[7,4]]

def distance_between_2p(x1, y1, x2, y2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def brute_force():
	minDist = INF
	closestPair = []

	for i in range(len(metricSpace)-1):
		print(i)
		for j in range(i+1, len(metricSpace)):
			print(j)
			p = metricSpace[i]
			print(p)
			q = metricSpace[j]
			print(q)
			if distance_between_2p(p[0], p[1], q[0], q[1]) < minDist:
				minDist = distance_between_2p(p[0], p[1], q[0], q[1])
				closestPair = [p,q]

	return closestPair


print(brute_force())




