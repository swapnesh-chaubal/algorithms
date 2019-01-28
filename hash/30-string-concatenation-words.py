"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""
"""
Thinking
1. make a hash table with first letter as the key.
2. Make hash table with word and count. The count has to be the same for all the
words to be in the same iteration
3. You can iterate from 0 to sum(len of all words)

"""
from functools import reduce
from operator import add

class Solution:
    def findSubstring(self, sen, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        total = reduce(add, [len(w) for w in words])
        cHash = {}
        wordHash = {}
        for word in words:
            cHash[word[0]] = word
            wordHash[word] = 0
        currentCounter = 0
        i = 0
        wordsRemaining = len(words)
        for i in range(total):
            start = i
            # import pdb;pdb.set_trace()
            # print(s[start])
            while start < len(sen):
                # import pdb;pdb.set_trace()
                c = sen[start]
                print(c)
                if c in cHash:
                    # import pdb;pdb.set_trace()
                    word = cHash[c]
                    end = start + len(word)
                    if sen[start:end] == word and wordHash[word] == 0:
                        print(word)
                        wordHash[word] = 1  # now word is taken
                        wordsRemaining -= 1
                        if wordsRemaining == 0:
                            # we used all the words
                            print(i)
                            for word in words:
                                wordHash[word] = 0
                        start = end
                    else:
                        break
                else:
                    break

if __name__ == "__main__":
    s = Solution()
    # print(s.removeInvalidParentheses("()())()"))
    print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))
