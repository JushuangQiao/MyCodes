class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret  = tmp = 0
        for i in nums:
            if i == 0:
                ret = ret if ret > tmp else tmp
                tmp = 0
            else:
                tmp += 1
        return ret if ret > tmp else tmp
