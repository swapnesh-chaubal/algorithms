"""
34. Find First and Last Position of Element in Sorted Array
Medium

1317

70

Favorite

Share
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        h = len(nums) - 1
        # first find the target using regular binary search
        pos = None
        import pdb;pdb.set_trace()
        while l <= h:
            m  = int(l + (h - l) / 2)
            if target == nums[m]:
                pos = m
            elif target < nums[m]:
                h = m - 1
            else:
                l = m + 1

        if not pos:
            return None
        # search left
        l = 0
        h = pos
        start = None
        while l <= h:
            m  = int(l + (h - l) / 2)
            if target < nums[m]:
                h = m - 1
            else:
                l = m + 1
        start = l 
        
        # search right
        l = pos
        h = len(nums) - 1
        end = None
        while l <= h:
            m  = l + (h - l) / 2
            if target < nums[m]:
                h = m - 1
            else:
                l = m + 1
        end = h
        return [start, end]

if __name__ == "__main__":
    s = Solution()
    s.searchRange([5,7,7,8,8,10], 8)