# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (not root.left and not root.right):
            return True
        if not root.left or not root.right:
            return False
        queue = [root.left, root.right]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if left.val == right.val:
                ll, lr, rl, rr = left.left, left.right, right.left, right.right
                if (not ll and rr) or (ll and not rr) or (rl and not lr) or (not rl and lr):
                    return False
                if ll and rr:
                    queue.append(ll)
                    queue.append(rr)
                if lr and rl:
                    queue.append(lr)
                    queue.append(rl)
            else:
                return False
        return True
