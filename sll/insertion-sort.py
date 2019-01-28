# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printList(self, head):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr1 = head
        head2 = None
        while curr1:
            curr2=head
            if not head2:
                temp = curr1.next
                head2 = curr1
                curr1 = temp
                curr2 = head2
            elif head2.val > curr2.val
                temp = curr1.next
                head2 = curr1
                curr1 = temp
                curr2 = head2
            else:
                while curr2 and curr2.val < curr.val:
                    curr2 = curr2.next
                temp = curr1.next
                curr2.val = curr1
                curr1 = temp
            # if not curr2:
            #
            # elif curr1.val > curr2.val:
            #     curr2 = curr1
            #     curr2.next = curr1
            #     curr1.next = temp
            # else
        return head2

if __name__ == '__main__':
    two = ListNode(2)
    one = ListNode(1)
    three = ListNode(3)
    three.next = one
    one.next = two
    head = three
    s = Solution()
    s.printList(head)
    print("sorted")
    s.printList(s.insertionSortList(head    ))
