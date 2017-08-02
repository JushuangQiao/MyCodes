class Solution(object):
    def getsub(self, tmp, len):
        ret = [1]
        for i in range(len - 1):
            ret.append(tmp[i] + tmp[i + 1])
        ret.append(1)
        return ret

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 可以使用map迭代，之后尝试
        ret = []
        if numRows <= 0:
            return ret
        ret += [1]
        for i in range(1, numRows):
            ret.append(self.getsub(ret[-1], i))
        return ret
