class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        M, N = len(text1), len(text2)
        dp_0 = [0]*(N+1)

        for i in range (M-1, -1, -1):
            dp_1 = [0]*(N+1)
            for j in range (N-1, -1, -1):
                if (text1[i] == text2[j]):
                    dp_1[j] = 1 + dp_0[j+1]
                else:
                    dp_1[j] = max(dp_0[j], dp_1[j+1])
               
            dp_0 = dp_1
        
        return dp_0[0]
