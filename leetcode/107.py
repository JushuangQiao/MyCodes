# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        level = [(root,)]
        while level:
            val = [node.val for nodes in level for node in nodes if node]
            level = [(node.left, node.right) for nodes in level for node in nodes if node]
            if val:
                ret.append(val)
        return ret[::-1]
