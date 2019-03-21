# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def _deleteNode(self, node):
        next = node.next
        if next != None:
            node.val = next.val
            node.next = next.next

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        start = head
        end = head.next
        while end != None:
            if start.val != end.val:
                start = start.next
                end = end.next
            else:
                self._deleteNode(end)


    def printList(self, head):
        while head != None:
            print(head.val)
            print(" -> ")
            head = head.next
        print("None")

if __name__ == '__main__':
    # 1 2 3 3 4 4 5
    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(3)
    # head.next.next.next.next = ListNode(4)
    # head.next.next.next.next.next = ListNode(4)
    # head.next.next.next.next.next.next = ListNode(5)

    s = Solution()
    s.deleteDuplicates(head)
    s.printList(head)
