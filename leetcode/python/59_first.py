class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[1]*n for _ in range(n)]
        start, end = 0, n
        value = 1
        while start*2 < n:
            value = self.get_circle(ret, start, end, value)
            start += 1
            end -= 1
        return ret

    def get_circle(self, ret, start, end, value):
        # left->right
        move =start
        for i in range(value, value+end-start):
            ret[start][move] = i
            move += 1
        value += (end - start)
        if end-start > 1:
            # top->bottom
            move = start + 1
            for i in range(value, value+end-start-1):
                ret[move][end-1] = i
                move += 1
            value += (end - start - 1)
            # right->left
            move = end - 2
            for i in range(value, value+end-start-1):
                ret[end-1][move] = i
                move -= 1
            value += (end - start - 1)
            # bottom->top
            move = end - 2
            for i in range(value, value+end-start-2):
                ret[move][start] = i
                move -= 1
            value += (end - start - 2)
        return value
