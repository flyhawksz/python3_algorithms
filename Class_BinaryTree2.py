# -*- coding: utf-8 -*-
# @Time    : 2017-9-27 14:24
# @Author  : zhangqi
# @File    : Class_BinaryTree.py
# @Software: PyCharm Community Edition

myTree = None

class StackUnderflow(ValueError):
    pass

class SStack():
	"""
    基于顺序表技术的栈类
    采用list对象，_elems 存储栈中元素
    所有栈操作映射到list操作
    """
	
	# noinspection InjectedReferences
	def __init__(self):
		"""
        生成一个空表
        """
		self._elems = []
	
	def is_empty(self):
		return self._elems == []
	
	def top(self):
		if self._elems == []:
			raise StackUnderflow("here")
		return self._elems[-1]
	
	def push(self, elem):
		self._elems.append(elem)
	
	def pop(self):
		if self._elems == []:
			raise StackUnderflow('')
		return self._elems.pop()


class treeNode:
	def __init__(self, rootObj=None, leftChild=None, rightChild=None):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None


class binaryTree:
	"""
	BinaryTree(self, binaryTreeObj)
	isEmpty(self)
	num_nodes(self)
	getData(self)
	getLeftChild()
	getRightChild()
	setLeftChild(self, btree)
	setRightChild(self, btree)
	traversal(self)   # 遍历二叉树节点迭代器
	forall()
	"""
	
	def __init__(self):
		self.root = treeNode()
	
	def createTreeByInput(self, root):
		"""
		input with pre-order string, and it is easy change into other order
		:param root:
		:return: root, a tree
		"""
		tmpKey = input("please input a key, input '#' for Null")
		if tmpKey == '#':
			root = None
		else:
			root = treeNode(rootObj=tmpKey)
			root.leftChild = self.createTreeByInput(root.leftChild)
			root.rightChild = self.createTreeByInput(root.rightChild)
		
		return root
	
	def createTreeByListWithRecursion(self, preOrderList):
		"""
		根据前序列表重建二叉树
		:param preOrder: 输入前序列表
		:return: 二叉树
		"""
		preOrder = preOrderList
		if preOrder is None or len(preOrder) <= 0:
			return None
		currentItem = preOrder.pop(0)  # 模拟C语言指针移动
		if currentItem is '#':
			root = None
		else:
			root = treeNode(currentItem)
			root.leftChild = self.createTreeByListWithRecursion(preOrder)
			root.rightChild = self.createTreeByListWithRecursion(preOrder)
		return root
	
	def createTreeByListWithStack(self, preOrderList):
		"""
		根据前序列表重建二叉树
		:param preOrder: 输入前序列表
		:return: 二叉树
		"""
		preOrder = preOrderList
		pStack = SStack()
		
		# check
		if preOrder is None or len(preOrder) <= 0 or preOrder[0] is '#':
			return None
		
		# get the root
		tmpItem = preOrder.pop(0)
		root = treeNode(tmpItem)
		
		# push root
		pStack.push(root)
		currentRoot = root
		
		while preOrder:
			# get another item
			tmpItem = preOrder.pop(0)
			# has child
			if tmpItem is not '#':
				# does not has left child, insert one
				if currentRoot.leftChild is None:
					currentRoot = self.insertLeft(currentRoot, tmpItem)
					pStack.push(currentRoot.leftChild)
					currentRoot = currentRoot.leftChild
				
				# otherwise insert right child
				elif currentRoot.rightChild is None:
					currentRoot = self.insertRight(currentRoot, tmpItem)
					pStack.push(currentRoot.rightChild)
					currentRoot = currentRoot.rightChild
			# one child is null
			else:
				# if has no left child
				if currentRoot.leftChild is None:
					currentRoot.leftChild = None
					
					# get another item fill right child
					tmpItem = preOrder.pop(0)
					# has right child
					if tmpItem is not '#':
						currentRoot = self.insertRight(currentRoot, tmpItem)
						pStack.push(currentRoot.rightChild)
						currentRoot = currentRoot.rightChild
					# right child is null
					else:
						currentRoot.rightChild = None
						# pop itself
						parent = pStack.pop()
						# pos parent
						if not pStack.is_empty():
							parent = pStack.pop()
						# parent become current root
						currentRoot = parent
						
						# return from right child, so the parent has right child, go to parent's parent
						if currentRoot.rightChild is not None:
							if not pStack.is_empty():
								parent = pStack.pop()
								currentRoot = parent
				
				# there is a leftchild ,fill right child with null and return to parent
				else:
					currentRoot.rightChild = None
					# pop itself
					parent = pStack.pop()
					if not pStack.is_empty():
						parent = pStack.pop()
					currentRoot = parent
		
		return root
	
	def createLevelOrderTreeWithQueue(self, levOder):
		"""
		:param root: a empty tree objedt
		:param levOder: a list that item in level order
		:return: tree
		"""
		root = treeNode()
		
		if len(levOder) < 1:
			return None
		
		t = 0
		myQueue = []
		
		currentRoot = root
		myQueue.append(currentRoot)
		while myQueue and t <= len(levOder) - 1:
			currentRoot = myQueue.pop(0)
			currentRoot.key = levOder[t]
			t += 1
			
			if currentRoot.leftChild is None:
				myQueue.append(self.insertLeft(currentRoot, None).leftChild)
			if currentRoot.rightChild is None:
				myQueue.append(self.insertRight(currentRoot, None).rightChild)
		
		return root
	
	def insertLeft(self, root, newNode):
		if root.leftChild is None:
			root.leftChild = treeNode(newNode)
		else:
			tmpNode = treeNode(newNode)
			tmpNode.leftChild = root.leftChild
			root.leftChild = tmpNode
		
		return root
	
	def insertRight(self, root, newNode):
		if root.rightChild is None:
			root.rightChild = treeNode(newNode)
		else:
			tmpNode = treeNode(newNode)
			tmpNode.rightChild = root.rightChild
			root.rightChild = tmpNode
		
		return root
	
	def isEmpty(self):
		return self.key is None
	
	def setRootValue(self, obj):
		self.key = obj
	
	def getRootValue(self):
		return self.key
	
	def getLeftChild(self):
		return self.leftChild
	
	def getRightChild(self):
		return self.rightChild


