"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
from collections import deque
class Solution:
    def isPalindrome(self, m):
        return m == m[::-1]

    def partitionHelper(self, s, visited):
        if s in visited:
            return
        if self.isPalindrome(s):
            return True
        if len(s) > 1:
            word1 = s[0:len(s)/2]
            word2 = s[len(s)/2+1:len(s)]

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        " this Works "
        def dfs(s, palidromes, res):
            if len(s) == 0:
                return res.append(palindromes)

            for i in range(1, len(s) + 1):
                if self.isPalindrome(s[:i]):
                    dfs(s[i:], res.append(s[:i]))

    def partitionIterative(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        "THis is not in the expected format"
        visited = {}
        que = deque()
        que.append(s)
        p = []
        while que:
            cur = que.popleft()
            print(cur)
            if cur in visited:
                continue
            else:
                visited[cur] = 1
            if self.isPalindrome(cur):
                p.append(cur)
            for i in range(1, len(cur)):
                que.append(cur[0:i])
                que.append(cur[i:len(cur)])
        print(p)

if __name__ == '__main__':
    s = Solution()
    s.partition("aab")
