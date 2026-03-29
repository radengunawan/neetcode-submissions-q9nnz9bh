class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
            
        m, n = len(s), len(t)
        cache = [[None]*(n+1) for _ in range (m+1)]

        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if cache[i][j] != None:
                return cache[i][j]
            
            res = dfs(i+1,j)
            if s[i] == t[j]:
                res += dfs(i+1,j+1)
                cache[i][j] = res
            
            return res
        
        return dfs(0,0)