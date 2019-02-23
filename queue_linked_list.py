class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            new_node.next = self.head
            self.head = self.tail

        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        self.tail.next = self.head.next
        self.head = None
        self.head = self.tail.next

    def print_queue(self):
        curr = self.head
        while curr.next is not self.head:
            print curr.data
            curr = curr.next
        print curr.data

    def print_head(self):
        print self.head.data

    def print_tail(self):
        print self.tail.data


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.dequeue()

    q.print_queue()
    q.print_head()
    q.print_tail()
