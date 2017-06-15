# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ret = [0]
        def dfs(root, ret, sum):
            if not root:
                return False
            ret.append(ret[-1] + root.val)
            if not root.left and not root.right:
                return ret.pop() == sum
            left = dfs(root.left, ret, sum)
            right = dfs(root.right, ret, sum)
            ret.pop()
            return left or right
        return dfs(root, ret, sum)

