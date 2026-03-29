class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        M, N = len(text1), len(text2)
        dp = [[0]*(N+1) for i in range(M+1)]

        for i in range (M-1, -1, -1):
            for j in range (N-1, -1, -1):
                res = 0
                if (text1[i] == text2[j]):
                    res = 1 + dp[i+1][j+1]
                else:
                    res = max(dp[i+1][j], dp[i][j+1])
                dp[i][j] = res
        
        return res
