#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/23 14:48
# @Author  : zhangqi
# @Site    : 
# @File    : Class_Node.py
# @Software: PyCharm Community Edition


class Node:
	"""
	Node(initdata)
	getData
	getNext
	setData(newdata)
	setNext(newnext)

	"""
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

if __name__ == '__main__':
	temp = Node(39)
	print temp.getData()
