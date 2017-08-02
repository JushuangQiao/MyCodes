class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        return (bin(num).count('0') - 1) % 2 == 0 and bin(num).count('1') == 1
