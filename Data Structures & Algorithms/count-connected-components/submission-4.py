class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}

        visited = set()

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            if node in visited:
                return 0
            
            visited.add(node)
            for neigh in adj[node]:
                dfs(neigh)
            
            return 1
        
        res = 0
        for i in range(n):
            res += dfs(i)
        
        return res

        