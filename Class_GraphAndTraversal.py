# -*- coding: utf-8 -*-
# @Time    : 2017-11-3 16:51
# @Author  : zhangqi
# @File    : Class_GraphAndTraversal.py
# @Software: PyCharm Community Edition

import matplotlib.pyplot as plt
from graphviz import Digraph
import networkx as nx
from networkx.classes.graph import Graph


class GraphTable:
	def __init__(self, nodes, edges, is_dir=False):
		self.nodes = nodes
		self.edges = edges
		self.is_dir = is_dir
		self.graph = []
		for node in nodes:
			self.graph.append([node])
		for edge in edges:
			for n in self.graph:
				if n[0] == edge[0]:
					n.append(edge[1])
				if not is_dir:
					if n[0] == edge[1]:
						n.append(edge[0])
		self.G = None

	# def __str__(self):
	# 	return 'n'.join([str(n) for n in self.graph])

	def draw(self):
		settings = dict(name='Graph', engine='circo', node_attr=dict(shape='circle'), format='png')
		self.G = nx.Digraph(**settings) if self.is_dir else Graph(**settings)

		if self.is_dir:
			self.G = nx.Digraph(**settings)
		else:
			self.G = Graph(**settings)

		for node in self.nodes:
			self.G.node(str(node), str(node))
		for edge in self.edges:
			self.G.edge(str(edge[0]), str(edge[1]))
		return self.G

	# Non direction graph
	def draw2(self):
		self.G = nx.Graph()                 #建立一个空的无向图G
		for node in self.nodes:
			self.G.add_node(str(node))
		for edge in self.edges:
			self.G.add_edge(str(edge[0]), str(edge[1]))

		print( "nodes:", self.G.nodes())      #输出全部的节点： [1, 2, 3]
		print( "edges:", self.G.edges())      #输出全部的边：[(2, 3)]
		print("number of edges:", self.G.number_of_edges())   #输出边的数量：1
		nx.draw(self.G, with_labels=True)
		plt.savefig("wuxiangtu.png")
		plt.show()

	def draw3(self):
		settings = dict(name='Graph', engine='circo', node_attr=dict(shape='circle'), format='png')
		self.G = nx.DiGraph()                 #建立一个空的无向图G
		for node in self.nodes:
			self.G.add_node(str(node))
		for edge in self.edges:
			self.G.add_edge(str(edge[0]), str(edge[1]))

		print( "nodes:", self.G.nodes())      #输出全部的节点： [1, 2, 3]
		print( "edges:", self.G.edges())      #输出全部的边：[(2, 3)]
		print("number of edges:", self.G.number_of_edges())   #输出边的数量：1
		nx.draw(self.G)
		plt.savefig("wuxiangtu.png")
		plt.show()

	def draw4(self):
		self.G = nx.DiGraph()
		self.G.add_node(1)
		self.G.add_node(2)  # 加点
		self.G.add_nodes_from([3, 4, 5, 6])  # 加点集合
		self.G.add_cycle([1, 2, 3, 4])  # 加环
		self.G.add_edge(1, 3)
		self.G.add_edges_from([(3, 5), (3, 6), (6, 7)])  # 加边集合
		nx.draw(self.G)
		plt.savefig("youxiangtu.png")
		plt.show()

if __name__ == '__main__':
	gt = GraphTable([1, 2, 3, 4, 5], [(1, 2), (1, 5), (2, 5), (2, 4), (5, 4), (2, 3), (3, 4)])
	print(gt)
	gt.draw2()
	# gt.draw3()
	# gt.draw4()

	"""
	[1, 2, 5]
	[2, 1, 5, 4, 3]
	[3, 2, 4]
	[4, 2, 5, 3]
	[5, 1, 2, 4]
	"""
