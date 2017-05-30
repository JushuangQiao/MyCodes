# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrder(self, root, out):
        if not root:
            return
        if root.left:
            self.inOrder(root.left, out)
        out.append(root.val)
        if root.right:
            self.inOrder(root.right, out)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ret = []
        self.inOrder(root, ret)
        leng = len(ret)
        if leng <= 1:
            return True
        for i in xrange(1, leng):
            if ret[i - 1] >= ret[i]:
                return False
        return True
