class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        d = {}
        for i in s:
            d[i] = d[i] + 1 if i in d else 1
        ret = 0
        mod = 0
        for i in d:
            ret += d[i] if d[i] % 2 == 0 else d[i] - 1
            if d[i] % 2 != 0:
                mod = 1
        return ret + mod
            
