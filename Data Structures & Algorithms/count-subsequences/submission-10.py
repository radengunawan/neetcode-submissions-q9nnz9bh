class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
            
        m, n = len(s), len(t)
        cache = [[None]*n for _ in range (m)]

        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if cache[i][j] != None:
                return cache[i][j]
            
            if s[i] == t[j]:
                cache[i][j] = dfs(i+1,j+1) + dfs(i+1,j)
            else:
                cache[i][j] = dfs(i+1,j)
            
            return cache[i][j]
        
        return dfs(0,0)