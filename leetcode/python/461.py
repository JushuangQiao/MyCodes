class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        '''ret = 0
        x, y = bin(x)[2:].zfill(32), bin(y)[2:].zfill(32)
        for i in xrange(32):
            if x[i] != y[i]:
                ret += 1
        return ret'''
        return bin(x^y).count('1')
        
