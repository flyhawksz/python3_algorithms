# -*- coding: utf-8 -*-
# @Time    : 2017-10-31 11:47
# @Author  : zhangqi
# @File    : Class_BinaryHeap.py
# @Software: PyCharm Community Edition

# this heap takes key value pairs, we will assume that the keys are integers
import random
from Class_BinaryTree2 import binaryTree, treeNode


class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def insert(self, newItem):
		self.heapList.append(newItem)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)

	def percUp(self, index):
		while index // 2 > 0:
			if self.heapList[index] < self.heapList[index//2]:
				self.heapList[index] , self.heapList[index // 2] = self.heapList[index//2], self.heapList[index]
				index = index // 2
			# if more than parent ,quit
			else:
				return

	def minChild(self, index):
		# if there is only left child, no right child
		if index * 2 + 1 > self.currentSize:
			# return left child index
			return index * 2

		else:  # there are left child and right child
			# left child is smaller
			if self.heapList[index * 2] < self.heapList[index * 2 + 1]:
				# return left child index
				return index * 2
			else:
				# otherwise return right child index
				return index * 2 + 1


	def percDown(self, index):
		while (index * 2) <= self.currentSize:  # the node still has child
			minChildIndex = self.minChild(index)

			# current node value is greater than all the child, change position
			if self.heapList[index] > self.heapList[minChildIndex]:
				self.heapList[index], self.heapList[minChildIndex] = \
					self.heapList[minChildIndex], self.heapList[index]

			# change index
			index = minChildIndex
			# if this heap has been ordered, may use short cut, quit compare
			# else:
			#     return

	#
	def buildHeapWithList(self, alist):
		# get the middle level to start
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while (i > 0):
			self.percDown(i)
			i -= 1
	
	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval



def printBTree(bt, depth):
	
	if bt:
		ch = bt.key
	else:
		return
		# ch = '#'
		
	if depth > 0:
		print '%s%s%s' % ((depth - 1) * '  ', '--', ch)
	else:
		print ch
	if not bt:
		return
	printBTree(bt.leftChild, depth + 1)
	printBTree(bt.rightChild, depth + 1)


def createHeapByInsert():
	bh = BinHeap()
	print 'Insert'
	for i in range(0, 100):
		value = (random.random() * 100)
		bh.insert(value)
		print value
	print 'Print Heap'
	tree = binaryTree()
	tree = tree.createLevelOrderTreeWithQueue(bh.heapList)
	printBTree(tree, 0)


def createHeapByList():
	bh = BinHeap()
	print 'List'
	alist = [random.random() for i in range(10)]
	bh.buildHeapWithList(alist)
	tree = binaryTree()
	tree = tree.createLevelOrderTreeWithQueue(bh.heapList)
	printBTree(tree, 0)


if __name__ == '__main__':
	createHeapByList()