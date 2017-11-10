# -*- coding: utf-8 -*-
# @Time    : 2017-10-25 9:10
# @Author  : zhangqi
# @File    : Question_QuickSort.py
# @Software: PyCharm Community Edition

def quickSort(arr):
	if len(arr)<2:
		return arr
	
	pivot = arr[0]
	less = [ i for i in arr[1:] if i <= pivot]
	greater = [ i for i in arr[1:] if i> pivot]
	
	return  quickSort(less) + [pivot] + quickSort(greater)

if __name__ == '__main__':
	print quickSort([1,3,7,4,2,8,39,224,12])