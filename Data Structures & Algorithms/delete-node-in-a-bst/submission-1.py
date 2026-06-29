# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        parent = None
        cur = root

        # Find the node to delete
        while cur and cur.val != key:
            parent = cur
            if key > cur.val:
                cur = cur.right
            else:
                cur = cur.left

        if not cur:
            return root

        # Node with only one child or no child
        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if not parent:
                return child
            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child
        else:
            # Node with two children
            par = None  # parent of right subTree min node
            delNode = cur
            cur = cur.right
            while cur.left:
                par = cur
                cur = cur.left

            if par:  # if there was a left traversal
                par.left = cur.right
                cur.right = delNode.right

            cur.left = delNode.left

            if not parent:  # if we're deleting root
                return cur

            if parent.left == delNode:
                parent.left = cur
            else:
                parent.right = cur

        return root