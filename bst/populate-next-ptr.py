"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections
"""
Something for ref just in case:
https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/114449/A-general-approach-to-level-order-traversal-questions-in-Java
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        que = collections.deque()
        que.append(root)
        que.append(None)
        
        while que:
            curr = que.popleft()
            if curr == None:
                if len(que) > 0: que.append(None)
            else:
                curr.next = que[0]
                if curr.left: que.append(curr.left)
                if curr.right: que.append(curr.right)
