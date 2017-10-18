class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for k, v in enumerate(numbers):
            if (target - v) in dic:
                return [dic[target-v], k+1]
            dic[v] = k + 1

