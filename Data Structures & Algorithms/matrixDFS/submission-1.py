class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        neighborz = [(0,1), (1,0), (0,-1), (-1,0)]

        def backtrack (r,c):
            if not(0 <= r < ROWS and 0 <= c < COLS ):
                return 0 

            if grid[r][c] ==1 or (r,c) in visited:
                return 0
            
            #visited.add((r,c))

            if (r,c) == (ROWS-1, COLS-1):
                return 1

            visited.add((r,c))

            count = 0
            for dr, dc in neighborz:
                next_r, next_c = r + dr, c + dc
                count += backtrack(next_r, next_c)

            visited.remove((r,c))

            return count

        return backtrack(0,0)
 