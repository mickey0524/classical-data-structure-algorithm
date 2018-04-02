#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: mickey0524
# Dijkstra, Floyd求最短路径
# 2018-04-02

# Dijkstra的核心思想是“松弛”，其实也有一些dp的思想，具体来说
# 就是根据当前点的最短路径去更新之前的最短路径
def dijkstra(graph, p):
  """
  type graph: list[list] 代表图的矩阵
  type p: int 基准点
  rtype: list
  """
  distance = graph[p][:]
  length = len(distance)
  is_visited = [False] * length
  is_visited[p] = True

  for _ in xrange(length - 1):
    cnt_min_index, cnt_min = None, float('inf')
    for i in xrange(length):
      if not is_visited[i] and distance[i] < cnt_min:
        cnt_min = distance[i]
        cnt_min_index = i
    is_visited[cnt_min_index] = True
    for i in xrange(length):
      tmp_dis = cnt_min + graph[cnt_min_index][i]
      if not is_visited[i] and distance[i] > tmp_dis:
        distance[i] = tmp_dis

  return distance


# Floyd的核心思想是依次允许遍历不同的节点
def floyd(graph):
  """
  type graph: list[list] 代表图的矩阵
  rtype: list[list]
  """
  length = len(graph)
  for i in xrange(length):
    for j in xrange(length):
      for k in xrange(length):
        if graph[j][i] + graph[i][k] < graph[j][k]:
          graph[j][k] = graph[j][i] + graph[i][k]
  
  return graph

if __name__ == '__main__':
  graph = [
    [0, 1, 12, float('inf'), float('inf'), float('inf')],
    [float('inf'), 0, 9, 3, float('inf'), float('inf')],
    [float('inf'), float('inf'), 0, float('inf'), 5, float('inf')],
    [float('inf'), float('inf'), 4, 0, 13, 15],
    [float('inf'), float('inf'), float('inf'), float('inf'), 0, 4],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0]
  ]
  distance = dijkstra(graph, 0)
  print distance

  print floyd(graph)