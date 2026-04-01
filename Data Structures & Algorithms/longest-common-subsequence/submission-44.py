class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0
        
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        M, N = len(text1), len(text2)

        if text1 == text2:
            return N

        if set(text2).isdisjoint(text1):
            return 0
            
        cache = [[None]*(N) for i in range (M)]

        def LCS_from(i,j) -> int:
            if (i==M or j ==N):
                return 0
            if cache[i][j] is not None:
                return cache[i][j]
            
            cal = 0
            if text1[i] == text2[j]:
                cal = 1 + LCS_from(i+1, j+1)
            else:
                op1 = LCS_from(i, j+1)
                op2 = LCS_from(i+1, j)
                cal = max(op1, op2)
            cache[i][j] = cal
            return cal


        return LCS_from(0,0)
        