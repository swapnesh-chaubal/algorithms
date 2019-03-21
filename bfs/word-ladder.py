"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
"""
import collections
import string

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        """
        Word Ladder 2
        https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer
        """
        
        que = collections.deque()
        
        steps = 0
        path = [beginWord]
        que.append((beginWord, steps, path))
        while que:
            curr, steps, path = que.popleft()
            if curr == endWord:
                print("found in %s steps"%(steps))
                print(path)
                return steps
            for i in range(len(curr)):
                for c in string.ascii_lowercase:
                    newWord = curr[:i] + chr(c) + curr[i+1:]
                    if newWord in wordList:
                        # print(newWord)
                        que.append((newWord, steps + 1, path.append(newWord)))

        return 0
if __name__ == '__main__':
    s = Solution()
    s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
