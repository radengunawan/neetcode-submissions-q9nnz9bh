class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        if grid [0][0] !=0 or grid[-1][-1] !=0:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs (curr_r, curr_c):

            if not (0 <= curr_r < ROWS and 0 <= curr_c < COLS):
                return 0

            if grid[curr_r][curr_c] != 0 or (curr_r, curr_c) in visited:
                return 0

            if (curr_r, curr_c) == (ROWS - 1, COLS -1):
                return 1
                #visited.add((curr_r, curr_c))
                #count = 1
                # visited.remove((curr_r, curr_c))
            
            visited.add((curr_r, curr_c))

            count = 0

            for dr, dc, in directions:
                next_r, next_c = curr_r + dr, curr_c + dc
                count += dfs(next_r, next_c)

            visited.remove((curr_r, curr_c))

            return count

        return dfs(0,0)

        