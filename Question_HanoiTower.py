#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/5 18:21
# @Author  : zhangqi
# @Site    : 
# @File    : Question_HanoiTower.py
# @Software: PyCharm Community Edition

# 一个简单的条件循环语句实现汉诺塔问题

def my_print(args):
	print args


def move(n, a, b, c):
	my_print((a, '-->', c)) if n == 1 else (move(n - 1, a, c, b) or move(1, a, b, c) or move(n - 1, b, a, c))


def move2(n, a, b, c):
	if n == 1:
		x = (a, '-->', c)
	else:
		x = (move(n - 1, a, c, b) or move(1, a, b, c) or move(n - 1, b, a, c))


if __name__ == '__main__':
	move(3, 'a', 'b', 'c')
