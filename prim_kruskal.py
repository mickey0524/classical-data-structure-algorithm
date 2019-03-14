#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: mickey0524
# prim 算法，得到最小生成树
# 2018-12-25


from union_find import UnionFind


def prim(graph, init_node):
    """
    prim 算法
    :param graph: 图
    :param init_node: 初始节点
    :return
    """
    length = len(graph)
    flag = [0] * length
    flag[init_node] = 1  # 1 代表处理过的节点
    distance = [w for w in graph[init_node]]  # deep copy
    res = 0

    for _ in xrange(length - 1):
        min_dis, min_idx = float('inf'), None
        for idx, n in enumerate(distance):
            if flag[idx] == 1:
                continue
            if n < min_dis:
                min_dis = n
                min_idx = idx
        if min_idx is None:
            raise Exception('It\'s not a connected graph')
        flag[min_idx] = 1
        res += min_dis
        for idx, n in enumerate(distance):
            if flag[idx] == 1:
                continue
            if graph[min_idx][idx] < distance[idx]:
                distance[idx] = graph[min_idx][idx]
                
    return res


def kruskal(graph):
    """
    kruskal 算法
    :param graph: 图
    """
    length = len(graph)
    uf = UnionFind(length)

    edges = []

    for i in xrange(length):
        for j in xrange(i + 1, length):
            if graph[i][j] < float('inf'):
                edges.append((graph[i][j], i, j))

    edges.sort()

    res = 0

    for e in edges:
        m, n = e[1], e[2]
        if uf.union(m, n):
            res += e[0]

    return res


if __name__ == "__main__":
    graph = [
        [float('inf'), 6, 1, 5, float('inf'), float('inf')],
        [6, float('inf'), 5, float('inf'), 3, float('inf')],
        [1, 5, float('inf'), 5, 6, 4],
        [5, float('inf'), 5, float('inf'), float('inf'), 2],
        [float('inf'), 3, 6, float('inf'), float('inf'), 6],
        [float('inf'), float('inf'), 4, 2, 6, float('inf')]
    ]

    for i in xrange(len(graph)):
        print prim(graph, i)

    print kruskal(graph)
