class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        visited = set() 
        directionz = [(1,1), (1,-1), (-1,1), (-1,-1), (0,1), (1,0), (0,-1), (-1,0)]
        queue = deque() 

        if grid[0][0] == 1 or grid [-1][-1] ==1:
            return -1
        
        visited.add((0,0))
        queue.append((0,0))

        level = 1
        while queue:
            for i in range (len(queue)):
                curr_r, curr_c = queue.popleft()
                if (curr_r,curr_c) == (ROWS-1, COLS-1):
                    return level
                for dr, dc in directionz:
                    next_r, next_c = curr_r + dr, curr_c + dc

                    if not (0 <= next_r < ROWS and 0<= next_c < COLS):
                        continue
                    if grid[next_r][next_c] > 0 or (next_r, next_c) in visited:
                        continue
                    
                    queue.append((next_r, next_c))
                    visited.add((next_r, next_c))

            level+=1

        return -1
