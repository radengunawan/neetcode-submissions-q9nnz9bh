class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([(0,0)])
        visited = {(0,0)}
        neighborz = [(0,1), (1,0), (0,-1), (-1,0)]

        length = 0
        while queue:
            for i in range (len(queue)):
                r,c = queue.popleft()
                
                if (r,c) == (ROWS-1, COLS-1):
                    return length

                for dr,dc in neighborz:
                    nr, nc = r+dr, c + dc

                    if not (0<=nr < ROWS and 0<=nc < COLS):
                        continue        
                    if (nr,nc) in visited or grid[nr][nc] ==1:
                        continue
                    queue.append((nr,nc))
                    visited.add((nr, nc))
            length +=1
        return -1