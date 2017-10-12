# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        ret = 0
        left, right = deque(), deque()
        if root and root.left:
            left.append(root.left)
        if root and root.right:
            right.append(root.right)
        while left or right:
            while left:
                top = left.popleft()
                if not top.left and not top.right:
                    ret += top.val
                if top.left:
                    left.append(top.left)
                if top.right:
                    right.append(top.right)
            while right:
                top = right.popleft()
                if top.left:
                    left.append(top.left)
                if top.right:
                    right.append(top.right)
        return ret
