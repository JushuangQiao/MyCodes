class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        remainder = 2
        while n:
            if n % 2 == remainder:
                return False
            remainder = n % 2
            n /= 2
        return True

