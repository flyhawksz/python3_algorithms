#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/23 14:30
# @Author  : zhangqi
# @Site    : 
# @File    : Class_Deque.py
# @Software: PyCharm Community Edition


class Deque:
	"""
	Deque
	addFront
	addRear
	removeFront
	removeRear
	isEmpty
	size
	"""
	def __init__(self):
		self.items = []

	def	addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)


if __name__ == '__main__':
	d = Deque()
	print(d.isEmpty())
	d.addRear(4)
	d.addRear('dog')
	d.addFront('cat')
	d.addFront(True)
	print(d.size())
	print(d.isEmpty())
	d.addRear(8.4)
	print(d.removeRear())
	print(d.removeFront())