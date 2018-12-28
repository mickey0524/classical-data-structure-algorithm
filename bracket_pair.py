#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: mickey0524
# 括号匹配，非常经典的问题（卡特兰公式的应用)
# 2018-04-03


def dfs_all_bracket_pair(pair_num):
    """
    给出所有合法的括号
    type pair_num: int 括号对数
    rtype: list
    """
    if pair_num <= 0:
        return ['']

    if pair_num == 1:
        return ['()']

    res = []

    for i in xrange(1, pair_num + 1):
        left, right = dfs_all_bracket_pair(i - 1), dfs_all_bracket_pair(pair_num - i)
        for j in left:
            for k in right:
                res.append('(' + j + ')' + k)

    return res


def resursive_all_bracket_pair(pair_num):
    """
    递归的给出结果，效率更高
    type pair_num: int 括号对数
    rtype: list
    :param pair_num:
    :return:
    """

    def resursive(path, left, right):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left < right:
            resursive(path + ')', left, right - 1)

        if left > 0:
            resursive(path + '(', left - 1, right)

    res = []
    resursive('', pair_num, pair_num)
    return res


if __name__ == '__main__':
    print dfs_all_bracket_pair(3)

    print resursive_all_bracket_pair(3)
