class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0

        M, N = len(text1), len(text2)

        if (M<1 or N <1):
            return 0

        cache = [[None]*(N+1) for _ in range (M+1)]

        def LCS_from(i,j) -> int:
            if (i == M or j ==N):
                return 0
            
            if cache[i][j] is not None:
                return cache[i][j]
            
            if text1[i] == text2[j]:
                cache[i][j] = 1 + LCS_from(i+1, j+1)
            else:
                poss1 = LCS_from(i+1, j)
                poss2 = LCS_from(i,j+1)
                cache[i][j] = max(poss1, poss2)
            return cache[i][j]
        
        return LCS_from(0,0)

