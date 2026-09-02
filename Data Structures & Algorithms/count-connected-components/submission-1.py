class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node):
            for neigh in adj[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)


        res = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res +=1
        
        return res
 