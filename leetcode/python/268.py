class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''nums.sort()
        for k, v in enumerate(nums):
            if k != v:
                return k
        return len(nums)'''
        n = len(nums)
        return n * (n+1) / 2 -sum(nums)
