class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = [1 for num in nums]
        for num in nums:
            tmp[num-1] -= 1
        dul, loss = -1, -1
        for k, v in enumerate(tmp):
            if v == 1:
                loss = k + 1
            if v == -1:
                dul = k + 1
        if dul>=0 and loss>=0:
            return [dul, loss]
        return []
        
