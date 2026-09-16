class DSU:
    def __init__ (self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
    
    def find (self, node):
        current = node
        while current != self.parent[current]:
            self.parent[current] = self.parent[self.parent[current]]
            current = self.parent[current]
        return current
    
    def union (self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]

        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        dsu = DSU(n)
        res = n

        for u,v in edges:
            if dsu.union(u,v):
                res -= 1
        
        return res
        