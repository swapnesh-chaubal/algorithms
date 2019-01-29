"""
17. Letter Combinations of a Phone Number.

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

import collections

class Solution:
    def __init__(self):
        self.numbers = {
            "0": "",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        self.permutations = []

    def helper(self, digits, i, cur):
        if i >= len(digits):
            self.permutations.append(cur)
            return
        letters = self.numbers[digits[i]]
        for l in letters:
            self.helper(digits, i + 1, cur + l)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        self.helper(digits, 0, "")
        print(self.permutations)
            
if __name__ == "__main__":
    s = Solution()
    s.letterCombinations("23")