# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(n) == 0:
            return n
        mid = n>>1
        low, high = 0, n
        while guess(mid) != 0:
            if guess(mid) == 1:
                low = mid
                mid = (mid + high)>>1
            else:
                high = mid
                mid = (low + mid)>>1
        return mid
