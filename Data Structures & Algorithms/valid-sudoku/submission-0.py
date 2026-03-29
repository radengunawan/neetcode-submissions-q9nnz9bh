class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range (9)]
        cols = [set() for _ in range (9)]
        boxes = [set() for _ in range (9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue

                num_rows = i//3
                offset = num_rows*3
                num_cols = j//3
                box_idx = offset + num_cols

                if num in rows[i] or num in cols[j] or num in boxes[box_idx]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)
        
        return True

                

                
        