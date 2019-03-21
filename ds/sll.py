class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, data):
        if self.first == None:
            self.first = SLLNode(data)
            self.last = self.first
        else:
            temp = SLLNode(data)
            self.last.next = temp
            self.last = temp

    def print_list(self):
        curr = self.first
        while (curr != None):
            print(curr.data)
            curr = curr.next

    def reverse(self):
        last = self.last
        curr = self.first 
        # 1 -> 2 -> 3
        self.first = last
        import pdb;pdb.set_trace()
        while curr != last:
            cnext = curr.next  # 2
            lnext = last.next  # None
            last.next = curr   # 3 -> 1
            curr.next = lnext
            curr = cnext   # 2
            self.last = curr

