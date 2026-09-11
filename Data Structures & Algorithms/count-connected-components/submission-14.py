class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def bfs(start):
            visited.add(start)
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neigh in adj[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)

        count = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                count += 1
        return count