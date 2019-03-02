# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.head = head
        curr = self.head
        next = None
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev =  curr
            curr = next

        self.head = prev
        return self.head