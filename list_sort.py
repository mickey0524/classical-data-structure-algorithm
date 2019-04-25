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
        arr = self.arr[:]
        length = len(arr)
        for i in xrange(1, length):
            for j in xrange(i - 1, -1, -1):
                if arr[j + 1] < arr[j]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                else:
                    break

        print arr
        return arr

    def shell_sort(self):
        """
        希尔排序
        :return:
        """
        arr = self.arr[:]
        length = len(arr)
        h = 1
        while h < length / 3:
            h = 3 * h + 1

        while h >= 1:
            for i in xrange(h, length):
                for j in xrange(i, h - 1, -h):
                    if arr[j] < arr[j - h]:
                        arr[j], arr[j - h] = arr[j - h], arr[j]
                    else:
                        break

            h /= 3
        print arr

    def select_sort(self):
        arr = self.arr[:]
        length = len(arr)

        for i in xrange(length - 1):
            cur_min_idx = i
            for j in xrange(i, length):
                if arr[j] < arr[cur_min_idx]:
                    cur_min_idx = j
            arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]

        print arr
        return arr

    def bubble_sort(self):
        """
        冒泡排序
        rype: list
        """
        arr = self.arr[:]
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
        arr = self.arr[:]
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
        arr = self.arr[:]
        length = len(arr)
        res = []

        for i in xrange(length):
            bisect.insort(res, arr[i])

        print res
        return res

    def heap_sort_v1(self):
        """
        堆排序 - down 建堆版本
        rtype: list
        """
        arr = self.arr[:]
        length = len(arr)

        for i in xrange(length / 2, -1, -1):
            self.heap_down(arr, i, length)

        for i in xrange(length - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heap_down(arr, 0, i)

        return arr

    @staticmethod
    def heap_down(arr, i, j):
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

    @staticmethod
    def heap_up(arr, i):
        while i > 0:
            parent_id = (i - 1) / 2
            if parent_id < 0:
                break
            if arr[i] > arr[parent_id]:
                arr[i], arr[parent_id] = arr[parent_id], arr[i]
                i = parent_id
            else:
                break

    def heap_sort_v2(self):
        """
        堆排序 - up 建堆版本
        :return:
        """
        length = len(self.arr)
        arr = []

        for i in xrange(length):
            arr += self.arr[i],
            self.heap_up(arr, i)

        for i in xrange(length - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heap_down(arr, 0, i)

        return arr

    def api_heap_sort(self):
        """
        用python提供的api实现堆排序
        rtype: list
        """
        arr = self.arr[:]
        length = len(arr)
        heap = []

        for i in xrange(length):
            heapq.heappush(heap, arr[i])
        return [heapq.heappop(heap) for _ in xrange(length)]

    def merge_sort(self, arr):
        """
        归并排序
        type head: int 起始索引
        type tail: int 终止索引
        rtype: list
        """
        length = len(arr)
        if length < 2:
            return arr

        pivot = length / 2
        l, r = self.merge_sort(arr[:pivot]), self.merge_sort(arr[pivot:])
        tmp = []
        l_idx, r_idx = 0, 0
        l_len, r_len = len(l), len(r)

        while l_idx < l_len and r_idx < r_len:
            if l[l_idx] <= r[r_idx]:
                tmp += l[l_idx],
                l_idx += 1
            else:
                tmp += r[r_idx],
                r_idx += 1

        if l_idx < l_len:
            tmp += l[l_idx:]

        if r_idx < r_len:
            tmp += r[r_idx:]

        return tmp

    def cardinality_sort(self):
        """
        O(n)时间复杂度，O(n)空间复杂度的排序
        rtype: list
        """
        arr = self.arr[:]
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

    print '希尔排序: ',
    sort.shell_sort()

    print '选择排序: ',
    sort.select_sort()

    print '冒泡排序: ',
    sort.bubble_sort()

    print '快速排序: ',
    quick_sort_arr = sort.arr[:]
    sort.quick_sort(quick_sort_arr, 0, len(quick_sort_arr) - 1)
    print quick_sort_arr

    print '二分排序: ',
    sort.binary_sort()

    print 'api二分排序: ',
    sort.api_binary_sort()

    print '堆排序: ',
    print sort.heap_sort_v1()
    print sort.heap_sort_v2()

    print 'api堆排序: {arr}'.format(arr=sort.api_heap_sort())

    print '归并排序: ',
    merge_sort_arr = sort.merge_sort(sort.arr[:])
    print merge_sort_arr

    print 'O(n)时间复杂度排序：',
    print sort.cardinality_sort()
