"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

 123
 456
"""
import collections
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        ans_stack = collections.deque()
        rev1 = num1[::-1]
        rev2 = num2[::-1]
        # if len(num1) >= len(num2):
        #     rev1 = num1[::-1]
        #     rev2 = num2[::-1]
        # else:
        #     rev1 = num2[::-1]
        #     rev2 = num1[::-1]

        n1_multiplier = 1
        n1_ans = 0
        for i, n1 in enumerate(rev2):
            n2_multiplier = 1
            n2_ans = 0
            for j, n2 in enumerate(rev1):
                p = int(n1) * int(n2) + carry
                if p >= 10:
                    carry = int(p/10)
                else:
                    carry = 0
                n2_ans += (p%10) * n2_multiplier
                n2_multiplier *= 10
            n2_ans += carry * n2_multiplier
            carry = 0
            ans_stack.append(n2_ans)

        m = 1
        s = 0

        while ans_stack:
            s += ans_stack.popleft() * m
            m *= 10
        return str(s)

if __name__ == "__main__":
    s = Solution()
    print(s.multiply("99","9"))
