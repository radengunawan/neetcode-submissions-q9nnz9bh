class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        M, N = len(text1), len(text2)
        cache = [[None]*(N+1) for i in range (M+1)]

        def LCS_from(i:int, j:int) -> int:

            if (i==M or j == N):
                return 0
            if cache[i][j] is not None:
                return cache[i][j]

            res = 0
            if text1[i] == text2[j]:
                res =  1 + LCS_from(i+1, j+1)
            else:
                prob1 = LCS_from(i+1, j)
                prob2 = LCS_from(i, j+1)

                res= max (prob1, prob2)
            cache[i][j] = res
            return res
        return LCS_from(0, 0)

       




    