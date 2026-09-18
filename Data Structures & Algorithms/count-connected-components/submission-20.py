class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for i in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def bfs(node):
            if node in visited:
                return 0
            
            q = deque([node])
            while q:
                cur = q.popleft()
                for neigh in adj[cur]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)

            return 1

        
        res = 0
        for i in range(n):
            res += bfs(i)
        
        return res
        