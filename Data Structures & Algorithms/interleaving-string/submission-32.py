class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if not s1 and not s2 and not s3:
            return True
        
        M, N, L = len(s1), len(s2), len(s3)

        if (M+N !=L ):
            return False
        
        if set(s1).isdisjoint(s3) and set(s2).isdisjoint(s3):
            return False
        
        dp = [[False]*(N+1) for _ in range(M+1)]
        dp[M][N] = True

        # "Floor" Edge Case
        for j in range(N-1, -1, -1):
            k = M + j
            dp[M][j] = (s2[j] == s3[k] and dp[M][j+1])

        # main algorithm
        for i in range(M-1,-1,-1):
            for j in range(N, -1, -1):
                k = i+j
                dp[i][j] = (s1[i] == s3[k] and dp[i+1][j]) or \
                 (j < N and s2[j] == s3[k] and dp[i][j+1])   

        return dp[0][0]    

        # def isInterLeave_from(i,j):
        #     if i == M and j == N:
        #         return True
        #     if cache[i][j] is not None:
        #         return cache[i][j]
            
        #     k = i+j
            
        #     res = (i < M and s1[i] == s3[k] and isInterLeave_from(i+1,j)) or \
        #          (j < N and s2[j] == s3[k] and isInterLeave_from(i,j+1))
            
        #     cache[i][j] = res
        #     return res
        
        # return isInterLeave_from(0,0)
        