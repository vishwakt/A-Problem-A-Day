class Node:
    '''Node class'''
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    '''Linked List class'''
    def __init__(self):
        self.head = None

    def print_list(self):
        """Prints linked list"""
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

    def add_first(self, new_data):
        """Inserts new node at the beginning of the linked list"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        """Inserts new node after a given node in the linked list"""
        if prev_node is None:
            print "Node doesn't exist"
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def add_last(self, new_data):
        """Inserts new node at the end of the linked list"""
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def insert_before(self, data, new_data):
        """Insert new node before a given data"""
        if self.head.next is None:
            self.add_first(new_data)

        if self.head.data is data:
            self.add_first(new_data)
            return

        new_node = Node(new_data)

        temp = self.head

        while temp.next is not None:
            if temp.data is data:
                break
            prev = temp
            temp = temp.next

        # if temp.next is None:
        #     print "No such node exists"

        prev.next = new_node
        new_node.next = temp

    def delete_node(self, data):
        """Deletes node with given data"""
        temp = self.head

        if temp.next is not None:
            if temp.data is data:
                self.head = temp.next
                temp = None
                return

        while temp.next is not None:
            if temp.data is data:
                break
            prev = temp
            temp = temp.next

        if temp.next is None:
            print "No such node exists"
            return

        prev.next = temp.next

        temp = None

    def delete_node_at_position(self, position):

        if self.head is None:
            return

        temp = self.head

        if position is 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None or temp.next is None or position < 0:
            print "Invalid position"
            return

        next = temp.next.next
        temp.next = None
        temp.next = next


if __name__ == "__main__":
    llist = LinkedList()
    llist.add_first(1)
    llist.add_last(2)
    llist.add_last(3)
    llist.add_last(4)
    llist.add_last(5)

    llist.insert_before(5, 4.5)
    llist.delete_node_at_position(-1)

    llist.print_list()