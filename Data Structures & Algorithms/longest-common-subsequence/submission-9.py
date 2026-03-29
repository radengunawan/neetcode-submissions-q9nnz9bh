class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0
        
        N_row, N_column = len(text1), len(text2)

        if (N_row < 1 or N_column <1):
            return 0

        cache = [[None]*(N_column + 1) for _ in range (N_row+1)]

        res = None
        def LCS_from(i:int, j:int) -> int:

            if (i == N_row or j == N_column):
                return 0
            
            if cache[i][j] is not None:
                return cache[i][j]

            res = None
            if text1[i] == text2[j]:
                res = 1 + LCS_from(i+1, j+1)
            else:
                opsi1 = LCS_from(i+1,j)
                opsi2 = LCS_from(i,j+1)
                res = max(opsi1, opsi2)
                
            cache[i][j] = res
            return res
        
        return LCS_from(0,0)



    