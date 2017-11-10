class LNode(object):                 # 定义一个节点类
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkListUnderflow(ValueError):       # 自定义一个异常
    pass


class Llist(object):                   # 定义一个链表
    def __init__(self):
        self._head = None

    def is_empty(self):                # 判断链表是否为空，通过self._head来判断
        return self._head is None

    def prepend(self, elem):           # 在链表的头部加上元素
        self._head = LNode(elem, self._head)

    def pop(self):                     # 删除表头节点并返回其中的值
        if self._head is None:         # 无结点
            raise LinkListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        print e

    def append(self, elem):
        if self._head is None:              # 在链表的结尾处添加元素
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):                      # 删除链表最后的一个元素
        if self._head is None:
            raise LinkListUnderflow('in pop_last')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:           # 找到链表的倒数第二个节点
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def printall(self):              # 自定义打印出来的结果
        p = self._head
        while p is not None:
            print p.elem
            p = p.next

    def rev(self):                   # 列表翻转的操作
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next                 # 摘下原来的首节点
            q.next = p                          # 将摘下来的节点放到p引用的节点序列中
            p = q
        self._head = p                          # 反转的结点序列做好后，重置表头链接

    def sort1(self):                           # 通过移动表中的元素进行排序
        if self._head is None:
            return
        cart = self._head.next                  # 从首节点之后的结点开始处理
        while cart is not None:
            p = self._head
            x = cart.elem
            while p is not cart and p.elem <= x:    # 跳过小的元素
                p = p.next
            while p is not cart:                    # 置换大的元素和现在的值
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            cart.elem = x                           # 回填最后的一个元素
            cart = cart.next