"""

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

"""
Solution:
https://leetcode.com/problems/decode-ways/discuss/30451/Evolve-from-recursion-to-dp
"""

class Solution:

    def numDecodingsHelperTLE(self, s):
        if len(s) == 0:
            return 1
        if int(s[0]) > 0 and int(s[0]) <= 26:
            ways = self.numDecodingsHelperTLE(s[1:len(s)])
        else:
            return 0
        if len(s) >=2:
            if (int(s[0]) <= 26 and int(s[0]) > 0) and (int(s[:2]) <= 26 and int(s[:2]) > 0):
                ways += self.numDecodingsHelperTLE(s[2:len(s)])
        return  ways

    def numDecodingsHelperMemo(self, i, s, mem):
        if len(s) == 0:
            return 1
        if mem[i] > -1:
            return mem[i]
        if int(s[0]) > 0 and int(s[0]) <= 26:
            ways = self.numDecodingsHelperMemo(i + 1, s[1:len(s)], mem)
            mem[i] = ways
        else:
            mem[i] = 0
            return 0
        if len(s) >=2:
            if (int(s[0]) <= 26 and int(s[0]) > 0) and (int(s[:2]) <= 26 and int(s[:2]) > 0):
                ways += self.numDecodingsHelperMemo(i + 2, s[2:len(s)], mem)
        mem[i] = ways
        return ways

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = [-1 for i in range(len(s) + 1)]
        return self.numDecodingsHelperMemo(0, s, mem) # This works
        # return self.numDecodingsHelperTLE(s)
        

if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('226'))
11