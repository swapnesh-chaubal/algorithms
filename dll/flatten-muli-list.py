"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.



Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
"""
import collections

# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    # def flattenHelper(self, head):
    #     curr = head
    #     while curr.next != None:
    #         print("processing %s"%(curr.val))
    #         if curr.child:
    #             temp = curr.next
    #             (first, last) = self.flattenHelper(curr.child)
    #             print("returned %s, %s, temp is %s"%(first.val, last.val, temp.val))
    #             curr.next = first
    #             first.prev = curr
    #             last.next = temp
    #             temp.prev = last
    #         curr = curr.next
    #     # return the first and last element
    #     return (head, curr)

    def flattenHelper(self, head, stack):
        """
        :type head: Node
        :rtype: Node
        """
        #self.flattenHelper(head)
        curr = head
        while curr != None:
            #print(curr.val)
            stack.append(curr)
            if curr.child:
                self.flattenHelper(curr.child, stack)
            curr = curr.next

    def flatten(self, head, stack):
        """
        :type head: Node
        :rtype: Node
        """
        #self.flattenHelper(head)
        curr = head
        while curr != None:
            #print(curr.val)
            stack.append(curr)
            if curr.child:
                self.flatten(curr.child, stack)
            curr = curr.next

    def printList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #self.flattenHelper(head)
        curr = head
        while curr != None:
            print(curr.val)
            curr = curr.next

def getChildList1(a, b, c):
    h = Node(a, None, None, None)
    n1 = Node(b, None, None, None)
    n2 = Node(c, None, None, None)
    h.next = n1
    n1.prev = h
    n1.next = n2
    n2.prev = n1
    return h

def getChildList(a, b, c):
    h2 = Node(20, None, None, None)
    n12 = Node(21, None, None, None)
    n22 = Node(22, None, None, None)
    h2.next = n12
    n12.prev = h2
    n12.next = n22
    n22.prev = n12

    h1 = Node(10, None, None, None)
    n11 = Node(11, None, None, h2)
    n21 = Node(12, None, None, None)
    h1.next = n11
    n11.prev = h1
    n11.next = n21
    n21.prev = n11

    h = Node(a, None, None, h1)
    n1 = Node(b, None, None, None)
    n2 = Node(c, None, None, None)
    h.next = n1
    n1.prev = h
    n1.next = n2
    n2.prev = n1
    return h

if __name__=='__main__':
    s = Solution()

    h = Node(1, None, None, None)
    n1 = Node(2, None, None, getChildList(4,5,6))
    n2 = Node(3, None, None, None)
    h.next = n1
    n1.prev = h
    n1.next = n2
    n2.prev = n1
    stack = collections.deque()
    s.flatten(h, stack)

    head = stack.popleft()
    curr = head
    while stack:
        temp = stack.popleft()
        curr.next = temp
        temp.prev = curr
        curr.child = None
        curr = curr.next
    s.printList(head)
