#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/17 18:07
# @Author  : zhangqi
# @Site    : 
# @File    : Class_LStack.py
# @Software: PyCharm Community Edition

from Class_LNode2 import Node

class StackUnderflow(ValueError):
    pass


class LStack():
    """
    基于连接表技术实现的栈类， 用LNode 作为节点
    """
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("")
        return self._top.elem

    def push(self, elem):
        self._top = Node(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow("")
        p = self._top
        self._top = p.next
        return p.elem

if __name__ == '__main__':
    st = LStack()
    st.push(1)
    st.push(5)
    print(st.pop())
    print(st.top())
    print(st.pop())
    print(st.is_empty())
    st.top()
