class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ret = []
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in ret:
                return False
            ret.append(n)
        return n == 1
