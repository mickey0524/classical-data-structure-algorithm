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
  
  def bubble_sort(self):
    """
    冒泡排序
    rype: list
    """
    arr = self.arr
    length = len(arr)
    for i in xrange(0, length - 1):
      for j in xrange(i + 1, length):
        if arr[j] < arr[i]:
          arr[i], arr[j] = arr[j], arr[i]
    print arr
    return arr
  
  def quick_sort(self):
    """
    快排
    rtype: list
    """
    pass

  def binary_sort(self):
    """
    二分排序
    rtype: list
    """
    pass
  
  def heap_sort(self):
    """
    堆排序
    rtype: list
    """
    pass

  def merge_sort(self):
    """
    归并排序
    rtype: list
    """
    pass


if __name__ == '__main__':
  arr = [1, 4, 5, 2, 4, 7, 8, 9, 4, 5, 10]  
  sort = ListSort(arr)

  print '普通插入排序: ',
  sort.insert_sort()

  print '冒泡排序: ',
  sort.bubble_sort()