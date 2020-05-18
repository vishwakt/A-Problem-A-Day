"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        print(head)
        if not head:
            return None

        curr = head
        copyOfLL = {}

        while curr:
            copyOfLL[curr] = Node(curr.val, None, None)
            curr = curr.next

        curr = head
        while curr:
            if curr.random:
                copyOfLL[curr].random = copyOfLL[curr.random]
            if curr.next:
                copyOfLL[curr].next = copyOfLL[curr.next]
            curr = curr.next

        return copyOfLL[head]


if __name__ == "__main__":
    s = Solution()
    s.copyRandomList(head=[[7,None],[13,0],[11,4],[10,2],[1,0]])
