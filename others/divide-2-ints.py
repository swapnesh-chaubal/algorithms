"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

Thinking:
In the brute force form, this look like you can just subtract the divisor from the divident in a loop
"""
import time
class Tester:
    def test(self, fn, expected, *args):
        print("Testing with args: " + str(args))
        start = time.clock()
        actual = fn(*args)
        end = time.clock()
        print("Function took %s seconds"%(str(end-start)))
        print ("Expected: " + str(expected) + ", Actual: " + str(actual))
        assert expected == actual


class Solution(Tester):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        minus = 1
        quotient = 0
        if (dividend > 0 and divisor > 0):
            minus = 1
        if (dividend < 0 and divisor < 0):
            dividend *= -1
            divisor *= -1
        else:
            if dividend < 0:
                dividend *= -1
                minus = -1
            if divisor < 0:
                divisor *= -1
                minus = -1

        while dividend >= divisor:
            dividend = dividend - divisor
            quotient += 1
        return quotient * minus

if __name__ == '__main__':
    s = Solution()
    s.test(s.divide, 3, *(10, 3))
    s.test(s.divide, 10, *(10, 1))
    s.test(s.divide, -10, *(10, -1))
    # s.test(s.divide(10, 3), 3, {10, 3})
    # s.test(s.divide(7, -3), -2)
    # s.test(s.divide(0, -3), 0)
    # s.test(s.divide(50000, 12), 4166)
    # s.test(s.divide(1, 1), 1)
    # s.test(s.divide(1, 10), 0)
    # s.test(s.divide(10, 1), 10)
    # s.test(s.divide(-1, -1), 1)
    # s.test(s.divide(-1, 10), 0)
    # s.test(s.divide(10, -1), -10)
    # s.test(s.divide(-2147483648, -1), 2147483648, {-2147483648, -1})
