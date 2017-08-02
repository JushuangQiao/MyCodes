class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for num in nums:
            if i<2 or nums[i-2]<num:
                nums[i] = num
                i += 1
        return i
        '''from collections import Counter
        a = Counter(nums)
        ret = []
        leng = 0
        for i in a.keys():
            if a[i] == 1:
                leng += 1
            if a[i] >= 2:
                leng += 2
                tmp = a[i]
                while tmp > 2:
                    nums.remove(i)
                    tmp -= 1
        return leng'''
