"""
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
"""
Thinking
1. This problem is actually not that hard. Its a typical 2 pointer one.
2. Start both pointers from 0.
3. Move the right pointer to until all the elements required to are in the window.
4. Move the left pointer and see if it can be moved.
5. Check the size of this window.
6. Now move the right window again. Keep on doing this until you reach the end.
"""
import collections
class Solution:
    def minWindow(self, st, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ht = collections.Counter(t)
        start = end = 0
        matchNeeded = len(t)
        minWindow = -1
        minWindowStart = 0
        while end < len(st):
            if ht.get(st[end], 0) > 0:
                ht[st[end]] -= 1
                matchNeeded -= 1
            while matchNeeded == 0:
                currWindow = end - start + 1
                if minWindow == -1 or currWindow < minWindow:
                    minWindow = currWindow
                    minWindowStart = start
                
                if ht[st[start]] >= 0:
                    ht[start] += 1
                    matchNeeded +=1
                start += 1
            end += 1

        print(end)
        return st[minWindowStart:minWindow]

if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
