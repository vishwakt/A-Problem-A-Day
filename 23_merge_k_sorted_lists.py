from typing import List


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # print(lists)

        if not lists:
            return

        if len(lists) == 1:
            return lists[0]

        mid = len(lists)//2

        leftHalf = self.mergeKLists(lists[:mid])
        rightHalf = self.mergeKLists(lists[mid:])
        return self.merge(leftHalf, rightHalf)

    def merge(self, l1, l2):
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next

            else:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next

        if l1:
            curr.next = l1

        if l2:
            curr.next = l2

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    s.mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]])
#
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
