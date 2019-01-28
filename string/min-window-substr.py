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
        i = j = 0
        matchedCount = 0
        minWin = len(st) + 1

        while(True):
            # move the right pointer of the window

            while matchedCount < len(t) and j < len(st):
                if st[j] in ht and ht[st[j]] > 0:
                    matchedCount += 1
                    ht[st[j]] -= 1
                j += 1
            # import pdb; pdb.set_trace()
            if matchedCount == len(t):
                matchedCount = 0
                ht = collections.Counter(t)
                while i < j and matchedCount < len(t):
                    if st[i] in ht and ht[st[i]] > 0:
                        i += 1
                        ht[st[i]] -= 1
                    else:
                        break
                if (j - i) < minWin:
                    minWin = j - i
                print(st[i:j])
                ht = collections.Counter(t)
                i = j
                matchedCount = 0
            else:
                break

if __name__ == "__main__":
    s = Solution()
    s.minWindow("ADOBECODEBANC", "ABC")
