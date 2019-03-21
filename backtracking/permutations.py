"""

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
import copy
import collections

class Solution:
    def __int__(self):
        self.permutations = []

    def backtrackIterative(self, nums):
        # NOT WORKING YET
        que = collections.deque()
        result = []
        if len(nums) == 0:
            return result
        import pdb; pdb.set_trace()
        for i in range(len(nums)):
            que.append([nums[i]])
            while que:
                perm = que.popleft()
                for j in range(i + 1, len(nums)):
                    word =  perm.append(nums[j]).append()
                    que.append(word)
                    print(que)
                

    def backtrack(self, result, tempList, nums):
        for i in range(len(tempList)):
            print(" "),
        print("backtrack(%s)"%(tempList))
        if len(tempList) == len(nums):
            if len(tempList) > 0:
                result.append(copy.copy(tempList))
        else:
            for i in range(0, len(nums)):
                if nums[i] in tempList:
                    continue
                tempList.append(nums[i])
                self.backtrack(result, tempList, nums)
                tempList.remove(tempList[-1])

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        self.backtrack(result, [], nums)
        print(result)


if __name__ == '__main__':
    s = Solution()
    s.permute([1,2, 3])
    # s.backtrackIterative([1,2, 3])
