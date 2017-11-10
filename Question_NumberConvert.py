#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/23 21:04
# @Author  : zhangqi
# @Site    : 
# @File    : Question_NumberConvert.py
# @Software: PyCharm Community Edition


def decToNBaseByRecursion(dec, base):
	"""
	# method 1 conver use Recursion(递归)
	:param number:source number
	:param base: target base
	:return: string
	"""
	convert_string = '0123456789ABCDEF'
	if dec < base:
		return convert_string[dec]
	else:
		# print convert_string[dec % base]
		# 余数要反过来写，形成转换
		# convert_string[dec % base] 经典，省去了各级if
		return decToNBaseByRecursion(dec/base, base) + convert_string[dec % base]


def decToNBaseByCycle(dec, base):
	"""
	# method 1 conver use Recursion(递归)
	:param number:source number
	:param base: target base
	:return: string
	"""
	convert_string = '0123456789ABCDEF'
	result = []
	t = dec
	while t >= 1:
		if t < base:
			result.append(convert_string[t])
		else:
			# 余数要反过来写，形成转换
			# convert_string[dec % base] 经典，省去了各级if
			result.append(convert_string[t % base])
		t = t/base
	result.reverse()
	return ''.join(map(str, result))


if __name__ == '__main__':
	print decToNBaseByRecursion(217, 16)
	print decToNBaseByRecursion(21, 8)
	print decToNBaseByRecursion(21, 2)
	#
	print decToNBaseByCycle(217, 16)
	print decToNBaseByCycle(21, 8)
	print decToNBaseByCycle(21, 2)


