class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        while len(s) != 1:
            s = str(sum([int(i) for i in s]))
        return int(s)
        '''if num == 0:
            return 0
        return num % 9 if num % 9 !=0 else 9'''
