"""
301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""
from collections import deque
class AnsNode:
    def __init__(self):
        self.ans = {}

    def add(self, count, ans):
        if count in self.ans:
            self.ans[count].add(ans)
        else:
            self.ans[count] = {ans}

class Solution:
    def __init__(self):
        self.ans = AnsNode()

    def checkValid(self, s):
        stack = []
        for i,e in enumerate(s):
            if e == '(':
                stack.append(e)
            elif e == ')':
                if not stack or stack[-1] != '(':
                    return False
                else:
                    _ = stack.pop()
            else:
                continue
        return True

    def isValid(self, s):
        count = 0
        for i, e in enumerate(s):
            if e == '(':
                count += 1
            elif e == ')':
                if count == 0:
                    return False
                else:
                    count -= 1
            else:
                continue
        return count == 0

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        que = deque()
        que.append(s)
        visited = {}
        valid = []
        import pdb;pdb.set_trace()
        while(que):
            cur = que.popleft()
            if cur not in visited:
                visited[cur] = 1
                if self.isValid(cur):
                    valid.append(cur)
                    continue
                for i in range(len(cur)):
                    p = s[0:i] + s[i+1:len(s)]
                    print(p)
                    que.append(p)
        return valid

if __name__ == "__main__":
    s = Solution()
    # print(s.removeInvalidParentheses("()())()"))
    print(s.removeInvalidParentheses(")("))
