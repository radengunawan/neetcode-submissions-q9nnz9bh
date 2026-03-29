class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0
        
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        M, N = len(text1), len(text2)

        if text1 == text2:
            return M
        
        check = 0
        for i in range (N):    
            if text2[i] in text1:
                check +=1
        if check == 0:
            return 0
            
        row_next = [0]*(N+1)
        row_curr = [0]*(N+1)

        for i in range(M-1, -1, -1):
            for j in range (N-1, -1, -1):
                if text1[i] == text2[j]:
                    row_curr[j] = 1 + row_next[j+1]
                else:
                    row_curr[j] = max(row_curr[j+1], row_next[j])
             
            row_next, row_curr = row_curr, row_next
        
        return row_next[0]

