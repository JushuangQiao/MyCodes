class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # It's also nice to use set
        dict = {}
        for k, v in enumerate(nums):
            dict[v] = k
        return sorted(dict.keys())[-3] if len(dict.keys()) >= 3 else sorted(dict.keys())[-1]
