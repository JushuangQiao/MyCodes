class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]
        '''d = {}
        leng = len(nums) / 2
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] > leng:
                return i'''
