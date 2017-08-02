class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l <= r:
            m = l + (r-l)/2
            if m**2 <= x < (m+1)**2:
                return m
            elif x < m**2:
                r = m
            else:
                l = m + 1
