class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1
        if N == 1:
            return 1

        direct = [0, 1, 0, -1, 0, 1, 1, -1, -1, 1]
        q1 = deque([(0, 0)])
        q2 = deque([(N - 1, N - 1)])
        grid[0][0] = -1
        grid[N - 1][N - 1] = -2

        res = 2
        start, end = -1, -2
        while q1 and q2:
            for _ in range(len(q1)):
                r, c = q1.popleft()
                for d in range(9):
                    nr, nc = r + direct[d], c + direct[d + 1]
                    if 0 <= nr < N and 0 <= nc < N:
                        if grid[nr][nc] == end:
                            return res
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = start
                            q1.append((nr, nc))

            q1, q2 = q2, q1
            start, end = end, start
            res += 1

        return -1