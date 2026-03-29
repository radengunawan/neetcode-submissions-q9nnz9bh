# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stackz = []
        current = root
        final_result = []

        while current or stackz:
            if current:
                final_result.append(current.val)
                if (current.right):
                    stackz.append(current.right)
                current = current.left
            else:
                current = stackz.pop()

        return final_result     