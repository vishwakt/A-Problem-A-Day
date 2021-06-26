from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def dfsLeft(node):
            if not node or not node.left and not node.right:
                return
            boundary.append(node.val)
            if node.left:
                dfsLeft(node.left)
            else:
                dfsLeft(node.right)

        def dfsLeaves(node):
            if not node:
                return
            dfsLeaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfsLeaves(node.right)

        def dfsRight(node):
            if not node or not node.left and not node.right:
                return
            if node.right:
                dfsRight(node.right)
            else:
                dfsRight(node.left)
            boundary.append(node.val)

        boundary = [root.val]
        dfsLeft(root.left)
        dfsLeaves(root)
        dfsRight(root.right)
        return boundary


if __name__ == "__main__":
    s = Solution()
    print(s.boundaryOfBinaryTree(root = [1,None,2,3,4]))