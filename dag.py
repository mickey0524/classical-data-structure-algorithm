#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: mickey0524
# 判断一个graph是否为DAG(有向无环图)
# 2018-09-27


def is_dag_dfs(graph):
    """
    type graph: list[list] 图
    rtype: bool 是否为DAG
    """
    length = len(graph)

    is_visited = [[False] * length, None]
    begin_with = [[False] * length]

    def resursive(idx):
        if is_visited[1] is not None:
            return
        if is_visited[0][idx] == True:
            is_visited[1] = False
            return
        is_visited[0][idx] = True
        begin_with[0][idx] = True
        for i in xrange(len(graph[idx])):
            if graph[idx][i] == 1:
                resursive(i)
                is_visited[0][i] = False

    for i in xrange(length):
        if not begin_with[0][i] and is_visited[1] is None:
            is_visited[0] = [False] * length
            resursive(i)

    return True if is_visited[1] is None else False


def is_dag_topo(graph):
    """
    type graph: list[list] 图
    rtype: bool 是否为DAG
    """
    length = len(graph)
    nodes = [i for i in xrange(length)]

    for _ in xrange(length - 1):
        zero_indegree_node = False
        for i in nodes:
            edge_found = False
            for j in nodes:
                if graph[j][i] == 1:
                    edge_found = True
                    break
            if not edge_found:
                nodes.remove(i)
                zero_indegree_node = True
                break

        if not zero_indegree_node:
            return False

    return True


if __name__ == '__main__':
    graph1 = [
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
    ]
    dfs_res = is_dag_dfs(graph1)
    print 'graph1-dfs得到的结果为:',
    if dfs_res:
        print '无环'
    else:
        print '有环'
    topo_res = is_dag_topo(graph1)
    print 'graph1-topo得到的结果为:',
    if topo_res:
        print '无环'
    else:
        print '有环'
    graph2 = [
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0],
    ]
    dfs_res = is_dag_dfs(graph2)
    print 'graph2-dfs得到的结果为:',
    if dfs_res:
        print '无环'
    else:
        print '有环'
    topo_res = is_dag_topo(graph2)
    print 'graph2-topo得到的结果为:',
    if topo_res:
        print '无环'
    else:
        print '有环'
