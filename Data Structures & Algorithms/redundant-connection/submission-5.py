class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)

        par = {i:i for i in range(1,N+1)}
        rank = {i:1 for i in range(1, N+1)}

        def find(X):
            p = par[X]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(x1,x2):
            p1, p2 = find(x1), find(x2)
            
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        for a,b in edges:
            if not union(a,b):
                return [a,b]
        