class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.first = None
        self.last = None

    def insert_end(self, data):
        temp = DLLNode(data)
        if self.last:
            self.last.next = temp
            temp.prev = self.last
            self.last = temp
        else:
            # empty list
            self.first = temp
            self.last = temp
    
    def insert_start(self, data):
        temp = DLLNode(data)
        if self.first:
            self.first.prev = temp
            temp.next = self.first
            self.first = temp
        else:
            # empty list
            self.first = temp
            self.last = temp

    def print_list(self):
        curr = self.first
        while (curr != None):
            print(curr.data)
            curr = curr.next

    def print_rev(self):
        curr = self.last
        while (curr != None):
            print(curr.data)
            curr = curr.prev
    