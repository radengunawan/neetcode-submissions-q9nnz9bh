class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        M, N = len(text1), len(text2)
        dp = [[""]* (N+1) for i in range (M+1)]

        res = ""
        for i in range (M-1, -1, -1):
            for j in range(N-1, -1, -1):
                if (text1[i] == text2[j]):
                    res = text1[i] + dp[i+1][j+1]
                else:
                    op1 = dp[i+1][j]
                    op2 = dp[i][j+1]
                    res = op1 if len(op1) > len(op2) else op2
                dp[i][j] = res
        lcs_string = dp[0][0]
        return len(lcs_string)
            