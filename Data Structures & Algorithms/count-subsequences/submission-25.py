class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)

        if N > M:
            return 0
        
        dp = [[0]*(N+1) for _ in range (M+1)]

        for i in range (M+1):
            dp[i][N] = 1
        
        res = 0
        for i in range (M-1, -1, -1):
            for j in range (N-1, -1, -1):
                if s[i] == t[j]:
                    res = dp[i+1][j+1] + dp[i+1][j]
                else:
                    res = dp[i+1][j]
                dp[i][j] = res


        return dp[0][0] 
        