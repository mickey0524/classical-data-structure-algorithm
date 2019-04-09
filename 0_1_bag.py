#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: mickey0524
# 0-1 背包
# 2019-02-26


weight_sum = 0


def zero_one_bag(idx, cnt_w, max_w, weights):
    global weight_sum
    if idx == len(weights) or cnt_w == max_w:
        if cnt_w > weight_sum:
            weight_sum = cnt_w

    zero_one_bag(idx + 1, cnt_w, max_w, weights)
    if cnt_w + weights[idx] <= max_w:
        zero_one_bag(idx + 1, cnt_w + weights[idx], max_w, weights)


def zero_one_bag_dp(max_w, weights):
    length = len(weights)
    dp = [False] * (max_w + 1)
    dp[0] = True

    for i in xrange(0, length):
        for j in xrange(max_w - weights[i], -1, -1):
            if dp[j]:
                dp[j + weights[i]] = True

    for i in xrange(max_w, -1, -1):
        if dp[i]:
            return i


if __name__ == '__main__':
    print zero_one_bag_dp(16, [1, 3, 2, 4, 6])
