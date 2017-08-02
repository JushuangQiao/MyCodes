class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col, width= len(matrix)-1, 0, len(matrix[0])
        while row>=0 and col<width:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col = col + 1
            else:
                row = row - 1
        return False
