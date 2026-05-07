class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if not s or not t:
            return 0
        
        M, N = len(s), len(t)

        if N > M or not set(t).issubset(set(s)):
            return 0
        
        if s == t:
            return 1
        
        dp = [[0]*(N+1) for _ in range(M+1)]

        for i in range(M+1):
            dp[i][N] = 1
        
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                dp[i][j] = dp[i+1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        
        return dp[0][0]

        # def numDis_from(i,j):
        #     if j == N:
        #         return 1
        #     if i == M:
        #         return 0
            
        #     res = numDis_from(i+1,j)
        #     if s[i] == t[j]:
        #         res += numDis_from(i+1,j+1)
            
        #     cache[i][j] = res
        #     return res
        
        # return numDis_from(0,0)
        