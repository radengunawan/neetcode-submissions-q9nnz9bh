class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
 
        M, N, L = len(s1), len(s2), len(s3)
        if (M+N != L):
            return False
        
        dp = [[False]*(N+1) for _ in range (M+1)]
        dp[M][N] = True

        for i in range (M, -1, -1):
            for j in range (N, -1, -1):
                k = i+j
                if i < M and s1[i] == s3[k] and dp[i+1][j]:
                    dp[i][j] = True
                if j < N and s2[j] == s3[k] and dp[i][j+1]:
                    dp[i][j] = True 

        return dp[0][0]

