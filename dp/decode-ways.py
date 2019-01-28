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

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        w = [0] * len(s)
        if int(s[0]) <= 26 and int(s[0]) > 0:
            w[0] = 1
        else:
            w[0] = 0

        for i in range(1, len(s)):
            w[i] = w[i-1]
            n = int(s[i-1] + s[i])
            print("checking %s"%(n))
            if n <= 26 and n > 0 and int(s[i-1]) > 0:
                w[i] += 1
            # w[i] = w[i-1] + 1 if int(s[i] + s[i-1]) <= 26 else 0
        print(w)
        return w[len(s) - 1]

if __name__ == '__main__':
    s = Solution()
    s.numDecodings('12')
