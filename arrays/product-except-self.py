"""
238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

"""
I didn't have a clue of how this is done. Had to look at the solution.
There are two keys here.
1. Can the array from both directions
2. The second and most cruital thing is when scanning from the left, to only get
product of the elements to the left of the current element
3. Similarly when scanning from the right, get all the product of the elements to
the right of the current element.
[1, 2, 3, 4]

"""
class Solution:
    def withExtraSpace(self, nums):
        if not nums or len(nums) == 0:
            return 0
        leftProduct = [1 for i in range(len(nums))]
        mul = 1
        for i in range(1, len(nums)):
            mul = mul * nums[i-1]
            leftProduct[i] = mul

        rightProduct = [1 for i in range(len(nums))]
        mul = 1
        # Start from the second last element
        for i in range(len(nums) - 2, -1, -1):
            mul = mul * nums[i+1]
            rightProduct[i] = mul
        product = []
        for i in range(len(nums)):
            product.append(leftProduct[i] * rightProduct[i])
        return product

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return 0
        product = [1 for i in range(len(nums))]
        mul = 1
        for i in range(1, len(nums)):
            mul = mul * nums[i-1]
            product[i] = mul
        mul = 1
        for i in range(len(nums) - 2, -1, -1):
            mul = mul * nums[i+1]
            product[i] = mul * product[i]
        return product
        print(product)

if __name__ == "__main__":
    s = Solution()
    s.productExceptSelf([1, 2, 3, 4])
