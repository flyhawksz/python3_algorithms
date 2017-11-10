# coding=utf-8

def BfMatch(t, p):  # target, partern , program with my mind
    tlen = len(t)
    plen = len(p)

    i = 0
    j = 0

    if tlen >= plen:
        for i in range(tlen - plen + 1):
            k = i
            for j in range(plen):
                if t[k] != p[j]:
                    break
                k = k + 1

            if j == plen - 1:
                return i + 1
            else:
                j = 0

        return -1


        # 朴素匹配


def naive_match(s, p):
    m = len(s);
    n = len(p)
    for i in range(m - n + 1):  # 起始指针i
        if s[i:i + n] == p:
            return i
    return -1

    # 朴素匹配


def naive_match2(t, p):
    m = len(p)
    n = len(t)

    i, j = 0, 0

    while i < m and j < n:
        if t[j] == p[i]:
            i = i + 1
            j = j + 1
        else:
            j, i = j - i + 1, 0

            # j = j - i + 1
            # i = 0

        if i == m:
            return j - i

    return -1



def BF3(t, p):
    i = 0
    j = 0
    count = 0

    while (i <= len(t) - len(p)):
        j = 0
        while (t[i] == p[j]):
            i = i + 1
            j = j + 1

            if j == len(p):  #find
                break
            elif (j == len(p) - 1):
                count = count + 1
            else:
                i = i + 1
                j = 0
    return count


if __name__ == '__main__':
    t = 'adbdlkaslduabiowqnl;na;lvjoabpabajoqwierjhkjasdkabxioqabcwuerijbksljdfbiaboargebjjkzxbvjbxzkclvbnwioquegrubv'
    p = 'abc'
    # t = "this is a big apple,this is a big apple,this is a big apple,this is a big apple."
    # p = "apple"

    # t = "为什么叫向量空间模型呢？其实我们可以把每个词给看成一个维度，而词的频率看成其值（有向），即向量，这样每篇文章的词及其频率就构成了一个i维空间图，两个文档的相似度就是两个空间图的接近度。假设文章只有两维的话，那么空间图就可以画在一个平面直角坐标系当中，读者可以假想两篇只有两个词的文章画图进行理解。"
    # p = "读者"

    # print (BfMatch(t, p))
    # print (naive_match(t, p))
    print (naive_match2(t, p))
    # print (BF3(t, p))
