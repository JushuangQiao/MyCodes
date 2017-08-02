class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = {}
        for i in nums:
            ret[i] = ret.get(i, 0) + 1
        for k in ret.keys():
            if ret[k] == 1:
                return k
