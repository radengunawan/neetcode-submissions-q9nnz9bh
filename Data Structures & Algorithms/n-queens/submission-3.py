class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = 0
        posDiag = 0
        negDiag = 0
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            nonlocal col, posDiag, negDiag
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if ((col & (1 << c)) or (posDiag & (1 << (r + c)))
                    or (negDiag & (1 << (r - c + n)))):
                    continue
                col ^= (1 << c)
                posDiag ^= (1 << (r + c))
                negDiag ^= (1 << (r - c + n))
                board[r][c] = "Q"

                backtrack(r + 1)

                col ^= (1 << c)
                posDiag ^= (1 << (r + c))
                negDiag ^= (1 << (r - c + n))
                board[r][c] = "."

        backtrack(0)
        return res