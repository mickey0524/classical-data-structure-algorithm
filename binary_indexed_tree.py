# coding: utf-8
# 树形数组，可以用于高效处理对一个存储数字的列表进行更新及求前缀和
# 2019-03-01


class BinaryIndexedTree(object):

    def __init__(self, nums):
        length = len(nums)
        tree_arr = [0] * (length + 1)

        for i, n in enumerate(nums):
            tree_arr[i + 1] = n

        for i in xrange(1, length + 1):
            j = i + (i & -i)
            if j <= length:
                tree_arr[j] += tree_arr[i]

        self.tree_arr = tree_arr
        self.nums = nums

    def update(self, i, n):
        delta = self.nums[i] - n
        self.nums[i] = n

        i += 1
        length = len(self.tree_arr)

        while i < length:
            self.tree_arr[i] += delta
            i = i + (i & -i)

    def prefix_sum(self, i):
        res = 0
        i += 1

        while i > 0:
            res += self.tree_arr[i]
            i = i - (i & -i)

        return res

    def range_sum(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i - 1)


if __name__ == '__main__':
    binary_indexed_tree = BinaryIndexedTree([1, 4, 5, 2, 5, 5])
    print binary_indexed_tree.prefix_sum(1)
    print binary_indexed_tree.range_sum(1, 5)
