class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        M, N = len (word1), len(word2)
        dp = [[0]*(N+1) for i in range (M+1)]

        for i in range(M+1):
            dp[i][N] = M - i
        
        for j in range (N+1):
            dp[M][j] = N - j
        
        res = 0
        for i in range (M-1, -1, -1):
            for j in range (N-1, -1, -1):
                if (word1[i] == word2[j]):
                    res = 0 + dp[i+1][j+1]
                else:
                    insert = 1 + dp[i][j+1]
                    delete = 1 + dp[i+1][j]
                    replace = 1 + dp[i+1][j+1]
                    res = min (insert, delete, replace)
                dp[i][j] = res
        
        return dp[0][0]
