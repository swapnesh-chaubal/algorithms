# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def serializeH(root, s):
            if root is None:
                s += "None"
            else:
                s += str(root.val) + ","
                s = serializeH(root.left, s)
                s = serializeH(root.right, s)
            return s
        # import pdb; pdb.set_trace()
        s = serializeH(root, "")
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserializeH(root, s):
            # s is a list
            if s[0] is None:
                # remove the element from the list
                s.pop(0)
                # set the leaf
                return None

            root = TreeNode(s.pop(0))
            root.left = deserializeH(root, s)
            root.right = deserialize(root, r)
        root = deserializeH(data.split(","))


    def serializeIterative(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # import pdb; pdb.set_trace()
        stack = []
        cur = root
        s = ""
        while stack or cur:
            while(cur):
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur is None:
                s += "None"
                continue
            else:
                s += str(cur.val) + ","
                cur = cur.right
        return s

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__=="__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    right = TreeNode(4)
    right.left = TreeNode(1)
    right.right = TreeNode(6)
    root.right = right

    s = Codec()
    print(s.serialize(root))
    print(s.serializeIterative(root))
