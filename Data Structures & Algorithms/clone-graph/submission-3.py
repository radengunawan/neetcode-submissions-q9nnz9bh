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

        oldToNew = {}
        visited = {node}
        # oldToNew[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            if cur not in oldToNew:
                oldToNew[cur] = Node(cur.val)

            for nei in cur.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                oldToNew[cur].neighbors.append(oldToNew[nei])

        return oldToNew[node]