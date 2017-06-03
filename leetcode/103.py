# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        queue = [root]
        flag = 0
        while queue:
            if not flag:
                ret.append([node.val for node in queue])
                flag = 1
            else:
                ret.append([node.val for node in queue[::-1]])
                flag = 0
            next = [(node.left, node.right) for node in queue]
            queue = [node for child in next for node in child if node]
        return ret