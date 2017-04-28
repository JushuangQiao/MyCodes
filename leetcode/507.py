class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # from math import sqrt
        ret = 1
        if num <= 3:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                ret += i
                ret += (num / i)
            if ret > num:
                return False
        return num == ret
