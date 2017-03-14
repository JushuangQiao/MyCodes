class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        flag = 0
        ret = ''
        while s:
            if flag == 0:
                ret = ret + s[:k][::-1]
                flag = 1
            else:
                ret = ret + s[:k]
                flag = 0
            s = s[k:]
        return ret
