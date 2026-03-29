class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
            
        m, n = len(s), len(t)
        dp = [0]*(n+1)
        dp[n] = 1

        for i in range (m-1, -1, -1):
            curRow = [0]*(n+1)
            curRow[n] = 1
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    curRow[j] = dp[j+1] + dp[j]
                else:
                    curRow[j] = dp[j]
            dp = curRow
        
        return dp[0]