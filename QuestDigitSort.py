# -*- coding: utf-8 -*-
# @Time    : 2017-10-24 17:14
# @Author  : zhangqi
# @File    : QuestDigitSort.py
# @Software: PyCharm Community Edition

def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	tmp = len(arr)
	for i in range(tmp):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
			
	return smallest_index


def digitSort(arr):
	newArray = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArray.append(arr.pop(smallest))
		
	return newArray

if __name__ == '__main__':
	print (digitSort([1,5,7,9,4,2,3]))
	
		
		
	