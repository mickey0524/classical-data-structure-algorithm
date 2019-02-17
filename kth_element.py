# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: mickey0524
# 第 k 大的数
# 2019-02-17


def kth_element(arr, k):
    """
    求数组 arr 中第 k 大的数
    :param arr:
    :return:
    """
    pivot = arr[-1]
    i = 0

    for j in xrange(len(arr) - 1):
        if arr[j] > pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[-1] = arr[-1], arr[i]
    diff = i - k + 1

    if diff == 0:
        return arr[i]
    if diff > 0:
        return kth_element(arr[:i], k)
    return kth_element(arr[i+1:], -diff)


if __name__ == '__main__':
    arr = [6, 1, 3, 5, 7, 2, 4, 9, 11, 8]
    for i in xrange(len(arr)):
        print kth_element(arr, i + 1)
