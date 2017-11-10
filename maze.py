# -*- coding: utf-8 -*-
# @Time    : 2017-9-22 15:18
# @Author  : zhangqi
# @File    : maze.py
# @Software: PyCharm Community Edition

# 迷宫ADT

from myarray2d import Array2D
from lliststack import Stack


class Maze(object):
	MAZE_WALL = "*"  # 墙
	PATH_TOKEN = "x"  # 表示走过的路径
	TRIED_TOKEN = "o"  # 死路
	
	def __init__(self, numRows, numCols):
		self._mazeCells = Array2D(numRows, numCols)
		self._startCell = None
		self._exitCell = None
	
	def numRows(self):
		return self._mazeCells.numRows()
	
	def numCols(self):
		return self._mazeCells.numCols()
	
	def setWall(self, row, col):
		assert 0 <= row < self.numRows() and 0 <= col < self.numCols(), "Cell index out of range."
		self._mazeCells[row, col] = Maze.MAZE_WALL
	
	def setStart(self, row, col):
		assert 0 <= row < self.numRows() and 0 <= col < self.numCols(), "Cell index out of range."
		self._startCell = _CellPosition(row, col)
	
	def setExit(self, row, col):
		assert 0 <= row < self.numRows() and 0 <= col < self.numCols(), "Cell index out of range."
		self._exitCell = _CellPosition(row, col)
	
	def findPath(self):
		dirctions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 方向集
		path = Stack()
		path.push(self._startCell)
		while not path.isEmpty():
			curPos = path.peek()  # 栈顶表示当前位置
			if self._exitFound(curPos.row, curPos.col):  # 检测当前位置是否就是终点
				self._markPath(curPos.row, curPos.col)
				break
			chioce = 0
			for dirction in dirctions:  # 先找出有多少种选择
				if self._validMove(curPos.row + dirction[0], curPos.col + dirction[1]):
					chioce += 1
			if chioce == 0:  # 如果不能移动，就将当前位置标记为'o'，并弹出栈
				self._markTried(curPos.row, curPos.col)
				path.pop()
			else:  # 如果能移动，标记当前位置为'x'，然后选择一个方向进行尝试，直到走到死路或者找到终点。
				for dirction in dirctions:
					if self._validMove(curPos.row + dirction[0], curPos.col + dirction[1]):
						self._markPath(curPos.row, curPos.col)
						nextPos = _CellPosition(curPos.row + dirction[0], curPos.col + dirction[1])
						path.push(nextPos)
						break
		if len(path):
			return True
		else:
			return False
		
		# 删除所有标记，即"x"和"o"。
	
	def reset(self):
		for row in range(self.numRows()):
			for col in range(self.numCols()):
				if self._mazeCells[row, col] in 'ox':
					self._mazeCells[row, col] = None
	
	def draw(self):
		for row in range(self.numRows()):
			str = ''
			for col in range(self.numCols()):
				if self._mazeCells[row, col] != None:
					str += self._mazeCells[row, col]
				else:
					str += '.'
			print str
		
		# 是否能移动到该位置
	
	def _validMove(self, row, col):
		return 0 <= row < self.numRows() and 0 <= col < self.numCols() and self._mazeCells[row, col] is None
	
	# 判断当前点是否为终点
	def _exitFound(self, row, col):
		return row == self._exitCell.row and col == self._exitCell.col
	
	# 将该位置设置为死路
	def _markTried(self, row, col):
		self._mazeCells[row, col] = Maze.TRIED_TOKEN
	
	# 标记走过的路
	def _markPath(self, row, col):
		self._mazeCells[row, col] = Maze.PATH_TOKEN
	
	# 储存类


class _CellPosition(object):
	def __init__(self, row, col):
		self.row = row
		self.col = col
	
		
	
# 从文件中建立迷宫，并解决迷宫


# 建立迷宫
def buildMaze(filename):
	with open(filename, 'r') as infile:
		nrows, ncols = readValuePair(infile)  # 迷宫大小
		maze = Maze(nrows, ncols)  # 建立迷宫，并初始化
		
		row, col = readValuePair(infile)
		maze.setStart(row, col)  # 根据给定坐标设定起始点
		row, col = readValuePair(infile)
		maze.setExit(row, col)  # 设定终点
		# 设定墙
		for row in range(nrows):
			line = infile.readline()
			for col in range(len(line)):
				if line[col] == "*":
					maze.setWall(row, col)
		infile.close()
	return maze


# 辅助方法，从给定文件中读取整数对值
def readValuePair(infile):
	line = infile.readline()
	(valA, valB) = tuple(line.split())
	return int(valA), int(valB)


def main():
	maze = buildMaze("mazefile.txt")
	if maze.findPath():
		print "Path found ..."
		maze.draw()
	else:
		print "Path not found ..."


if __name__ == "__main__":
	main()