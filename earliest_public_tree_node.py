#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: mickey0524
# 获取树两个节点的最早公共节点
# 2018-04-09


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


parent = None


def get_earliest_public_tree_node(node, left, right):
    """
    获取left和right节点的最近公共祖先
    type node: TreeNode 树节点
    type left: TreeNode 左节点
    type right: TreeNode 右节点
    """
    global parent
    if not node:
        return 0

    if parent:
        return 2

    left_val = get_earliest_public_tree_node(node.left, left, right)
    right_val = get_earliest_public_tree_node(node.right, left, right)
    cnt_node_val = 1 if node == left or node == right else 0

    if parent is None and left_val + right_val + cnt_node_val == 2:
        parent = node

    return left_val + right_val + cnt_node_val


if __name__ == '__main__':
    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node0.left = node1
    node0.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    get_earliest_public_tree_node(node0, node3, node1)
    print '最近公共祖先数组为：{num}'.format(num=parent.val)
