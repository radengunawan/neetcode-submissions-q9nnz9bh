class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        M, N = len(word1), len(word2)
        dp = [0]*(N+1)
        
        for j in range(N+1):
            dp[j] = len(word2[j:])

        for i in range(M-1, -1, -1):
            curRow = [0]*(N+1)
            curRow[N] = len(word1[i:])
            for j in range (N-1, -1, -1):
                if word1[i] == word2[j]:
                    curRow[j] = dp[j+1]
                else:
                    curRow[j] = 1 + min(dp[j+1], dp[j], curRow[j+1])
            dp = curRow
            
        return dp[0]