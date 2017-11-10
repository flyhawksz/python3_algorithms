# coding = utf-8
from Class_LNode import LNode

class LinkedListUnderflow(ValueError):
    pass



class LList:
    '''
    ADT List：          #建立List抽象数据类型
        List（）          #创建一个新表
        is_empty（）        #是否空表
        len（）           #长度
        prepend(elem)     #

        append(self)
        insert(self)
        del_first(self)
        del_last(self)
        del(self, i)

        search(self,elem)
        forall(self, op)        #对所有元素执行OP


    自定义链表
    建立空表

    '''
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        p = self._head
        n = 0
        while p.next is not None:
            p = p.next
            n = n + 1
        return n

    def prepend(self, elem):
        p = LNode(elem)
        p.next = self._head
        self._head = p

        # self._head = LNode(elem, self._head)   #right answer

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head
        self._head = self._head.next
        return e

    def append(self, elem):
        t = LNode(elem)
        if self._head is None:
            self._head = t
        else:
            p = self._head
            while p.next is not None:
                p = p.next
            p.next = t

    def insert(self, elem):
        pass

    def del_first(self):
        pass

    def del_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in del")

        p = self._head
        # only one element
        if p.next is None:
            self._head = None

        # more than one element, and p.next is last one
        while p.next.next is not None:
            p = p.next
        p.next = None

    def del_elem(self, i):
        pass

    def search(self, pred):
        p = self._head
        while p.next is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

        pass

    def forall(self, op):   # 对所有元素执行OP
        pass