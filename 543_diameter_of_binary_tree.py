class Solution(object):
    def diameterOfBinaryTree(self, root):
        return self.helper(root)[0]

    def helper(self, node):
        if not node:
            return 0, -1
        l_diameter, l_path = self.helper(node.left)
        r_diameter, r_path = self.helper(node.right)
        diameter = max(l_diameter, r_diameter, 2 + l_path + r_path)
        path = 1 + max(l_path, r_path)
        return diameter, path
