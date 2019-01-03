#!/usr/bin/env python
# -*- coding=utf-8 -*-
# author: mickey0524
# simple dp such as largest substring sum, longest common subsequence
# 2018-03-30

def largest_substring_sum(arr):
    """
    最长字段和
    type arr: list 输入数组(字符串也一样)
    rtype: int
    """
    res, tmp = 0, 0
    for num in arr:
        if tmp < 0:
            tmp = num
        else:
            tmp += num
        res = max(res, tmp)

    return res


def longest_common_subsequence(a, b):
    """
    最长公共子序列
    type a: str a输入串
    type b: str b输入串
    rtype: (int, str)
    """
    a_len, b_len = len(a), len(b)
    flag, res = [[0] * (b_len + 1) for _ in xrange(a_len + 1)], []

    for i in xrange(a_len):
        for j in xrange(b_len):
            if a[i] == b[j]:
                flag[i + 1][j + 1] = flag[i][j] + 1
            else:
                flag[i + 1][j + 1] = max(flag[i + 1][j], flag[i][j + 1])

    def print_str(i, j):
        if i == 0 or j == 0:
            return
        if flag[i][j] == flag[i - 1][j]:
            print_str(i - 1, j)
        elif flag[i][j] == flag[i][j - 1]:
            print_str(i, j - 1)
        else:
            res.insert(0, b[j - 1])
            print_str(i - 1, j - 1)

    print_str(a_len, b_len)

    return (max([max(row) for row in flag]), ''.join(res))


def longest_common_substring(a, b):
    """
    最长公共字串
    type a: str a输入串
    type b: str b输入串
    rtype: (int, str)
    """
    a_len, b_len = len(a), len(b)
    flag = [[0] * (b_len + 1) for _ in xrange(a_len + 1)]
    max_len, max_i, max_j = 0, None, None

    for i in xrange(a_len):
        for j in xrange(b_len):
            if a[i] == b[j]:
                flag[i + 1][j + 1] = flag[i][j] + 1
                if flag[i + 1][j + 1] > max_len:
                    max_len = flag[i + 1][j + 1]
                    max_i, max_j = i + 1, j + 1
            else:
                flag[i + 1][j + 1] = 0

    res = ''
    while max_i > 0 and max_j > 0 and flag[max_i][max_j] != 0:
        res = b[max_j - 1] + res
        max_i -= 1
        max_j -= 1

    return (max_len, res)


if __name__ == '__main__':
    arr = [6, -3, -3, 1, -9, 7, 7, 6, -7, 5, 5, -1, 10, 0, -7, 9, 1, 1, -7, -8]
    print '最大子串和: {num}'.format(num=largest_substring_sum(arr))

    a, b = 'abcbdab', 'bdcaba'
    print '最长公共子序列: {sequence}'.format(sequence=longest_common_subsequence(a, b))

    print '最长公共子串: {string}'.format(string=longest_common_substring(a, b))
