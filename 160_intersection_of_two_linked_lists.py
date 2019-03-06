# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        hA = headA
        while hA.next:
            hA = hA.next

        tail = hA
        tail.next = headA

        intersection = None
        hb1 = headB
        hb2 = headB

        while hb1 and hb2:
            hb1 = hb1.next
            hb2 = hb2.next
            if hb2:
                hb2 = hb2.next
            if hb1 == hb2:
                break

        if hb1 and hb2 and hb1 == hb2:
            hb1 = headB
            while hb1 != hb2:
                hb1 = hb1.next
                hb2 = hb2.next

            intersection = hb1

        tail.next = None

        return intersection


if __name__ == "__main__":
    s = Solution()
