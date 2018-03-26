#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: mickey0524
# 实现插入(insert)，冒泡(bubble)，快速(quick)，二分(binary)，堆(heap)，归并(merge)的排序
# 2018-03-26

class ListSort(object):

  def __init__(self, arr):
    self.arr = arr
  
  def insert_sort(self):
    """
    普通插入排序
    rtype: list
    """
    arr = self.arr
    length = len(arr)
    for i in xrange(1, length):
      j = 0
      while j < i:
        if arr[i] < arr[j]:
          break  
        j += 1
      if j != i:
        tmp = arr[i]
        for index in xrange(i, j, -1):
          arr[index] = arr[index - 1]
        arr[j] = tmp
    print arr
    return arr


if __name__ == '__main__':
  arr = [1, 4, 5, 2, 4, 7, 8, 9, 4, 5, 10]  
  sort = ListSort(arr)

  print '普通插入排序: ',
  sort.insert_sort()