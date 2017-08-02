class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 有待改进
        '''leng = len(nums)
        cou = nums.count(val)
        j = 0
        for i in range(leng):
            if nums[j] == val:
                nums.remove(nums[j])
                cou -= 1
                j -= 1
            j += 1
            if cou == 0:
                return len(nums)'''
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

