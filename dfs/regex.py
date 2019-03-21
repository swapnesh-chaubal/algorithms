"""
10. Regular Expression Matching
"""
import collections

class Solution:
    def isMatchDp(self, s, p):
        dp = [[False] for range in (len(p) + 1)] for range in (len(s) + 1)]
        for i in range(len(s) + 1)):
            dp[0][i] = True
        for i in range(len(s) + 1)):
            dp[i][0] = True
        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j]:
                    dp[i][j] = dp[i-1][j-1]
                if p[j] == "*":
                    dp[i][j] = dp[i][j - 2]
                if p[j] == ".":


        return dp[len(s)][len(s)]
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        que = collections.deque()
        que.append(p)
        visited = {}
        # import pdb;pdb.set_trace()
        while que:
            cur = que.popleft()
            if cur in visited:
                continue
            if cur == s:
                return True
            visited[cur] = 1
            for i in range(len(cur)):
                if cur[i] == "*":
                    word = cur[0:i - 1] + cur[i:len(cur)]
                    print(word)
                    que.append(word)
                    for c in range(ord('a'), ord('z') + 1):
                        word = cur[0:i] + chr(c) + cur[i + 1: len(cur)]
                        print(word)
                        que.append(word)
                elif cur[i] == ".":
                    for c in range(ord('a'), ord('z') + 1):
                        word = cur[0:i] + chr(c) + cur[i + 1: len(cur)]
                        print(word)
                        que.append(word)
        return False

if __name__ == "__main__":
    s = Solution()


    print(s.isMatch("mississippi", "mis*is*p*."))
