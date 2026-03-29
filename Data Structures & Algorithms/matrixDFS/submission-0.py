class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit, path, all_paths = set(), [], []
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left

        def dfs (r,c):
            if(min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c]==1 or (r,c) in visit):
                return

            visit.add((r,c))
            path.append((r,c))

            if (r,c) == (ROWS-1, COLS-1):
                all_paths.append(path.copy())
            else:
                for dr, dc in DIRS:
                    dfs (r+dr, c + dc)
            
            visit.remove((r,c))
            path.pop()

        dfs(0,0)

        return len(all_paths)

        