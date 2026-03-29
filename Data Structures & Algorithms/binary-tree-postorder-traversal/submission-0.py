# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        resultz = []

        def anyOrder(nodez):

            if not nodez:
                return

            anyOrder(nodez.left)
            anyOrder(nodez.right)
            resultz.append(nodez.val)
        
        anyOrder(root)

        return  resultz
        