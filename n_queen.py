# coding: utf-8

from copy import copy


def n_queen(n):
    """
    n 皇后问题
    :param n: 皇后的数目
    :return:
    """
    state = [None] * n  # 索引代表行，数值代表该行的皇后位于哪一列

    res = [[], False]  # 记录结果

    def dfs(cur):
        """
        dfs
        :param cur: 当前行
        :return:
        """
        if res[1]:
            return

        if cur == n:
            res[0] = copy(state)
            res[1] = True
            return

        for i in xrange(n):
            state[cur] = i
            is_conflict = False
            for r in xrange(cur):
                if state[cur] == state[r] or cur - r == state[cur] - state[r] or \
                        cur + state[cur] == r + state[r]:
                    is_conflict = True
                    break
            if not is_conflict:
                dfs(cur + 1)

    dfs(0)

    return res[0]


def print_queue(state):
    """
    打印棋盘，皇后用 Q 标示
    :param state: 皇后分布
    :return:
    """
    length = len(state)
    for n in state:
        for i in xrange(length):
            if n == i:
                print 'Q',
            else:
                print '.',
        print '\n'


if __name__ == '__main__':
    print_queue(n_queen(8))
