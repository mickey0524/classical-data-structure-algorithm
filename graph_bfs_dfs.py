#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: mickey0524
# 图的bfs和dfs遍历
# 2018-04-01


from collections import deque


class Graph(object):
    def __init__(self, graph):
        """
        init
        type graph: list[list] 表示图连通的二维数组
        """
        self.graph = graph

    def bfs(self):
        """
        bfs遍历
        """

        def resursive(begin):
            """
            利用队列进行遍历
            :type begin: int 当前遍历的点
            """
            length = len(self.graph)
            queue = deque()
            queue.appendleft(begin)
            while len(queue) != 0:
                cnt_p = queue.pop()
                if is_visited[cnt_p]:
                    continue
                is_visited[cnt_p] = True
                print cnt_p,
                for i in xrange(length):
                    if self.graph[cnt_p][i] and not is_visited[i]:
                        queue.appendleft(i)

        length = len(self.graph)
        is_visited = [False] * length

        for i in xrange(length):
            if not is_visited[i]:
                resursive(i)

    def recursive_dfs(self):
        """
        递归dfs遍历
        """

        def resursive(begin):
            """
            遍历函数
            :type begin: int 当前遍历的点
            """
            length = len(self.graph)
            print begin,
            is_visited[begin] = True
            for i in xrange(length):
                if self.graph[begin][i] and not is_visited[i]:
                    resursive(i)

        length = len(self.graph)
        is_visited = [False] * length

        for i in xrange(length):
            if not is_visited[i]:
                resursive(i)

    def non_recursive_dfs(self):
        """
        非递归dfs遍历
        """

        def resursive(begin):
            """
            遍历函数
            :type begin: int 当前遍历的点
            """
            stack = deque()
            stack.append(begin)
            while len(stack) != 0:
                is_push = False
                cnt_p = stack[-1]
                if not is_visited[cnt_p]:
                    print cnt_p,
                    is_visited[cnt_p] = True
                for i in xrange(length):
                    if self.graph[cnt_p][i] == 1 and not is_visited[i]:
                        stack.append(i)
                        is_push = True
                        break
                if not is_push:
                    stack.pop()

        length = len(self.graph)
        is_visited = [False] * length

        for i in xrange(length):
            if not is_visited[i]:
                resursive(i)


if __name__ == '__main__':
    graphArr = [
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0]
    ]
    graph = Graph(graphArr)

    print 'bfs遍历: ',
    graph.bfs()
    print '\n递归dfs遍历: ',
    graph.recursive_dfs()
    print '\n非递归dfs遍历: ',
    graph.non_recursive_dfs()
