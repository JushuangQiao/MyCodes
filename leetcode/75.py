class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red, white, blue, leng = 0, 0, 0, 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1
            leng += 1
        while leng > 0:
            leng -= 1
            while blue:
                nums[leng] = 2
                leng -= 1
                blue -= 1
            while white:
                nums[leng] = 1
                leng -= 1
                white -= 1
            while red:
                nums[leng] = 0
                leng -= 1
                red -= 1
