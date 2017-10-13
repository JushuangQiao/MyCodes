class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        move = 1
        for k, v in enumerate(nums):
            if k == 0:
                ret = move
                continue
            move = move + 1 if v > nums[k-1] else 1
            ret = move if move > ret else ret
        return ret

