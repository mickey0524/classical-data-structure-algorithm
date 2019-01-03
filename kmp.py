# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: mickey0524
# kmp 算法
# 2019-01-03


def kmp(a, b):
    """
    kmp 算法
    :param a: 长串
    :param b: 子串
    :return:
    """
    len_a, len_b = len(a), len(b)
    if len_a < len_b:
        return False
    if a == b:
        return True

    next = gen_next(b)
    i, j = 0, 0

    while i < len_a and j < len_b:
        if j == -1 or a[i] == b[j]:
            i += 1
            j += 1
        else:
            j = next[j]

    if j == len_b:
        return True

    return False


def gen_next(s):
    """
    生成 next 数组
    :param s:
    :return:
    """
    length = len(s)
    next = [0] * length
    next[0] = -1
    k, j = -1, 0

    while j < length - 1:
        if k == -1 or s[k] == s[j]:
            k += 1
            j += 1
            next[j] = k
        else:
            k = next[k]

    return next


if __name__ == '__main__':
    a = 'BBC ABCDAB ABCDABCDABDE'
    b = 'ABCDABD'
    c = 'ABCDABE'

    print kmp(a, b)
    print kmp(a, c)
