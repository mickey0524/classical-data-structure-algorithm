#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: mickey0524
# 并查集算法
# 2017-03-31


class UnionFind(object):
    def __init__(self, N):
        """
        初始化参数
        type N: int 点的个数
        """
        self.count = N
        self.id = [i for i in xrange(N)]
        self.size = [1] * N

    def get_count(self):
        """
        获取并查集中不同种类的点
        rtype: int
        """
        return self.count

    def _find(self, p):
        """
        查询id指代的节点的根节点
        type p: int 节点id
        rtype: int
        """
        if p != self.id[p]:
            self.id[p] = self._find(self.id[p])

        return self.id[p]

    def union(self, p, q):
        """
        在连通图中打通p节点和q节点
        type p: int 节点p
        type q: int 节点q
        """
        p_root, q_root = self._find(p), self._find(q)

        if p_root == q_root:
            return False

        if self.size[p_root] < self.size[q_root]:
            self.id[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else:
            self.id[q_root] = p_root
            self.size[p_root] += self.size[q_root]

        self.count -= 1

        return True


if __name__ == '__main__':
    uf = UnionFind(10)
    print uf.id, uf.count
    opearte = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1),
               (8, 9), (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]

    for p, q in opearte:
        uf.union(p, q)

    print uf.id, uf.count
