class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        k %= leng
        right = nums[-k:]
        while leng - k > 0:
            nums[leng-1] = nums[leng-k-1]
            leng -= 1
        while leng > 0:
            nums[leng-1] = right[leng-1]
            leng -= 1

