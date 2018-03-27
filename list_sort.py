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
  
  def quick_sort(self, arr, head, tail):
    """
    快排
    type arr: list 待排序的数组
    type head: int 起始索引
    type tail: int 终止索引
    rtype: list
    """
    def partition(arr, head, tail):
      """
      获取快排中用于分割数组的元素的索引
      type arr: list 待排序的数组
      type head: int 起始索引
      type tail: int 终止索引
      rtype: int
      """
      # 预处理，选取合适的基准元素，减少复杂度
      if arr[head] > arr[tail]:
        arr[head], arr[tail] = arr[tail], arr[head]
      middle = head + (tail - head) / 2
      if head != middle and arr[head] > arr[middle]:
        arr[head], arr[middle] = arr[middle], arr[head]
      
      base_num = arr[head]
      while head < tail:
        while tail > head and arr[tail] >= base_num:
          tail -= 1
        arr[head], arr[tail] = arr[tail], arr[head]
        while head < tail and arr[head] <= base_num:
          head += 1
        arr[head], arr[tail] = arr[tail], arr[head]
      arr[head] = base_num
      return head

    if head < tail:
      middle = partition(arr, head, tail)
      self.quick_sort(arr, head, middle - 1)
      self.quick_sort(arr, middle + 1, tail)
    
  def binary_sort(self):
    """
    二分排序
    rtype: list
    """
    arr = self.arr
    length = len(arr)
    for i in xrange(1, length):
      head, tail = 0, i - 1
      while head <= tail:
        middle = head + (tail - head) / 2
        if arr[middle] <= arr[i]:
          head = middle + 1
        else:
          tail = middle - 1
      tmp = arr[i]
      for j in xrange(i, head, -1):
        arr[j] = arr[j - 1]
      arr[head] = tmp
    print arr
    return arr

  def heap_sort(self):
    """
    堆排序
    rtype: list
    """
    arr = self.arr
    length = len(arr)
    
    for i in xrange(length - 1):
      tail = length - 1 - i
      for j in xrange(tail - 1 / 2, -1, -1):
        left, right = 2 * j + 1, 2 * j + 2
        if left <= tail and arr[left] > arr[j]:
          arr[left], arr[j] = arr[j], arr[left]
        if right <= tail and arr[right] > arr[j]:
          arr[right], arr[j] = arr[j], arr[right]
      arr[tail], arr[0] = arr[0], arr[tail]
    
    print arr
    return arr
    
  def merge_sort(self, arr, head, tail):
    """
    归并排序
    type head: int 起始索引
    type tail: int 终止索引
    rtype: list
    """
    middle = head + (tail - head) / 2
    if middle != head and middle != tail:
      return self.merge_sort(arr, head, middle) + self.merge_sort(arr, middle + 1, tail)
    l_head, l_tail = head, middle
    r_head, r_tail = middle + 1, tail
    extra_arr = []
    while l_head <= l_tail and r_head <= r_tail:
      if arr[l_head] <= arr[r_head]:
        extra_arr += arr[l_head],
        l_head += 1
      else:
        extra_arr += arr[r_head],
        r_head += 1
    if l_head <= l_tail:
      extra_arr += arr[l_head:l_tail + 1]
    else:
      extra_arr += arr[r_head:r_tail + 1]
    return extra_arr
    

if __name__ == '__main__':
  arr = [1, 4, 5, 2, 4, 7, 8, 9, 4, 5, 10, 12, 43, 1, 0, 123]  
  sort = ListSort(arr)

  print '普通插入排序: ',
  sort.insert_sort()

  print '冒泡排序: ',
  sort.bubble_sort()

  print '快速排序: ',
  quick_sort_arr = sort.arr
  sort.quick_sort(quick_sort_arr, 0, len(quick_sort_arr) - 1)
  print quick_sort_arr

  print '二分排序: ',
  sort.binary_sort()

  print '堆排序: ',
  sort.heap_sort()
  
  print '归并排序: ',
  merge_sort_arr = sort.arr
  sort.merge_sort(merge_sort_arr, 0, len(merge_sort_arr) - 1)
  print merge_sort_arr



