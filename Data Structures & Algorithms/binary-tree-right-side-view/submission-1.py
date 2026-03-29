# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        final_list = []
        queue = deque()

        if root:
            queue.append(root)

        while queue:
            level = []
            for i in range (len(queue)):
                current = queue.popleft()
                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append (current.right)
            final_list.append(level)

        for i in range (len(final_list)):
            final_list[i] = final_list[i][-1]

        
        
        return final_list

        


        