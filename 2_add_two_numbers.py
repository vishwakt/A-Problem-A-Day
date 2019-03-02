"""Time: O(max(list1, list2)) Space: O(max(list1, list2))"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = ListNode(0)
        temp = root

        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(carry + v1 + v2, 10)
            temp.next = ListNode(val)
            temp = temp.next
        return root.next


if __name__ == "__main__":

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solution = Solution()
    o = solution.addTwoNumbers(l1, l2)
    while o:
        print o.next.val
