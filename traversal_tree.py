#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 作者: mickey0524
# 实现树的前序，中序，后序的递归与非递归遍历以及树的层次遍历
# 2018-03-25

from collections import deque

class TreeNode(object):

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class TraversalTree(object):

  def __init__(self, arr):
    self.arr = arr
    self.root = self._generate_tree(arr, 0)
  
  def _generate_tree(self, arr, cnt_index):
    """
    type arr: List 用于生成树的数组
    type cnt_index: int 当前节点数值的索引
    rtype: TreeNode
    """
    node = TreeNode(arr[cnt_index])
    left_index, right_index = cnt_index * 2 + 1, cnt_index * 2 + 2
    if left_index < len(arr):
      node.left = self._generate_tree(arr, left_index)
    else:
      node.left = None
    if right_index < len(arr):
      node.right = self._generate_tree(arr, right_index)
    else:
      node.right = None
    return node
    

  def recursive_preorder(self, node):
    """
    递归先序遍历
    type node: TreeNode 树的节点
    """
    if not node:
      return
    print node.val,
    self.recursive_preorder(node.left)
    self.recursive_preorder(node.right)

  def non_recursive_preorder(self, node):
    """
    非递归前序遍历
    type node: TreeNode 树的节点
    """
    stack = deque()
    if not node:
      return
    stack.append(node)
    while len(stack) != 0:
      node = stack.pop()
      print node.val,
      if node.right:
        stack.append(node.right)
      if node.left:
        stack.append(node.left)


  def recursive_inorder(self, node):
    """
    递归中序遍历
    type node: TreeNode 树的节点
    """
    if not node:
      return
    self.recursive_inorder(node.left)
    print node.val,
    self.recursive_inorder(node.right)
  
  def non_recursive_inorder(self, node):
    """
    非递归中序遍历
    type node: TreeNode 树的节点
    """

  def recursive_postorder(self, node):
    """
    递归后序遍历
    type node: TreeNode 树的节点
    """
    if not node:
      return
    self.recursive_postorder(node.left)
    self.recursive_postorder(node.right)
    print node.val,

  def non_recursive_postorder(self, node):
    """
    非递归后序遍历
    type node: TreeNode 树的节点
    """


  def level_traversal(self, node):
    """
    层次遍历
    type node: TreeNode 树的节点
    """
    if not node:
      return
    
    queue = deque()
    queue.append(node)
    while len(queue) != 0:
      node = queue.pop()
      print node.val,
      if node.left:
        queue.appendleft(node.left)
      if node.right:
        queue.appendleft(node.right)




if __name__ == '__main__':
  arr = [1, 4, 5, 2, 4, 7, 8, 9, 4, 5, 10]
  tree = TraversalTree(arr)

  print '递归前序遍历: ',
  tree.recursive_preorder(tree.root)
  print '\n非递归前序遍历: ',
  tree.non_recursive_preorder(tree.root)
  print '\n递归中序遍历: ',
  tree.recursive_inorder(tree.root)
  print '\n递归后序遍历: ',
  tree.recursive_postorder(tree.root)
  print '\n层次遍历: ',
  tree.level_traversal(tree.root)
