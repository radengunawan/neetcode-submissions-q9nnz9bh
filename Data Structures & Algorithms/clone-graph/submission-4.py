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

        clone = Node(node.val)
        oldToNew = {node: clone}
        q = deque([(node, clone)])

        while q:
            cur, cur_copy = q.popleft()

            for nei in cur.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append((nei, oldToNew[nei]))
                oldToNew[cur].neighbors.append(oldToNew[nei])

        return clone