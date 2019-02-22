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
        """Delete node at given position"""
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

    def delete_linked_list(self):
        """Delete linked list"""
        current = self.head
        while self.head is not None:
            self.head = self.head.next
            del current
            current = self.head

        # del current

    def length_of_list(self):
        """Print length of linked list"""
        reassign = self.head
        count = 0
        current = self.head
        while self.head is not None:
            self.head = self.head.next
            count += 1
            current = self.head
        print "Length of linked list is:", count
        self.head = reassign
        return count

    def search_an_element(self, element):
        """Search for a given element in a linked list"""
        current = self.head
        count = 0
        while current is not None:
            count += 1
            if current.data == element:
                print "Element found at position:", count - 1
                return
            current = current.next
        print "Element not found"

    def get_nth_node(self, index):
        """Get node at a given index in a linked list"""
        current = self.head
        count = 0

        while current:
            if count == index:
                print current.data
                return
            else:
                count += 1
                current = current.next

        print "Index doesn't exist"

    def get_nth_from_last(self, index):
        """Get nth element from the end of the linked list"""
        print_index = self.length_of_list() - index - 1
        self.get_nth_node(print_index)

    def check_if_palindrome(self):
        """Check if the data in the linked list is a palindrome"""
        stack_of_data = list()
        current = self.head
        while current:
            stack_of_data.append(current.data)
            current = current.next
        current = self.head
        while current:
            if stack_of_data.pop() != current.data:
                print "Not a palindrome"
                return
            else:
                current = current.next
        print "It is a palindrome"

    def swap_nodes(self, x, y):
        """Swap nodes of a linked list"""
        if x is y:
            return

        prevX = None
        currX = self.head
        while currX is not None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        while currY is not None and currY.data != y:
            prevY = currY
            currY = currY.next

        temp = currX.next
        currX.next = currY.next
        currY.next = temp


if __name__ == "__main__":
    llist = LinkedList()
    llist.add_first('a')
    llist.add_last('b')
    llist.add_last('c')
    llist.add_last('c')
    llist.add_last('b')
    llist.add_last('a')
    llist.swap_nodes('a', 'c')
    # llist.insert_before(5, 4.5)

    # llist.length_of_list()
    # llist.search_an_element(3)
    # llist.delete_linked_list()
    # llist.get_nth_node(3)
    # llist.get_nth_from_last(0)
    # llist.check_if_palindrome()
    llist.print_list()