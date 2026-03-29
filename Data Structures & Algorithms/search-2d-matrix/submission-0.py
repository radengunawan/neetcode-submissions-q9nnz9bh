class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)

        for i in range (m):
            if (target in matrix[i]):
                return True

        return False
        