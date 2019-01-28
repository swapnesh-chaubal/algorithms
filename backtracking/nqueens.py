"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
class Solution:
    def isSafeToKeep(self, board, row, col, n):
        for r in range(n):
            for c in range(n):
                if board[r][c] == 'Q' and (row == r or col == c or row + r == col + c):
                    return False
            return True

    def solveNQueensHelper(self, board, row, col, n):
        if col == n:
            # print chessboard

        for r in range(n):
            if self.isSafeToKeep(board, r, c, n):
                board[r][c] = 'Q'
                solveNQueensHelper(board, r, c + 1, n)
                board[r][c] = '.'

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.' for x in range(n)] for y in range(n)]
        self.solveNQueensHelper(board, 0, 0)
