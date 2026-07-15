class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def get_area(r, c):
            stack = [(r, c)]
            area = 0
            while stack:
                row, col = stack.pop()
                if (row < 0 or row == ROWS or col < 0 or col == COLS or
                    grid[row][col] == 0 or (row, col) in visit):
                    continue

                visit.add((row, col))
                area += 1
                stack.append((row + 1, col))
                stack.append((row - 1, col))
                stack.append((row, col + 1))
                stack.append((row, col - 1))
            return area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, get_area(r, c))
        return max_area