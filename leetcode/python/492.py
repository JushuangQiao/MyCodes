class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        from math import sqrt
        if int(sqrt(area))**2 == area:
            return [int(sqrt(area))]*2
        w = int(sqrt(area))
        while area%w != 0:
            w -= 1
        return [area/w, w]
