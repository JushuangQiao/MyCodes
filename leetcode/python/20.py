class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ret = []
        for i in s:
            if i in ['[', '{', '(']:
                ret.append(i)
            else:
                if ret and {']':'[', ')':'(', '}':'{'}[i] == ret[-1]:
                    ret.pop()
                else:
                    return False
        return not ret
