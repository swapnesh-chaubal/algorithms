class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        print("created tree")

    def insert(self, data):
        self.root= self._insert(self.root, data)
        return self.root
       
    def _insert(self, c_root, data):
        if c_root == None:
            print("adding node %s"%data)
            c_root = BTNode(data)
            return c_root

        if data < c_root.data:
            print("%s is < %s, going left"%(data, c_root.data))
            
            c_root.left = self._insert(c_root.left, data)
        else:
            print("%s is >= %s, going right"%(data, c_root.data))
            c_root.right = self._insert(c_root.right, data)
        return c_root

    def print_inorder_r(self):
        self._print_inorder_r(self.root)

    def _print_inorder_r(self, c_root):
        if c_root == None:
            return
        self._print_inorder_r(c_root.left)
        print(c_root.data)
        self._print_inorder_r(c_root.right)
            
