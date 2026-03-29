class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:

        M, N = len(t1), len(t2)
        cache = [[None]*(N+1) for _ in range (M+1)]

        def dfs(i,j):
            if (i == M or j == N):
                return 0

            if cache[i][j] is not None:
                return cache[i][j]

            res = None
            if t1[i] == t2[j]:
                res =  1+ dfs(i+1,j+1)
            else:
                possibility1 = dfs(i+1,j)
                possibility2 = dfs(i,j+1)
                res = max (possibility1, possibility2)

            cache[i][j] =  res
            return res

        return dfs(0,0)
            

        
        
        