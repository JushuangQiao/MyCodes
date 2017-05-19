class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return nums
        max_sum = tmp = nums[0]
        for num in nums[1:]:
            if num + tmp < num:
                tmp = num
            else:
                tmp += num
            max_sum = max(max_sum, tmp)
        return max_sum

