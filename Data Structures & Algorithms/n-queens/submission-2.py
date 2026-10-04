class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [False] * n
        posDiag = [False] * (n * 2)
        negDiag = [False] * (n * 2)
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if col[c] or posDiag[r + c] or negDiag[r - c + n]:
                    continue
                col[c] = True
                posDiag[r + c] = True
                negDiag[r - c + n] = True
                board[r][c] = "Q"

                backtrack(r + 1)

                col[c] = False
                posDiag[r + c] = False
                negDiag[r - c + n] = False
                board[r][c] = "."

        backtrack(0)
        return res