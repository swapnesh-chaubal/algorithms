class Solution:
    def uniquePathsDP(self, m, n, grid):
        for i in range(0, m):
            grid[i][0] = 1
        for i in range(0, n):
            grid[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[m-1][n-1]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[0 for x in range(n)] for y in range(m)]
        # print(self.uniquePathsHelper(0, 0, m, n, grid, 0))
        print(self.uniquePathsDP(m, n, grid))

if __name__ == "__main__":
    s = Solution()

    s.uniquePaths(4, 4)
