class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        most = 0
        left = 0
        right = len(height) - 1
        while left < right:
            temp = (right - left) * min(height[left], height[right])
            most = most if most > temp else temp
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return most
