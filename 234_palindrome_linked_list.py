# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        self.head = None

    def add_first(self, new_data):
        """Inserts new node at the beginning of the linked list"""
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, new_data):
        """Inserts new node at the end of the linked list"""
        new_node = ListNode(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        head1 = head
        head2, count = self.reverse_list(head)
        flag = False
        while head2 and head1:
            if head2.val is head1.val:
                head2 = head2.next
                head1 = head1.next
            else:
                return False
        return True

    def reverse_list(self, head):
        curr = head
        prev = None
        next = None
        count = 0
        while curr:
            count += 1
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        curr = prev
        return curr, count


if __name__ == "__main__":
    s = Solution()
    s.add_first(1)
    s.add_last(2)
    s.add_last(2)
    s.add_last(1)
    # s.add_last(-129)
    # s.add_last(-129)
    print s.isPalindrome(s.head)