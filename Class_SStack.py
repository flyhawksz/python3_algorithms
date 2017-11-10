# coding=utf-8


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


if __name__ == '__main__':
    st = SStack()
    st.push(1)
    st.push(5)
    print(st.pop())
    print(st.top())
    print(st.pop())
    print(st.is_empty())
    st.top()
