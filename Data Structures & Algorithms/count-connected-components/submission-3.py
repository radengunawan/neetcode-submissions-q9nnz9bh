class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return 0
            
            visited.add(node)
            for neigh in adj[node]:
                # if neigh not in visited:
                #     visited.add(neigh)
                dfs(neigh)
            
            return 1


        res = 0
        for i in range(n):
            res += dfs(i)
            # if i not in visited:
            #     visited.add(i)
            #     dfs(i)
            #     res +=1
        
        return res
 