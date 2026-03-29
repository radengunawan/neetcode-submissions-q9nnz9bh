class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0
        
        M, N = len(text1), len(text2)

        cache = [[-1]*N for _ in range(M)]

        def dfs(i,j):
            if i == M or j == N:
                return 0
            
            if cache[i][j] != -1:
                return cache[i][j]
            

            if text1[i] == text2[j]:
                cache[i][j] = 1 + dfs(i+1,j+1)
            else:
                cache[i][j] =  max (dfs(i+1,j),dfs(i,j+1))
            
            return cache[i][j]
        
        return dfs(0,0)
            

        
        
        