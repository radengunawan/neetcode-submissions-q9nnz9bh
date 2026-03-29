class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        M, N = len(text1), len(text2)
        cache = {}

        def dfs(i,j):
            if (i == M or j == N):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]


            res = None
            if text1[i] == text2[j]:
                res =  1+ dfs(i+1,j+1)
            else:
                possibility1 = dfs(i+1,j)
                possibility2 = dfs(i,j+1)
                res = max (possibility1, possibility2)
                cache[(i,j)] =  res
            return res

        return dfs(0,0)
            

        
        
        