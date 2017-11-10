# -*- coding: utf-8 -*-
# @Time    : 2017-9-21 10:21
# @Author  : zhangqi
# @File    : Class_fib.py
# @Software: PyCharm Community Edition

def fib21(i):
    firstNumber = 0
    secondNumber = 1

    for l in range(i):
        print firstNumber
        # method 1
        firstNumber, secondNumber = secondNumber, firstNumber + secondNumber
        # 在这里需要注意，“i, j = i, i + j”这条代码不能写成如下所示：
        # i = j
        # j = i + j
        # 如果写成这样，j就不是前两位相加的值，而是已经被j赋过值的i和j相加的值
        # print firstNumber
    # 返回某项
    return firstNumber

def fib22(i):
    firstNumber = 0
    secondNumber = 1

    for l in range(i):
        if l == 0:
            fiboNumber = 0
            print fiboNumber
        elif l == 1:
            fiboNumber = 1
            print fiboNumber
        else:
            # method 2
            fiboNumber = firstNumber + secondNumber
            firstNumber = secondNumber
            secondNumber = fiboNumber
            print fiboNumber

    print '-'*50
    return fiboNumber


def fib(i):
    """
    :param i:int number
    :return: one fibo number
    """
    if i == 0 or i == 1:
        return i
    else:
        return fib(i-1) + fib(i - 2)


if __name__ == '__main__':
    # 获取用户输入
    nterms = int(input("您要输出几项? "))

    # 检查输入的数字是否正确
    if nterms <= 0:
        print("输入正数")
    else:
        print("斐波那契数列:")
        # test 1
        # fib21(nterms)

        # test 2
        print(fib22(nterms))


        # test3
        # print(fib(nterms - 1))
        # for i in range(nterms):
        #     print(fib(i))


