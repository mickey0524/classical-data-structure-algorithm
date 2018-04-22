#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: mickey0524
# 全排列实现
# 2018-04-22


def full_permutation(arr):
  """
  :param arr: list 传入的排列
  :return list[list] 返回全排列
  """
  len_arr = len(arr)
  if len_arr == 0:
    return []

  cnt_permutation = [[arr[0]]]
  for index in xrange(1, len_arr):
    num = arr[index]
    tmp_permutation = []
    for permutation in cnt_permutation:
      for i in xrange(len(permutation) + 1):
        copy = permutation[:]
        copy.insert(i, num)
        tmp_permutation.append(copy)
    cnt_permutation = tmp_permutation

  return cnt_permutation

if __name__ == '__main__':
  a = [11, 18, 14, 20, 123]
  print len(full_permutation(a))


