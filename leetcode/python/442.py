class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c = Counter(nums)
        return [i[0] for i in c.most_common() if i[1] > 1]

