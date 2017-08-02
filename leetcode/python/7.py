class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = int(str(x)[::-1]) if x >= 0 else -int(str(abs(x))[::-1])
        return ret if abs(ret) < 2147483648 else 0
