class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        if not str1 and not str2:
            return ""
        
        if not str1:
            return str2
        elif not str2:
            return str1

        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        M, N = len(str1), len(str2)
        
        if str1 == str2:
            return str1
        
        if set(str2).isdisjoint(str1):
            return (str1+str2)
        
        dp_below = [0]*(N+1)
        dp_current = [0]*(N+1)

        #1. Edge Case
        # 1.1. "Horizontal" Edge case
        for j in range(N+1):
            dp_below[j] = str2[j:]
        
        # 1.2. "Vertical" Edge Case
        # for i in range(M+1):
        #     dp[i][N] = str1[i:]
        
        #2. Core DP algorithm + "vertical" edge case on the go
        for i in range(M-1, -1, -1):
            dp_current[N] = str1[i:]
            for j in range(N-1, -1, -1):
                if str1[i] == str2[j]:
                    dp_current[j] = str1[i] + dp_below[j+1]
                else:
                    op1 = str1[i] + dp_below[j]
                    op2 = str2[j] + dp_current[j+1]
                    dp_current[j] = op1 if len(op1) < len(op2) else op2
            
            dp_below, dp_current = dp_current, dp_below
        
        return dp_below[0]
        
        # def SCS_form(i,j):
        #     if j == N:
        #         return str1[i:]
        #     if i == M:
        #         return str2[j:]
        #     if cache[i][j] is not None:
        #         return cache[i][j]
            
        #     res = ""
        #     if str1[i] == str2[j]:
        #         res = str1[i] + SCS_form(i+1,j+1)
        #     else:
        #         op1 = str1[i] + SCS_form(i+1,j)
        #         op2 = str2[j] + SCS_form(i,j+1)
        #         res = op1 if len(op1) < len(op2) else op2
        #     cache[i][j] = res
        #     return res
            
        # return SCS_form(0,0)