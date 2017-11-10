# -*- coding: utf-8 -*-
# @Time    : 2017-11-3 15:18
# @Author  : zhangqi
# @File    : Question_GraphTraversal.py
# @Software: PyCharm Community Edition

def createGraphList():
	a, b, c, d, e, f, g, h = range(8)
	N = [
		[b, c, d, e, f],  # a
		[c, e],  # b
		[d],  # c
		[e],  # d
		[f],  # e
		[c, g, h],  # f
		[f, h],  # g
		[f, g]  # h
	]
	return N


# Walking Through a Connected Component of a Graph Represented Using Adjacency Sets
def walk(G, s, S=set()):  # Walk the graph from node s
	P, Q = dict(), set()  # Predecessors + "to do" queue
	P[s] = None  # s has no predecessor
	Q.add(s)  # We plan on starting with s
	while Q:  # Still nodes to visit
		u = Q.pop()  # Pick one, arbitrarily
		for v in G[u].difference(P, S):  # New nodes?
			Q.add(v)  # We plan to visit them!
			P[v] = u  # Remember where we came from
	return P


if __name__ == '__main__':
	aGraphList = createGraphList()
	aGraph = aGraphList
	print(aGraphList)
	# turn graph list into graph with set
	for i in range(len(aGraphList)):
		aGraph[i] = (set(aGraphList[i]))
		
	print ("-"*80)
	print (aGraph)
	print (list(walk(aGraph, 0)))  # [0, 1, 2, 3, 4, 5, 6, 7]
