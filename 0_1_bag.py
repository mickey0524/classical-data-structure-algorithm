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
