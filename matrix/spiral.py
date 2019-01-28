"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rowsTop = 0
        rowsBottom = len(matrix)
        colsLeft = 0
        colsRight = len(matrix[0])

        # can be right, left, top, down
        direction = 'right'
        e = len(matrix[0]) * len(matrix)
        while(e > 0):
            if direction == "right":
                row = rowsTop
                col = colsLeft
                while(col < colsRight):
                    print(matrix[row][col])
                    e -= 1
                    col += 1
                direction = "down"
                rowsTop += 1
            elif direction == "down":
                row = rowsTop
                col = colsRight - 1
                while(row < rowsBottom):
                    print(matrix[row][col])
                    e -= 1
                    row += 1
                direction = "left"
                colsRight -= 1
            elif direction == "left":
                row = rowsBottom - 1
                col = colsRight - 1
                # import pdb; pdb.set_trace()
                while(col >= colsLeft):
                    print(matrix[row][col])
                    e -= 1
                    col -= 1
                direction = "up"
                rowsBottom -= 1
            elif direction == "up":
                row = rowsBottom - 1
                col = colsLeft
                while(row > rowsTop):
                    print(matrix[row][col])
                    e -= 1
                    row += 1
                direction = "right"
                colsRight -= 1

if __name__ == '__main__':
    s = Solution()
    s.spiralOrder([
      [1, 2, 3, 4, -1, -2, -3, -4],
      [5, 6, 7, 8, -5, -6, -7, -8],
      [9,10,11,12, -9,-10,-11,-12,],
      [50, 60, 70, 80, -50, -60, -70, -80]
    ])
