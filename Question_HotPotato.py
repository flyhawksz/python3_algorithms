#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/23 11:39
# @Author  : zhangqi
# @Site    : 
# @File    : Question_HotPotato.py
# @Software: PyCharm Community Edition

from queue import Queue

def hotPotato(nameList, killNumber):
	killedSequence = Queue()
	simqueue = Queue()
	for name in nameList:
		simqueue.enqueue(name)

	while simqueue.size() > 1:
		for i in range(killNumber):
			simqueue.enqueue(simqueue.dequeue())

		killedGuy = simqueue.dequeue()
		# print killedGuy
		killedSequence.enqueue(killedGuy)

	lastGuy = simqueue.dequeue()
	print 'The last one to live is: ' + lastGuy
	killedSequence.enqueue(lastGuy)
	return killedSequence


def printQueue(qu):
	while not qu.isempty():
		print qu.dequeue()


if __name__ == "__main__":
	nameList = []
	for j in range(10):
		nameList.append('guy' + str(j))

	printQueue(hotPotato(nameList, 7))





