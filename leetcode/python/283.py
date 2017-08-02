class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        import copy
        n = copy.deepcopy(nums)
        move = 0
        for i in n:
            if i != 0:
                nums[move] = i
                move += 1
        while move != len(n):
            nums[move] = 0
            move += 1
