# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ret = []
        level = [root] if root else []
        while level:
            sum , len = 0, 0
            tmp = []
            for node in level:
                sum += node.val
                len += 1
                if node.right:
                    tmp.append(node.right)
                if node.left:
                    tmp.append(node.left)
            level = tmp
            ret.append(sum/(len*1.0))
        return ret
        
