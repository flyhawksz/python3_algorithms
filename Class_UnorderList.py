#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/23 14:45
# @Author  : zhangqi
# @Site    : 
# @File    : Class_UnorderList.py
# @Software: PyCharm Community Edition

from Class_Node import Node
import numpy as np



class UnorderList:
	"""
	UnorderList
	addItemFront(item)
	addItemRear(item)
	popFront
	popRear
	searchItem(item)
	isEmpty
	size


	"""
	def __init__(self):
		self.head = None

	def addFront(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		# temp.next = self.head
		self.head = temp

	def addRear(self, item):
		t = Node(item)
		if self.head is None:
			self.head = t
		else:
			p = self.head
			while p.next is not None:
				p = p.next
			p.next = t

	def popFront(self):
		temp = self.head
		self.head = self.head.next
		return temp

	def popRear(self):
		p = self.head
		# only one element
		if p.next is None:
			return self.head

		# more than one element, and p.next is last one
		while p.next.next is not None:
			p = p.next
		temp = p.next
		p.next = None
		return temp

	def delLast(self):
		p = self.head
		# only one element
		if p.next is None:
			self.head = None

		# more than one element, and p.next is last one
		while p.next.next is not None:
			p = p.next
		p.next = None

	def searchItem(self, item):
		current = self.head
		found = False
		while current is not None:
			temp = current.getData()
			if temp == item:
				found = True
				return found
			else:
				current = current.getNext()
		return found

	def isEmpty(self):
		return self.head is None

	def size(self):
		currentNode = self.head
		count = 0
		while currentNode is not None:
			currentNode = currentNode.getNext
			count = count + 1
		return count

	def printList(self):
		current = self.head
		if current is not None:
			if current.next is None:
				print current.getData()
			else:
				while current is not None:
					print current.getData()
					current = current.getNext()


if __name__ == '__main__':
	testList = UnorderList()
	for i in (np.random.randint(1, 100, size=10)):
		testList.addFront(i)

	found = input('input a number to find:')
	print 'the result is: ' + str(testList.searchItem(found))
	testList.printList()
