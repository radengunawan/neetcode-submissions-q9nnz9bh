class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        M, N = len(word1), len(word2)
        dp = [[0]*(N+1) for _ in range (M+1)]

        for i in range(M+1):
            dp[i][N] = len(word1[i:])
        
        for j in range(N+1):
            dp[M][j] = len(word2[j:])

        for i in range(M-1, -1, -1):
            for j in range (N-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
            
        return dp[0][0]