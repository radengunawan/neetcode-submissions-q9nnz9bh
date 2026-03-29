# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree (n1, n2):
            stack = [(n1,n2)]

            while stack:
                n1, n2 = stack.pop()

                if not n1 and not n2:
                    continue
                if not n1 or not n2 or n1.val != n2.val:
                    return False
                stack.append((n1.right, n2.right))
                stack.append((n1.left, n2.left))
        
            return True

        if not subRoot:
            return True

        if not root:
            return False

        q1 = deque([root])

        while q1:  
            for _ in range (len(q1)):
                nod1 = q1.popleft()
                if isSameTree(nod1, subRoot):
                    return True
                if nod1.left:
                    q1.append(nod1.left)
                if nod1.right:
                    q1.append(nod1.right)

        return False
        