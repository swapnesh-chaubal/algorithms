"""

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        p = [0] * len(nums)
        p[0] = nums[0]
        max_p = p[0]
        for i in range(1, len(nums)):
            s = p[i-1] * nums[i]
            if s > p[i-1]:
                p[i] = s
            else:
                p[i] = nums[i]
            if p[i] > max_p:
                max_p = p[i]
        print(p)
        return max_p

if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([-2,0,-1]))
