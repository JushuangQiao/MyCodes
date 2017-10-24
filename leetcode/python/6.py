class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = ['' for i in range(numRows)]
        move = 0
        counts = 0
        
        for c in s:
            if move == 0:
                rows[counts] += c
                counts += 1
                if counts == numRows:
                    move = 1
                    counts -= 2
            else:
                rows[counts] += c
                counts -= 1
                if counts < 0:
                    move = 0
                    counts += 2
        return ''.join(rows)
