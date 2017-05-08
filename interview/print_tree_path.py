# coding:utf-8
# 使用python实现linux下的tree命令
# 思路：递归
# 思路：使用栈（列表）


class BinTree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(root, sta):
    print sta
    if root and root.left:
        sta.append(root.left.value)
        dfs(root.left, sta)
    if root and root.right:
        sta.append(root.right.value)
        dfs(root.right, sta)
    sta.pop()


def print_tree(root):
    if not root:
        return None
    sta = [root.value]
    dfs(root, sta)
