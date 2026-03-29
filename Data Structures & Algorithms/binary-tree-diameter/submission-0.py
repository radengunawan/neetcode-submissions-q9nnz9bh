# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        path_list = []

        def maxDepth(node):
            if not node:
                return 0

            return 1 + max(maxDepth(node.left), maxDepth(node.right))

        def preorder(node):
            if not node:
                return

            left_path = maxDepth(node.left)
            right_path = maxDepth(node.right)
            path_list.append(left_path + right_path)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return max(path_list)
        