class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0

        M, N = len(text1), len(text2)

        if text1 == text2:
            return M
        
        if set(text1).isdisjoint(text2):
            return 0
        
        cache = [[None]*(N+1) for _ in range (M+1)]
        
        def LCS_from(i,j):
            if i == M or j == N:
                return 0
            if cache[i][j] is not None:
                return cache[i][j]
            
            res = 0
            if text1[i] == text2[j]:
                res = 1 + LCS_from(i+1,j+1)
            else:
                op1 = LCS_from(i+1,j)
                op2 = LCS_from(i,j+1)
                res = max(op1,op2)
            cache[i][j] = res
            return res
                
        return LCS_from(0,0)