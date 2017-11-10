#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/24 0:00
# @Author  : zhangqi
# @Site    : 
# @File    : Question_TurtleDrawByRecursion.py
# @Software: PyCharm Community Edition

import turtle


def tree(branchLen, t):
	if branchLen > 5:
		t.forward(branchLen)
		t.right(20)
		tree(branchLen-15, t)
		t.left(40)
		tree(branchLen-15, t)
		t.right(20)
		t.backward(branchLen)


def drawTree():
	t = turtle.Turtle()
	myWin = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.color("green")
	tree(75, t)
	myWin.exitonclick()


# __________________________________________________________________
myTurtle = turtle.Turtle()
myWin = turtle.Screen()


def Spiral(myTurtle, lineLen):
	if lineLen > 0:
		myTurtle.forward(lineLen)
		myTurtle.right(60)
		Spiral(myTurtle, lineLen-10)


def drawSpiral():
	Spiral(myTurtle, 200)
	myWin.exitonclick()


if __name__ == '__main__':
	drawSpiral()
