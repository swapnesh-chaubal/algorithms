"""
Perfect Squares


Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
import collections
import sys

class Solution(object):
    def numSquaresDP(self, n):
        dp = [0 for i in range(n +1)] 

        dp[0] = 0
        for i in range(1, n + 1):
            minimum = sys.maxsize
            for j in range(1, n):
                if j * j > n:
                    break
                dp[i] = min(minimum, dp[i - j * j] + 1)
        
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = []
        for i in range(1, n + 1):
            square = i * i
            if square > n:
                break
            squares.append(square)
        print(squares)
        que = collections.deque()
        steps = 0
        que.append(n)
        # import pdb;pdb.set_trace()
        while que:
            steps += 1
            queElements = len(que)
            for i in range(queElements):
                currSq = que[0]
                j = 1
                for sq in squares:
                    if currSq < sq:
                        break
                    rem = currSq - j * j
                    if rem == 0:
                        return
                    else:
                        que.append(rem)
        return steps

    # def numSquares(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     def bfs(results, curr, n, currentSum, squares):
    #         if currentSum == n:
    #             return "found"
    #         for sq in squares:
    #             if (curr, sq) not in results:
    #                 res = curr + sq
    #                 results[(curr, sq)] = res
    #                 bfs(results, res, n, currentSum + res, squares)
       
    #     squares = []
    #     for i in range(n):
    #         square = i * i
    #         if square > n:
    #             break
    #         squares.append(square)
        
        


if __name__ == '__main__':
    s = Solution()
    s.numSquares(7168)