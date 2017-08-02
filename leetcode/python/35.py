class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        tmp = 0
        for k, v in enumerate(nums):
            if v >= target:
                return k
            tmp = k
        return tmp + 1

