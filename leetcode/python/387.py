class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        loc = {}
        nums = {}
        for k, v in enumerate(s):
            nums[v] = nums[v] + 1 if nums.get(v) else 1
            loc[v] = loc[v] if loc.get(v) else k
        one = [c for c in nums if nums[c] == 1]
        ret = [loc[c] for c in one]
        if ret:
            return min(ret)
        return -1
