"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        curr = root
        stack = []
        prev = None
        while curr != None or stack:
            while curr != None:
                # print("appending %s to stack"%(curr.val))
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev and prev.val >= curr.val:
                return False
            print(curr.val)
            prev = curr
            curr = curr.right
        return True


if __name__=="__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    right = TreeNode(4)
    right.left = TreeNode(3)
    right.right = TreeNode(6)
    root.right = right

    s = Solution()
    print(s.isValidBST(root))
