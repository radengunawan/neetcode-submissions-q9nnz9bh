class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        M, N = len(s), len(t)

        if (N > M):
            return 0
        
        def dfs(i,j):

            if j == N:
                return 1
            if i == M:
                return 0
            
            res = None
            if s[i] == t[j]:
                pick = dfs(i+1,j+1)
                skip = dfs(i+1,j)
                res = pick +skip
            else:
                res = dfs(i+1,j)

            return res

        return dfs(0,0)
