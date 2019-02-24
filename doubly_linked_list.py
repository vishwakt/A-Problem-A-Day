class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, prev_node, data):
        try:
            new_node = Node(data)
            curr = self.head
            if curr is None:
                print "No list found"
            while curr.data is not prev_node:
                curr = curr.next

            new_node.next = curr.next
            new_node.prev = curr
            new_node.next.prev = new_node
            curr.next = new_node
        except AttributeError:
            print "Node doesn't exist, insert after failed"

    def insert_before(self, next_node, data):
        try:
            new_node = Node(data)
            curr = self.head
            if curr.data == next_node:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                while curr.next.data is not next_node:
                    curr = curr.next
                new_node.next = curr.next
                new_node.prev = curr
                curr.next.prev = new_node
                curr.next = new_node

        except AttributeError:
            print "Node doesn't exist, insert before failed"

    def print_dll(self):
        curr = self.head
        while curr:
            print curr.data
            curr = curr.next


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    dll.push(4)
    dll.push(5)

    dll.insert_after(0, 4)
    dll.insert_before(4, 6)

    dll.print_dll()
