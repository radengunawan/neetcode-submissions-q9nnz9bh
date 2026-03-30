class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if not s1 and not s2 and not s3:
            return True

        M, N, L = len(s1), len(s2), len(s3)
        
        if (M+N != L):
            return False
        
        dp = [[False]*(N+1) for _ in range (M+1)]
        dp[M][N] = True

        # dp outer layer fill
        # Edge case1 - floor shell:
        for j in range(N-1, -1, -1):
            k = M + j
            if (s2[j] == s3[k] and dp[M][j+1]):
                dp[M][j] = True

        # Edge case 2: right shell
        for i in range (M-1, -1, -1):
            k = i + N
            if (s1[i] == s3[k] and dp[i+1][N]):
                dp[i][N] = True

        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                k = i+j
                if(s1[i] == s3[k] and dp[i+1][j]):
                    dp[i][j] = True
                elif(s2[j] == s3[k] and dp[i][j+1]):
                    dp[i][j] = True

        return dp[0][0] 

