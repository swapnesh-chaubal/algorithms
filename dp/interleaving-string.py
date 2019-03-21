"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        is len(s3) != len(s1) + len(s2):
            return False

        # lets have rows for s2 and
        # cols for s1
        dp = [[False for i in range(len(s1) + 1)] for i in range(len(s2) + 1)]
        # set col 0
        for i in range(len(s2)):
            dp[i][0] = True
        # set row 0
        for i in range(len(s1)):
            dp[0][i] = True

        for i in range(len(s2)):
            for j in range(len(s1)):
                if s2[i] == s1[j]:
                    dp[i][j] = dp[i - 1][j] &
            dp[i][j] = 1 + dp[i-]
