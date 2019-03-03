# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        walker = head
        runner = head.next
        try:
            while walker is not runner:
                walker = walker.next
                runner = runner.next.next

            return True
        except:
            return False