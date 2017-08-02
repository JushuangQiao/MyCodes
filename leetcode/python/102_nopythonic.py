# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        q1 = [root]
        q2 = []
        flag = 1
        while q1 or q2:
            tmp = []
            if flag == 1:
                while q1:
                    node = q1.pop(0)
                    tmp.append(node.val)
                    if node.left:
                        q2.append(node.left)
                    if node.right:
                        q2.append(node.right)
                flag = 2
            else:
                while q2:
                    node = q2.pop(0)
                    tmp.append(node.val)
                    if node.left:
                        q1.append(node.left)
                    if node.right:
                        q1.append(node.right)
                flag = 1
            ret.append(tmp)
        return ret