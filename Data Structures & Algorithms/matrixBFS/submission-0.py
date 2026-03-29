class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # 0. edge case: handling if grid is None or contain nothing
        # 1. we will use BFS, level by level
        # 2. on each level, we have 4 neighbor cell max to inspect
        # 3.  each cell must be checked, have we arrived to the expected cell
        # 4. we will use queue
        # 5. we use pointer r,c to track current cell
        # 6. edge case: handling: grid empty
        if not grid or not grid[0]:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        visited = {(0,0)}
        queue = deque([(0,0)])
        neighbor = [(0,1), (1,0), (0,-1), (-1,0)]
        length = 0

        while queue:
            for i in range (len(queue)):
                curr_r, curr_c = queue.popleft()

                if (curr_r, curr_c) == (ROWS - 1, COLS - 1):
                    return length

                for dr, dc in neighbor:
                    next_r, next_c = curr_r + dr, curr_c + dc

                    # bound check
                    if not (0<= next_r < ROWS and 0 <= next_c < COLS):
                        continue

                    # not in visited and not rock (val not 1)
                    if grid[next_r][next_c] ==1 or (next_r, next_c) in visited :
                        continue

                    queue.append((next_r, next_c))
                    visited.add((next_r, next_c))
            length +=1
        
        return -1
        