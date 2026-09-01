class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > (n-1):
            return False

        adj = {i:[] for i in range(n)}

        for node, connection in edges:
            adj[node].append(connection)
            adj[connection].append(node)
        
        visited = set()

        def dfs(node, par):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        result1 = dfs(0, -1)
        result2 = len(visited) == n

        return result1 and result2
        