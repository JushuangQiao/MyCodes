class Solution(object):
    def findLeft(self, nums, target, leng):
        left, right = 0, leng - 1
        while left <= right:
            mid = (left + right) / 2
            if mid > 0 and nums[mid] == target and nums[mid - 1] < target:
                return mid
            if mid == 0 and nums[mid] == target:
                return mid
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def findRight(self, nums, target, leng):
        left, right = 0, leng - 1
        while left <= right:
            mid = (left + right) / 2
            if mid < leng - 1 and nums[mid] == target and nums[mid + 1] > target:
                return mid
            if mid == leng - 1 and nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leng = len(nums)
        return [self.findLeft(nums, target, leng), self.findRight(nums, target, leng)]
