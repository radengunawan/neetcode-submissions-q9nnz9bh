class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        M, N = len(text1), len(text2)
        
        cache = [[None]*(N+1) for _ in range (M+1)]

        def LCS_from(i,j) -> str:
            if (i==M or j == N):
                return ""
            
            if cache[i][j] is not None:
                return cache[i][j]

            res = ""
            if (text1[i] == text2[j]):
                res = text1[i] + LCS_from(i+1, j+1)
            else:
                op1 = LCS_from(i+1, j)
                op2 = LCS_from(i,j+1)
                res = op1 if len(op1) > len(op2) else op2
            cache[i][j] = res
            return res
        
        final_string = LCS_from(0,0)


        return len(final_string)
            