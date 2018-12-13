"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
------
Didn't look for any hints on this one.
Think of the matrix as a long array. The only thing to calculate is the row and col
of the mid element
mid = int(low + (high - low)/2)
row = int(mid/cols)
col = int(mid%cols)

"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix) if matrix else -1
        cols = len(matrix[0]) if rows != -1 else -1
        if rows == -1 or cols == -1:
            return False
        low = 0
        high = rows * cols - 1
        print("rows %s, cols %s, high %s"%(rows, cols, high))
        while low <= high:
            mid = int(low + (high - low)/2)
            row = int(mid/cols)
            col = int(mid%cols)
            print("row %s, col %s, mid %s"%(row, col, mid))
            print("e %s"%(matrix[row][col]))
            if target == matrix[row][col]:
                print("foound")
                return True
            elif target < matrix[row][col]:
                # going left
                high = mid - 1
            else:
                #going right
                low = mid + 1
        return False

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    s.searchMatrix(matrix, 3)
