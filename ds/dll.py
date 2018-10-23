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
        return self.first

    def move_to_front(self, node):
        if self.first:
            nnext = node.next
            nprev = node.prev

            first = self.first

            self.first = node
            node.next = first
            node.prev = None
            first.prev = node

            nprev.next = nnext
            nnext.prev = nprev
        # self.first = node
        return self.first


    def delete_last(self):
        if self.last.prev:
            temp = self.last
            self.last = last.prev
            temp = None
        else:
            self.last = None

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
    