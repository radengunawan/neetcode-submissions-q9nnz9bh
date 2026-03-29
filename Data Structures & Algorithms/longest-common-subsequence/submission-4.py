class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0
        
        M, N = len(text1), len(text2)

        # dp = [[0]*(N+1) for _ in range(M+1)]

        dp = [0]*(N+1)

        for i in range (M-1,-1,-1):
            curRow = [0]*(N+1)
            for j in range (N-1, -1, -1):
                if text1[i] == text2[j]:
                    curRow[j] = 1 + dp[j+1]
                else:
                    curRow[j] = max(curRow[j+1], dp[j])
            dp = curRow
        
        return dp[0]
