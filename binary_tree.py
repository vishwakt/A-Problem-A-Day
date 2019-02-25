class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_inorder(self, root):
        if root:
            self.print_inorder(root.left)
            print root.data
            self.print_inorder(root.right)

    def print_postorder(self, root):
        if root:
            self.print_postorder(root.left)
            self.print_postorder(root.right)
            print root.data

    def print_preorder(self, root):
        if root:
            print root.data
            self.print_preorder(root.left)
            self.print_preorder(root.right)

    def print_level_order(self, root):
        if root is None:
            print "No nodes"
            return

        else:
            queue = []
            queue.append(root)
            while len(queue) is not 0:
                print queue[0].data
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)


if __name__ == "__main__":
    bt = Node(3)
    bt.insert(2)
    bt.insert(1)
    bt.insert(5)
    bt.insert(4)

    bt.print_inorder(bt)
    bt.print_preorder(bt)
    bt.print_postorder(bt)

    bt.print_postorder(bt)