def printBTree(self, bt, depth):
	'''''
	递归打印这棵二叉树，#号表示该节点为NULL
	'''
	
	ch = bt.key if bt else '#'
	if depth > 0:
		print( '%s%s%s' % ((depth - 1) * '  ', '--', ch))
	else:
		print (ch)
	if not bt:
		return
	printBTree(bt.leftChild, depth + 1)
	printBTree(bt.rightChild, depth + 1)


# 1 creat a tree with insert method
def createTreeByMethod():
	myTree = binaryTree()
	myTree.setRootValue('a')
	print (myTree.getRootValue())
	myTree.insertLeft('b')
	myTree.insertRight('c')
	myTree.getLeftChild().insertRight('d')
	myTree.getRightChild().insertLeft('e')
	myTree.getRightChild().insertRight('f')
	myTree.getRightChild().getRightChild().getRootValue
	
	print(myTree.getLeftChild())
	print(myTree.getLeftChild().getRootValue())
	
	print(myTree.getRightChild())
	print(myTree.getRightChild().getRootValue())
	
	myTree.getLeftChild().setRootValue('hello')
	print (myTree.getLeftChild().getRootValue())


# 2.create a tree with string in preoder
def createTreeByListWithRecursion(myTree, treeElements):
	myTree = myTree.createTreeByListWithRecursion(list(treeElements))
	printBTree(myTree, 0)
	return myTree


def createTreeByListWithStack(myTree, treeElements):
	myTree = myTree.createTreeByListWithStack(list(treeElements))
	printBTree(myTree, 0)
	return myTree


# 3.create a tree by input
def createTreeByInput(myTree):
	myTree = myTree.createTreeByInput(myTree)
	printBTree(myTree, 0)
	return myTree


