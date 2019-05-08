#!/usr/bin/env python
# -*- coding=utf-8 -*-
# author: mickey0524
# single direction stack
# 2019-04-26


from collections import deque


# 数组中元素前一个比它小的元素
def single_direction_stack(arr):
    stack = deque([])
    res = []

    for n in arr:
        while stack and stack[-1] >= n:
            stack.pop()

        res.append(None if not stack else stack[-1])
        stack.append(n)

    return res


# 最大字典序子序列
def max_dictionary_order_subsequence(s):
    stack = deque([])

    for ch in s:
        while stack and stack[-1] < ch:
            stack.pop()
        stack.append(ch)

    return ''.join(stack)


# 最小字典序子序列，每个字符使用一次
def max_dictionary_order_subsequence_v1(s):
    stack = deque([])
    last_idx_arr = [0] * 26
    is_visited = [False] * 26

    for i, ch in enumerate(s):
        idx = ord(ch) - 97
        last_idx_arr[idx] = i

    for i, ch in enumerate(s):
        idx = ord(ch) - 97
        while stack and last_idx_arr[stack[-1]] > i and stack[-1] >= idx:
            is_visited[stack.pop()] = False
        if not is_visited[idx]:
            stack.append(idx)
            is_visited[idx] = True

    res = ''
    while stack:
        res = chr(stack.pop() + 97) + res

    return res


# 最小字典序子序列，每个字符最少一次
def max_dictionary_order_subsequence_v2(s):
    pass


# 指定长度最小字典序子序列
def max_dictionary_order_subsequence_v3(s):
    pass


if __name__ == '__main__':
    arr = [1, 7, 2, 3, 5, 4, 9, 10]
    print single_direction_stack(arr)

    print max_dictionary_order_subsequence('ababba')

    print max_dictionary_order_subsequence_v1('babbdcc')
