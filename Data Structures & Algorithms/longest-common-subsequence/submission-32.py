class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 and not text2:
            return 1
        if not text1 or not text2:
            return 0
        M, N = len(text1), len(text2)

        cache = [[None]*(N+1) for i in range (M+1)]

        def LCS_from (i,j) -> int:
            if i == M or j ==N:
                return 0
            if cache[i][j] != None:
                return cache[i][j]
            
            res = 0
            if text1[i] == text2[j]:
                res = 1 + LCS_from(i+1, j+1)
            else:
                ops1 = LCS_from(i,j+1)
                ops2 = LCS_from(i+1,j)
                res = max(ops1, ops2)
            cache[i][j] = res
            return res

        return LCS_from(0,0)