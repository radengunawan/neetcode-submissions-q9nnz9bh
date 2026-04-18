class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        if not str1 and not str2:
            return ""
        
        if not str1:
            return str2
        elif not str2:
            return str1
        
        if str1 == str2:
            return str1
        
        if set(str1).isdisjoint(str2):
            return (str1+str2)
        
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        M, N = len(str1), len(str2)

        dp_below = [""]*(N+1)
        dp_current = [""]*(N+1)

        for j in range(N+1):
            dp_below[j] = str2[j:]
        
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

        # def SCS_from(i,j):
        #     if i ==M :
        #         return str2[j:]
        #     if j==N:
        #         return str1[i:]
        #     if cache[i][j] is not None:
        #         return cache[i][j]
            
        #     if str1[i] == str2[j]:
        #         cache[i][j] = str1[i] + SCS_from(i+1,j+1)
        #     else:
        #         op1 = str1[i] + SCS_from(i+1,j)
        #         op2 = str2[j] + SCS_from(i,j+1)
        #         cache[i][j] = op1 if len(op1) < len(op2) else op2
            
        #     return cache[i][j]

        # return SCS_from(0,0)