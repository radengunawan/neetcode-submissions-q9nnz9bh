"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = set()
        oldToNew = {}

        def DFS(node):
            if node.val in visited:
                return oldToNew[node.val]
            
            visited.add(node.val)
            copy = Node(node.val)
            oldToNew[node.val] = copy

            for neigh in node.neighbors:
                copy.neighbors.append(DFS(neigh))
            
            return copy

        return DFS(node)


        