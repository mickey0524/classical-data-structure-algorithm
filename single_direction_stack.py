#!/usr/bin/env python
# -*- coding=utf-8 -*-
# author: mickey0524
# single direction stack
# 数组中元素前一个比它小的元素
# 2019-04-26


from collections import deque


def single_direction_stack(arr):
    stack = deque([])
    res = []

    for n in arr:
        while stack and stack[-1] >= n:
            stack.pop()

        res.append(None if not stack else stack[-1])
        stack.append(n)

    return res


if __name__ == '__main__':
    arr = [1, 7, 2, 3, 5, 4, 9, 10]
    print single_direction_stack(arr)