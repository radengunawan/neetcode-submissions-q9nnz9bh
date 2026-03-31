class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0

        if len(text1) < len(text2):
            text1, text2 = text2, text1

        M, N = len(text1), len(text2)

        if text1 == text2:
            return N

        if set(text1).isdisjoint(text2):
            return 0
            
        dp_M = [0]*(N+1)
        dp_1 = [0]*(N+1)

        for i in range(M-1, -1, -1):
            for j in range (N-1, -1, -1):
                if text1[i] == text2[j]:
                    dp_1[j] = 1 + dp_M[j+1]
                else:
                    dp_1[j] = max(dp_1[j+1], dp_M[j]) 
            dp_M, dp_1 = dp_1, dp_M
        
        return dp_M[0]

