class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        ret = []
        for i in d:
            if d[i] == 1:
                ret.append(i)
        return ret
        '''
        from collections import Counter
        c = Counter(nums).most_common()[-2:]
        return [i[0] for i in c]
        '''
