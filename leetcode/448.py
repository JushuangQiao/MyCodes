class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for v in nums:
            t = abs(v) - 1
            if nums[t] > 0:
                nums[t] = -nums[t]
        return [k+1 for k, v in enumerate(nums) if v > 0]
