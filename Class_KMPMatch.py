# coding=utf-8

def gen_pnext(p):
    """
    :param p: pattern string
    :return: 最长前缀表，用于KMP算法
    """
    i = 0
    k = -1
    m = len(p)
    pnext = [-1] * m  # 全部设置初值为-1
    while i < m-1:
        if k == -1 or p[i] == p[k]:
            i = i + 1
            k = k + 1
            pnext[i] = k   # 设置 pnext 值

        else:
            k = pnext[k]   # 退到更短相同前缀
    return pnext

def matching_KMP(t, p ,pnext):
    """
    :param t:target string
    :param p: pattern
    :param pnext: 预先处理过的 Pnext 表
    :return: match的位置
    """
    j = 0
    i = 0
    n = len(t)
    m = len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:   # 如果是第一个pnext 或者 匹配成功
            j = j + 1
            i = i + 1
        else:
            i = pnext[i]
    if i == m:  # 找到匹配，返回下标
        return j - i
    return -1


def main():
    tString = '31759021386591402801787614752141025901283781235'
    pString = '028'
    matching_KMP(tString, pString,)


if __name__ == '__main__':
    main()
