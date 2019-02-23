class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        if self.head is not None:
            while True:
                print temp.data,
                temp = temp.next
                if temp is self.head:
                    break

    def push(self, data):
        new_node = Node(data)
        temp = self.head

        new_node.next = self.head

        if self.head is not None:
            while temp.next is not self.head:
                temp = temp.next
            temp.next = new_node

        else:
            new_node.next = new_node

        self.head = new_node


if __name__ == "__main__":
    cllist = CircularLinkedList()
    cllist.push(12)
    cllist.push(48)
    cllist.push(72)
    cllist.push(24)

    cllist.print_list()
