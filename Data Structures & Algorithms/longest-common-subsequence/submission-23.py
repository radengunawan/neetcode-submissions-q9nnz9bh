class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        M, N = len(text1), len(text2)
        cache = [[None]* (N+1) for i in range (M+1)]

        def LCS_from(i,j) -> str:
            if i == M or j ==N:
                return ""
            if cache[i][j] is not None:
                return cache[i][j]
            res = ""
            if text1[i] == text2[j]:
                res = text1[i] + LCS_from(i+1, j+1)
            else:
                ops1 = LCS_from(i+1,j)
                ops2 = LCS_from(i, j+1)
                res = ops1 if len(ops1) > len(ops2) else ops2
            cache[i][j] = res
            return res
        
        result = LCS_from(0,0)
        return len(result)
            

            