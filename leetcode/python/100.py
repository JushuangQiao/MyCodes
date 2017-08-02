# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        left = right = True
        if (p and q) and (p.val == q.val):
            if p.left and q.left:
                left = self.isSameTree(p.left, q.left)
            else:
                left = not p.left and not q.left
            if p.right and q.right:
                right = self.isSameTree(p.right, q.right)
            else:
                right = not p.right and not q.right
        else:
            return not p and not q
        return left and right
