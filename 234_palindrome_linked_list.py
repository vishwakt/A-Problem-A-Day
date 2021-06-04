# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head

        # find the midddle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half of linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


if __name__ == "__main__":
    s = Solution()
    # s.add_first(1)
    # s.add_last(2)
    # s.add_last(2)
    # s.add_last(1)
    # s.add_last(-129)
    # s.add_last(-129)
    print(s.isPalindrome(s.head))
