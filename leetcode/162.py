class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for k, v in enumerate(nums[:-1]):
            if k != 0 and nums[k-1] < v and nums[k+1] < v:
                return k
        try:
            if nums[0] > nums[1]:
                return 0
            if nums[-1] > nums[-2]:
                return len(nums) - 1
        except:
            return 0
