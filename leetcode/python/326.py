class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
	# 3**19 < 2**31-1 < 3**20
        return n > 0 and 3**19 % n == 0
