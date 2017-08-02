# Two Sum
class Solution(object):
    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicts = {}
        for i, v in enumerate(nums):
            if (target - v) in dicts:
                return [dicts[target-v][1], i]
            dicts[v] = (target-v, i)

