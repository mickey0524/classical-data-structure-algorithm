# coding: utf-8
# 树形数组，可以用于高效处理对一个存储数字的列表进行更新及求前缀和
# 2019-03-01
# n & -n 用于获取 n 的二进制表示中最右边的 1
# 在树状数组中，一个元素可能存储了前面多个元素的 sum
# 比如第二个元素存储了第一个和第二个的和，第四个存储了前四个的和
# 其实是按照二进制中尾部有多少个 0 来决定保存前几个的和
# 10 -> 1 个 0 -> 2 ** 1 = 2
# 100 -> 2 个 0 -> 2 ** 2 = 4
# 110 -> 1 个 0 -> 2 ** 1 = 2


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
        delta = n - self.nums[i]
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
