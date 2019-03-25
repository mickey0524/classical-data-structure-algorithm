#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: mickey0524
# 实现插入(insert)，冒泡(bubble)，快速(quick)，二分(binary)，堆(heap)，归并(merge)的排序
# 2018-03-26

import heapq, bisect


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
            base_num = arr[tail]
            i = head

            for j in xrange(head, tail):
                if arr[j] < base_num:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[tail], arr[i] = arr[i], arr[tail]

            return i

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

    def api_binary_sort(self):
        """
        用python提供的api实现二分排序
        rtype: list
        """
        arr = self.arr
        length = len(arr)
        res = []

        for i in xrange(length):
            bisect.insort(res, arr[i])

        print res
        return res

    def heap_sort(self):
        """
        堆排序
        rtype: list
        """
        arr = self.arr[:]
        length = len(arr)

        def down(i, j):
            while i < j:
                a, b = 2 * i + 1, 2 * i + 2
                if a >= j:
                    break
                max_idx = a
                if b < j and arr[b] > arr[a]:
                    max_idx = b
                if arr[i] < arr[max_idx]:
                    arr[i], arr[max_idx] = arr[max_idx], arr[i]
                    i = max_idx
                else:
                    break

        for i in xrange(length / 2, -1, -1):
            down(i, length)

        for i in xrange(length - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            down(0, i)

        return arr

    def api_heap_sort(self):
        """
        用python提供的api实现堆排序
        rtype: list
        """
        arr = self.arr
        length = len(arr)
        heap = []

        for i in xrange(length):
            heapq.heappush(heap, arr[i])
        return [heapq.heappop(heap) for _ in xrange(length)]

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

    def cardinality_sort(self):
        """
        O(n)时间复杂度，O(n)空间复杂度的排序
        rtype: list
        """
        arr = self.arr
        max_num, min_num = max(arr), min(arr)
        if min_num < 0:
            max_num -= min_num

        tmp = [0] * (max_num + 1)
        for num in arr:
            num = num if min_num >= 0 else num - min_num
            tmp[num] += 1
        res = []
        if min_num > 0:
            min_num = 0

        for i in xrange(max_num + 1):
            if tmp[i] > 0:
                res.extend([i + min_num] * tmp[i])

        return res


if __name__ == '__main__':
    arr = [1, 4, 5, 2, 4, 7, 8, 9, 4, 5, 10, 12, 43, 1, 0, 123, -1, -5]
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

    print 'api二分排序: ',
    sort.api_binary_sort()

    print '堆排序: ',
    print sort.heap_sort()

    print 'api堆排序: {arr}'.format(arr=sort.api_heap_sort())

    print '归并排序: ',
    merge_sort_arr = sort.arr
    sort.merge_sort(merge_sort_arr, 0, len(merge_sort_arr) - 1)
    print merge_sort_arr

    print 'O(n)时间复杂度排序：',
    print sort.cardinality_sort()
