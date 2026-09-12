class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        
        def bfs(node):

            visited.add(node)
            q = deque([node])

            while q:
                curr = q.popleft()
                for neigh in adj[curr]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)
            
            return 1


        res = 0

        for node in range(n):
            if node not in visited:
                res += bfs(node)
        
        return res
        