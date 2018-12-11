"""
Problem
--------
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
--------
Looked at the explanation, it says stack and greedy
Looked for some hints and this is what i came up with:
1. Scan `num` from left to right.
2. for i in num,
  i. if push num[i] > stack.top elem:
       if num[i] == 0:
           pop stack.
       else:
           push num on stack
     else:
         continue.


"""

class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for n in num:
            print("processing " + n)
            if not stack:
                print("adding " + n)
                stack.append(n)
            else:
                while k >0 and int(stack[-1][0]) > int(n):
                    #_ = stack.pop()
                    print("popping " + stack.pop())
                    k -= 1
                stack.append(n)
        print (stack)

if __name__ == '__main__':
    s = Solution()
    s.removeKdigits("10200", 2)
