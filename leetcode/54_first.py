# no pythonic
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        m, n = rows, cols
        start, ret = 0, []
        while start*2 < m and start*2 < n:
            self.get_ret(matrix, ret, start,  rows, cols)
            start += 1
            rows -= 1
            cols -= 1
        return ret

    def get_ret(self, raw, ret, start, rows, cols):
        # left->right
        for i in range(start, cols):
            ret.append(raw[start][i])
        # top->bottom
        if rows-start > 1:
            for i in xrange(start+1, rows):
                ret.append(raw[i][cols-1])
        # right->left
        if rows-start > 1 and cols-start > 1:
            for i in range(start, cols-1)[::-1]:
                ret.append(raw[rows-1][i])
        # bottom->top
        if rows-start > 1 and cols-start > 1:
            for i in range(start+1, rows-1)[::-1]:
                ret.append(raw[i][start])
