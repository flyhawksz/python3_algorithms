# -*- coding: utf-8 -*-
# @Time    : 2017-9-27 14:24
# @Author  : zhangqi
# @File    : Class_BinaryTree.py
# @Software: PyCharm Community Edition


class BinaryTree:
	"""
	BinaryTree(self, binaryTreeObj)
	isEmpty(self)
	num_nodes(self)
	getData(self)
	getLeftChild()
	getRightChild()
	setLeftChild(self, btree)
	setRightChild(self, btree)
	traversal(self)   # 遍历二叉树节点迭代器
	forall()
	"""
	
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.leftChild is None:
			self.leftChild = BinaryTree(newNode)
		else:
			tmp = BinaryTree(newNode)
			tmp.leftChild = self.leftChild
			self.leftChild = tmp
	
	def insertRight(self, newNode):
		if self.rightChild is None:
			self.rightChild = BinaryTree(newNode)
		else:
			tmp = BinaryTree(newNode)
			tmp.rightChild = self.rightChild
			self.rightChild = tmp

	def isEmpty(self):
		return self.key is None
	
	def setRootValue(self,obj):
		self.key = obj

	def getRootValue(self):
		return self.key

	def getLeftChild(self):
		return self.leftChild
	
	def getRightChild(self):
		return self.rightChild
	
	def traversal(self):   # 遍历二叉树节点迭代器
		pass
	
	def createBinaryTreeInPreorder(self):  # 创建二叉树，遵循前序遍历方式输入
		pass
	
	
if __name__ == '__main__':

	# 1 creat a tree with insert method
	tree = BinaryTree('a')
	tree.insertLeft('b')
	tree.insertRight('c')
	tree.getLeftChild().insertRight('d')
	tree.getRightChild().insertLeft('e')
	tree.getRightChild().insertRight('f')

	tree.getRightChild().getRightChild().insertRight('g')

	print(tree.getRightChild().getRightChild().getRightChild().getRootValue())

