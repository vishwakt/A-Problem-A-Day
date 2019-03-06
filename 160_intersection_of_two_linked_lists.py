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
        if not headA or headB:
            return None

        p = headA
        while p.next:
            p = p.next

        mark = p
        mark.next = headA

        intersection = None
        p1 = headB
        p2 = headB

        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            if p2: p2 = p2.next
            if p1 == p2: break

        if p1 and p2 and p1 == p2:
            p1 = headB
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next

            intersection = p1

        mark.next = None

        return intersection


if __name__ == "__main__":
    s = Solution()
