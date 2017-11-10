#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/2 22:35
# @Author  : zhangqi
# @Site    : 
# @File    : Question_Graph_BFS.py
# @Software: PyCharm Community Edition

import matplotlib.pyplot as plt
import networkx as nx
from networkx.classes.graph import Graph
from Class_Graph import Graph, Vertex
from queue import Queue



def dfs(g, v):
	"""
	姥姥的伪代码
	void  DFS( Graph G,  int V )
	{ /* 从第V个顶点出发递归地深度优先遍历图G */
	VertexType W;
		Visited[V] = TRUE;
		VisitFunc(V);      /* 访问第V个顶点 */
		for( W = FirstAdjV(G, V);  W;  W = NextAdjV (G, V, W) )
			if( !Visited[W] )
				DFS(G, W); /* 对V的尚未访问的邻接顶点W递归调用DFS */
}
	:param g: a instance of graph
	:param start: a instance vertex, such as g.getVertex('FOOL')
	:return:
	"""
	currentVert = v
	# the fist step set 0
	if currentVert.pred is None:
		currentVert.setDistance(0)
		currentVert.setPred(None)

	if currentVert.getColor() == 'black':
		return

	if currentVert.getColor() == 'white':
		currentVert.setColor('gray')

	for nbr in currentVert.getConnections():
		if nbr.getColor() == 'white':
			nbr.setColor('gray')
			nbr.setDistance(currentVert.getDistance() + 1)
			nbr.setPred(currentVert)
			dfs(g, nbr)

	currentVert.setColor('black')


def bfs(g, start):
	"""
	广度优先搜索算法使用我们先前开发的邻接表表示。此外，它使用一个 Queue，一个关键的地方，决定下一个探索的顶点
	BFS 从起始顶点开始，颜色从灰色开始，表明它正在被探索。另外两个值，即距离和前导，
	对于起始顶点分别初始化为 0 和 None 。最后，放到一个队列中
	:param g: a instance of graph
	:param start: a instance vertex, such as g.getVertex('FOOL')
	:return:
	"""
	start.setDistance(0)
	start.setPred(None)
	vertQueue = Queue()
	vertQueue.enqueue(start)
	while vertQueue.size() > 0:
		currentVert = vertQueue.dequeue()
		for nbr in currentVert.getConnections():
			if nbr.getColor() == 'white':
				nbr.setColor('gray')
				nbr.setDistance(currentVert.getDistance() + 1)
				nbr.setPred(currentVert)
				vertQueue.enqueue(nbr)

			currentVert.setColor('black')


def buildGraph(wordFile):
	d = {}
	g = Graph()
	wfile = file(wordFile, 'r')
	# create buckets of words that differ by one letter
	for line in wfile:
		word = line[:-1]
		for i in range(len(word)):
			bucket = word[:i] + '_' + word[i + 1:]
			if bucket in d:
				d[bucket].append(word)
			else:
				d[bucket] = [word]
	# add vertices and edges for words in the same bucket
	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2:
					g.addEdge(word1, word2)

	return g


def traverse(y):
	"""
	展示了如何按前导链接打印出字梯
	:param y: a instance of vertex , such as g.getVertex('FOOL')
	:return:
	"""
	x = y
	while x.getPred():
		print(x.getId())
		x = x.getPred()
	print(x.getId())



def draw2(myGraph):
	G = nx.Graph()                 #建立一个空的无向图G
	for node in myGraph.vertexList:
		G.add_node(str(node))
	for edge in myGraph.edgesList:
		G.add_edge(str(edge[0]), str(edge[1]))

	print( "nodes:", G.nodes())      #输出全部的节点： [1, 2, 3]
	print( "edges:", G.edges())      #输出全部的边：[(2, 3)]
	print("number of edges:", G.number_of_edges())   #输出边的数量：1
	nx.draw(G, with_labels=True)
	plt.savefig("wuxiangtu.png")
	plt.show()

def draw3(myGraph):
	G = nx.DiGraph()                 #建立一个空的无向图G
	for node in myGraph.vertexList:
		G.add_node(str(node))
	for edge in myGraph.edgesList:
		G.add_edge(str(edge[0]), str(edge[1]))

	print( "nodes:", G.nodes())      #输出全部的节点： [1, 2, 3]
	print( "edges:", G.edges())      #输出全部的边：[(2, 3)]
	print("number of edges:", G.number_of_edges())   #输出边的数量：1
	nx.draw(G, with_labels=True)
	plt.savefig("wuxiangtu.png")
	plt.show()


if __name__ == '__main__':
	g = Graph()

	g = buildGraph('e:\\fourletterwords2.txt')
	# bfs(g, g.getVertex('BOSS'))
	# dfs(g, g.getVertex('BOSS'))
	# traverse(g.getVertex('SAGE'))

	# g.addEdge(0, 1, 5)
	# g.addEdge(0, 5, 2)
	# g.addEdge(1, 2, 4)
	# g.addEdge(2, 3, 9)
	# g.addEdge(3, 4, 7)
	# g.addEdge(3, 5, 3)
	# g.addEdge(4, 0, 1)
	# g.addEdge(5, 4, 8)
	# g.addEdge(5, 2, 1)

	draw2(g)
	# bfs(g, g.getVertex(2))

	# traverse(g.getVertex(1))
	# print('-'*80)
	# dfs(g, g.getVertex(2))
	# traverse(g.getVertex(1))