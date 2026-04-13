class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        M, N, L = len(s1), len(s2), len(s3)

        if (M+N != L):
            return False
        
        dp = [[None]*(N+1) for _ in range (M+1)]
        dp[M][N] = True

        for j in range(N-1, -1, -1):
            k = M+j
            dp[M][j] = (s2[j] == s3[k] and dp[M][j+1])
        
        for i in range(M-1, -1, -1):
            for j in range (N, -1, -1):
                k = i+j
                dp[i][j] = (s1[i] == s3[k] and dp[i+1][j]) or \
                           (j < N and s2[j] == s3[k] and dp[i][j+1])
        
        return dp[0][0]

        # def isInterleave_from(i,j):
        #     if i == M and j==N:
        #         return True
            
        #     k = i+j
            
        #     res = (i<M and s1[i] == s3[k] and isInterleave_from(i+1,j)) or \
        #           (j<N and s2[j] == s3[k] and isInterleave_from(i,j+1))
            
        #     cache[i][j] = res
        #     return res

        # return isInterleave_from(0,0)