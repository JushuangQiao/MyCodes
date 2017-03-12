class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        r = [[1 for i in range(n)] for j in range(m)]
        # r = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                r[i][j] = r[i-1][j] + r[i][j-1]
        return r[-1][-1]