# 	to do something with data
def todo(root):
	if root.key is not None:
		print (root.key)


# pre-order traversal with recursion
def preorderTraversalWithRecursion(root):
	if root is not None:
		todo(root)
		preorderTraversalWithRecursion(root.leftChild)
		preorderTraversalWithRecursion(root.rightChild)


# in-order traversal with recursion
def inorderTraversalWithRecursion(root):
	if root is not None:
		inorderTraversalWithRecursion(root.leftChild)
		todo(root)
		inorderTraversalWithRecursion(root.rightChild)


# post-order traversal with recursion
def postorderTraversalWithRecursion(root):
	if root is not None:
		postorderTraversalWithRecursion(root.leftChild)
		postorderTraversalWithRecursion(root.rightChild)
		todo(root)


# pre-order traversal with stack
def preorderTraversalWithStack(root):
	if root is None:
		return
	
	myStack = []
	while root or myStack:
		# check left child
		while root:
			todo(root)
			myStack.append(root)
			root = root.leftChild
		# finish check left child. left child is None, loop over
		
		# get parent
		root = myStack.pop()
		# check right child
		root = root.rightChild


# another methode
def preorderTraversalWithStack2(root):
	myStack = SStack()
	while root or myStack:
		while root:  # go down ro the left
			todo(root)  # deal with data
			myStack.push(root.rightChild)  # push right child
			root = root.leftChild
		root = myStack.pop()  # end of left branch , go back deal with right branch


# in-order traversal with stack
def inorderTraversalWithStack(root):
	if root is None:
		return
	
	myStack = []
	while root or myStack:
		# check left sub-tree get the last child
		while root:
			myStack.append(root)
			root = root.leftChild
		# finish check left child. left child is None, loop over
		
		
		# the last child is None , get parent
		root = myStack.pop()
		todo(root)
		# check right child
		root = root.rightChild


# post-order traversal with stack
def postorderTraversalWithStack(root):
	"""利用堆栈实现树的后序遍历"""
	if root is None:
		return
	myStack1 = []
	myStack2 = []
	node = root
	myStack1.append(node)
	while myStack1:  # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
		node = myStack1.pop()
		if node.leftChild:
			myStack1.append(node.leftChild)
		if node.rightChild:
			myStack1.append(node.rightChild)
		myStack2.append(node)
	while myStack2:  # 将myStack2中的元素出栈，即为后序遍历次序
		todo(myStack2.pop())


# level-order traversal with queue
def levelorderTraversalWithQueue(root):
	if root is None:
		return
	myQueue = []
	node = root
	myQueue.append(node)
	while myQueue:
		node = myQueue.pop(0)
		todo(node)
		if node.leftChild is not None:
			myQueue.append(node.leftChild)
		if node.rightChild is not None:
			myQueue.append(node.rightChild)


if __name__ == '__main__':
	myTree = binaryTree()
	treeElements = '124#8##5##369###7##'
	# myTree = createTreeByListWithStack(myTree, treeElements )
	
	myTree = createTreeByListWithRecursion(myTree, treeElements)
	
	# myTree = createTreeByInput(myTree)
	print ('*' * 80)
	print ('pre-order Traversal')
	preorderTraversalWithRecursion(myTree)
	print ('-' * 80)
	preorderTraversalWithStack(myTree)
	
	print ('*' * 80)
	print ('in-order Traversal')
	print ('*' * 80)
	inorderTraversalWithRecursion(myTree)
	print ('-' * 80)
	inorderTraversalWithStack(myTree)
	
	print ('*' * 80)
	print ('pos-order Traversal')
	print ('*' * 80)
	postorderTraversalWithRecursion(myTree)
	print ('-' * 80)
	postorderTraversalWithStack(myTree)
	
	print ('*' * 80)
	print ('level-order Traversal')
	print ('*' * 80)
	levelorderTraversalWithQueue(myTree)
	print ('-' * 80)
