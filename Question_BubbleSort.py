# -*- coding: utf-8 -*-
# @Time    : 2017-10-26 17:03
# @Author  : zhangqi
# @File    : Question_BubbleSort.py
# @Software: PyCharm Community Edition

def bubbleSort(alist):
	
	for pass_number in range(len(alist) - 1, 0, -1):
		for compare_number in range(0, pass_number, 1):
			if alist[compare_number] > alist[pass_number]:
				alist[compare_number], alist[pass_number ] = alist[pass_number], alist[compare_number]
			print(alist)
		#print(alist)
		
	return alist

if __name__ == '__main__':
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print(alist)
	print (bubbleSort(alist))
