class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0
        
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        if set(text2).isdisjoint(text1):
            return 0
        
        M, N = len(text1), len(text2)

        cache = [[None]*N for _ in range (M)]

        def LCS_from(i,j):
            if i == M or j == N:
                return 0
            if cache[i][j] != None:
                return cache[i][j]
            
            res = 0
            if text1[i] == text2[j]:
                res = 1 + LCS_from(i+1,j+1)
            else:
                res = max(LCS_from(i+1,j), LCS_from(i,j+1))
            cache[i][j] = res
            return res
        
        return LCS_from(0,0)
        