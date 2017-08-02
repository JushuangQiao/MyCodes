class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tmp = 1
        ret = []
        for i in digits[::-1]:
            ret.append((tmp+i)%10)
            tmp = (tmp+i) / 10
        if tmp != 0:
            ret.append(tmp)
        return ret[::-1]
